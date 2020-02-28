import json

data_types = ['user', 'ticket', 'org']
foreign_keys = {'user': {'organization_id': ('org', '_id')},
            'ticket': {'submitter_id': ('user', '_id')}
        }

class SearchSystem:
    def __init__(self):
        self.data = {}
        self.index = {}
        for d_type in data_types:
            self.data[d_type] = []
            self.index[d_type] = {}

    def __get_data_type(self, file_name):
        for d_type in data_types:
            if d_type in file_name:
                return d_type

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

    def get_query_keys(self, data_type):
        if data_type not in self.data:
            return None
        if not self.data[data_type]:
            return None
        #print(self.data[data_type][0].keys())
        query_keys = list(self.data[data_type][0].keys())
        return query_keys

    def add_data(self, data_type, file_name):
        data = json.load(open(file_name))
        data_type = self.__get_data_type(file_name)
        self.__index(data, data_type)
        self.data[data_type] = data

    def query(self, data_type, key, value):
        #Add logs here
        if data_type not in self.index:
            return "Please choose a valid data type"
        if key not in self.index[data_type]:
            return "Please enter a valid search term"
        if value not in self.index[data_type][key]:
            return "There is no data for that query"
        indices = self.index[data_type][key][value]
        query_data = []
        for idx in indices:
            query_data.append(self.data[data_type][idx])
        return query_data


if __name__ == '__main__':
    search = SearchSystem()
    search.add_data('users.json')
    #print(search.data)
    #print(search.index)
    query_data = search.query('user', 'suspended', False)
    print(query_data)
