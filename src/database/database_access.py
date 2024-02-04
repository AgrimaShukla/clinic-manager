from database.database_conn import DatabaseConnection
from config.prompts import PrintPrompts, InputPrompts
import sqlite3
import logging
from config.database_query import DatabasePath

logger = logging.getLogger("Database")   
class QueryExecutor:

    @staticmethod
    def returning_query(query, params = None):
        with DatabaseConnection(DatabasePath.DBPath) as connection:
            cursor = connection.cursor()
            if params:
                data = cursor.execute(query, params).fetchall()
                # print(data)
                return data
            data = cursor.execute(query).fetchall()
            return data
        

    @staticmethod
    def non_returning_query(query, params = None):
        # try:
            with DatabaseConnection(DatabasePath.DBPath) as connection:
                cursor = connection.cursor()
                if params:
                    cursor.execute(query, params)
                    return True
                else:
                    cursor.execute(query)
                    return True
                
    @staticmethod
    def single_returning_query(query, params = None):
        
        with DatabaseConnection(DatabasePath.DBPath) as connection:
            cursor = connection.cursor()
            if params:
                data = cursor.execute(query, params).fetchone()
                return data
            data = cursor.execute(query)
            return data
        
        # except sqlite3.Error as e:
        #     logging.debug(e)
        #     print(PrintPrompts.ERROR)
        #     return False