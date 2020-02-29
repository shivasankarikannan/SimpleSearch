import logging
data_types = ['user', 'ticket', 'org']
files = { 'user': 'users.json',
        'ticket': 'tickets.json',
        'org': 'organizations.json'
        }
names = {'user': 'Users',
         'ticket': 'Tickets',
         'org': 'Organizations'
        }
LOG_FILE = 'search_logger.log'
LOG_LEVEL = logging.INFO
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
