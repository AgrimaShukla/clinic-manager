from database.database_conn import DatabaseConnection
from config.database_query import admin

class Admin:
    def create_admin():
        with DatabaseConnection("src/database/data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(admin.query_create)

    def add_admin(a_id, username, password, name, mobile_number, age, gender):
        Admin.create_admin()
        with DatabaseConnection("src/database/data.db") as connection:
            cursor = connection.cursor()
            cursor.execute(admin.query_insert, (a_id, username, password, name, mobile_number, age, gender))
