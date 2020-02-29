from SearchSystem import SearchSystem
from config import *
import logging

logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=FORMAT)
logger = logging.getLogger()

n = '\n'
t = '\t'
class SearchInterface:
    def __init__(self):
        self.search = SearchSystem()
        self.__load_data()
        logger.info('Initialized SearchInterface')

    def __load_data(self):
        for key in files:
            self.search.add_data(key, files[key])

    def print_help(self):
        logger.debug('Inside print_help')
        help_string = 'Help:\n'
        for d_type in data_types:
            help_string = f'{help_string}Search {d_type} with{n}'
            query_keys = self.search.get_query_keys(d_type)
            if query_keys:
                for key in query_keys:
                    help_string = f'{help_string}{key}{n}'

                help_string = f'{help_string}{n}'
                help_string = f'{help_string}------------------------------------------------{n}'
            else:
                logger.warn(f'No query keys found for data type {d_type}')

        print(help_string)

    def print_search(self, data_type, key, value):
        logger.debug('Inside print_search')
        query_results = self.search.query(data_type, key, value)
        if isinstance(query_results, str):
            print(query_results)
        else:
            for result in query_results:
                for key in result:
                    print(f'{key:30}{result[key]}')
                print()
                print('------------------------------------------------------------------')
                print()

    def commandline_interface(self):
        logger.debug('Inside commandline_interface')
        print('Welcome to Zendesk Query Prompt\n\t\tType search or s to search\n\t\tType help or h to view searchable fields\n\t\tType quit or q to exit')
        cmd = input()
        cmd = cmd.lower()
        while True:
            if cmd == 'h' or cmd == 'help':
                self.print_help()
            elif cmd == 'q' or cmd == 'quit':
                exit(0)
            elif cmd == 's' or cmd == 'search':
                intro_msg = 'Select a number from'
                for i in range(len(data_types)):
                    intro_msg = f'{intro_msg} {i+1}) {names[data_types[i]]}'
                print(intro_msg)
                try:
                    data_type = int(input())
                except ValueError as ve:
                    #log this
                    print('Please enter a valid number 1, 2, 3...')
                    data_type = int(input())
                data_type = data_types[data_type - 1]
                print('Enter Search term:')
                key = input()
                key = key.strip()
                print('Enter Search Value:')
                value = input()
                value = value.strip()
                self.print_search(data_type, key, value)
            else:
                logger.warn(f'Unidentified Command {cmd}')
                print('Please\n\t\tType search or s to search\n\t\tType help or h to view searchable fields\n\t\tType quit or q to exit')

            print('Please\n\t\tType search or s to search\n\t\tType help or h to view searchable fields\n\t\tType quit or q to exit')
            cmd = input()

if __name__ == '__main__':
    cli = SearchInterface()
    cli.commandline_interface()
