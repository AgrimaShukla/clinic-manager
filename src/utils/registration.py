'''
This module is for registering and logging user
'''

import logging
import shortuuid
import maskpass
from database.database_conn import DatabaseConnection
from utils import validation
from config.database_query import registration, credentials_query, DatabasePath
from utils.encrypt import encrypt, decrypt
from config.prompts import PrintPrompts, InputPrompts
from database.database_access import QueryExecutor
from config.database_query import registration, DatabasePath
logger = logging.getLogger('reg')

class Registration:

    def register_user(self, uuid, username, password, name, mobile_number, gender) -> str:
        
        password = encrypt(password)
        # print(username)
        obj_query = QueryExecutor()
        result = obj_query.returning_query(credentials_query.query_select1, (username,))
        print(result)
        # if result:
        #     print('Username already exists')
        #     return False
        with DatabaseConnection(DatabasePath.DBPath) as connection:
            cursor = connection.cursor()
            cursor.execute(credentials_query.query_insert, (uuid, 'user', username, password))
            cursor.execute(registration.query_create)
            cursor.execute(registration.query_insert, (uuid, username, password, name, mobile_number, gender))
        return uuid, name
    

    # registering user
    def reg(self)->str:
        with DatabaseConnection(DatabasePath.DBPath) as connection:
            cursor = connection.cursor()
            cursor.execute(registration.query_create)
            self.p_id, self.name = Registration.register_user(self)
            return self.p_id, self.name


# Login user
def login(u_name, u_pw):
    
    pw = None
    with DatabaseConnection(DatabasePath.DBPath) as connection:
        cursor = connection.cursor()
        pw = cursor.execute(credentials_query.query_select1, (u_name,)).fetchone()

    if pw is None:
        print(PrintPrompts.INVALID)
        return False
        
    else:
        password = decrypt(pw[0])
        u_pw = bytes(u_pw, 'utf-8')
    # print(u_pw) 
    if password == u_pw:
        print(PrintPrompts.SUCCESS)
        role = QueryExecutor.single_returning_query(credentials_query.query_select, (u_name, pw[0]))
        return role, pw[0], pw[1]
    else:
        logger.error('Invalid username or password')
        return False
