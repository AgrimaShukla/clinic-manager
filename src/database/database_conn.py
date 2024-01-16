'''
This module is for Context Manager of database connection
'''

import sqlite3
import logging
logger = logging.getLogger('database')

class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = "src/data.db"

    def __enter__(self):
         self.connection = sqlite3.connect(self.host)
         return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            logger.error(f'{exc_type} error occurred')
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
