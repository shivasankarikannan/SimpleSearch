import json
from config import *
import logging
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=FORMAT)

#add_format
logger = logging.getLogger()

class SearchSystem:
    def __init__(self):
        self.data = {}
        self.index = {}
        for d_type in data_types:
            self.data[d_type] = []
            self.index[d_type] = {}
        logger.info('Initialized SearchSystem')

    def __index(self, data, data_type):
        for i in range(len(data)):
            item = data[i]
            for key in item:
                value = item[key]
                if key not in self.index[data_type]:
                    self.index[data_type][key] = {}
                if isinstance(value, list):
                    for val in value:
                        if not isinstance(val, str):
                            val = str(val)
                        if val not in self.index[data_type][key]:
                            self.index[data_type][key][val] = []
                        self.index[data_type][key][val].append(i)
                else:
                    if not isinstance(value, str):
                        value = str(value)
                    if value not in self.index[data_type][key]:
                        self.index[data_type][key][value] = []
                    self.index[data_type][key][value].append(i)
        logger.info('Finished Indexing Data')

    def get_query_keys(self, data_type):
        logger.debug(f'Inside get_query_keys input_params: {data_type}')
        if data_type not in self.data:
            logger.warn(f'{data_type} data type not in data')
            return None
        if not self.data[data_type]:
            logger.warn(f'Data of type {data_type} is empty')
            return None
        query_keys = list(self.data[data_type][0].keys())
        logger.debug(f'Returning data {query_keys}')
        return query_keys

    def add_data(self, data_type, file_name):
        data = json.load(open(file_name))
        self.__index(data, data_type)
        self.data[data_type] = data
        logger.info(f'Successfully added data of type {data_type}')

    def query(self, data_type, key, value):
        logger.debug('Inside query method')
        if data_type not in self.index:
            logger.error(f'Wrong data type provided {data_type}')
            return "Please choose a valid data type"
        if key not in self.index[data_type]:
            logger.error(f'Wrong key {key} provided in data of type {data_type}')
            return "Please enter a valid search term"
        if value not in self.index[data_type][key]:
            logger.error(f'Invalid search value {value}')
            return "There is no data for that query"
        indices = self.index[data_type][key][value]
        query_data = []
        for idx in indices:
            query_data.append(self.data[data_type][idx])
        logger.debug(f'Returning data {query_data}')
        return query_data


if __name__ == '__main__':
    search = SearchSystem()
    search.add_data('users.json')
    #print(search.data)
    #print(search.index)
    query_data = search.query('user', 'suspended', False)
    print(query_data)
