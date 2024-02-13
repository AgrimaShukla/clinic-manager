import shortuuid
import maskpass
from utils import validation
from utils.encrypt import encrypt, decrypt
from database.database_conn import DatabaseConnection
from config.database_query import admin, DatabasePath

from controllers.admin_table import Admin
from config.prompts import PrintPrompts

class Register_admin:
    def __init__(self):
        self.A_id = shortuuid.ShortUUID().random(length = 10)
        self.username = validation.validate_user()
        self.password = maskpass.advpass()
        self.password = encrypt(self.password)
        self.name = validation.validate_dname()
        self.mobile_no = validation.validate_mobile_no()
        self.age = validation.validate_age()
        self.gender = validation.validate_gender()
        Admin.add_admin(self.A_id, self.username, self.password, self.name, self.mobile_no, self.age, self.gender)

    def check_admin():
        with DatabaseConnection(DatabasePath.DBPath) as connection:
            attempts = 3
            print(PrintPrompts.LOGIN)
            while attempts > 0:
                u_name = input("Enter username: ")
                password = maskpass.advpass()
                cursor = connection.cursor()
                pw = cursor.execute(admin.query_select, (u_name, )).fetchone()
                if pw is None:
                    print(PrintPrompts.INVALID)
                    attempts = attempts - 1
                    continue
                else:
                    try:
                        pass_word = decrypt(pw[0])
                        password = bytes(password, 'utf-8')
                        # print(pass_word)
                        if password == pass_word:
                            print(PrintPrompts.SUCCESS)
                            return True
                        else:
                            attempts = attempts - 1
                            raise Exception
                    except:
                        print(PrintPrompts.INVALID)

        return False
