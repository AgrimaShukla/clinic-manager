import shortuuid
from utils.validation import validate_age, validate_dname, validate_gender, validate_mobile_no, validate_special
from tabulate import tabulate
from database.database_conn import DatabaseConnection
from config.database_query import doctor, appointment_query, credentials_query
from config.prompts import PrintPrompts, InputPrompts
from database.database_access import QueryExecutor

class Doctor:
    
    def __init__(self) -> None:
        self.D_id = shortuuid.ShortUUID().random(length = 10)
        self.name = validate_dname()
        self.name = 'Dr ' + self.name
        self.mobile_no = validate_mobile_no()
        self.age = validate_age()
        self.gender = validate_gender()
        self.specialization = validate_special()
        Doctor.add_doctor(self)

   
    @staticmethod
    def create_doctor():
        QueryExecutor.non_returning_query(doctor.query_create)
    
    # @staticmethod
    def add_doctor(self):
        Doctor.create_doctor()
        QueryExecutor.non_returning_query(doctor.query_insert, (self.D_id, self.name, self.mobile_no, self.age, self.gender, self.specialization))

    @staticmethod
    def delete_doctor(d_id):
        QueryExecutor.non_returning_query(doctor.query_delete, (d_id, ))
    
    @staticmethod
    def show_doctor():
        table = QueryExecutor.returning_query(doctor.query_select)
        if not table:
            return False
        else:
            print(tabulate(table))
            return True
            
    
    @staticmethod
    def doctor_appoint():
        with DatabaseConnection("src/database/data.db") as connection:
            new_id = {}
            new_name = {}
            cursor = connection.cursor()
            rows = (app for app in cursor.execute(doctor.query_doc_appoint).fetchall())
            i = 1
            while True:
                for _ in range(5):
                    try:
                        row = next(rows)
                        new_id[i] = row[0]
                        new_name[i] = row[1]
                        print(f"{i}) Name: {row[1]} and Specialization: {row[2]}\n")
                        i += 1
                    except StopIteration:
                        #logger.debug("Stop Iteration encountered")
                        print()
                        break
                inp = int(input('Choose doctor for appointment: '))
                # print(new_id, new_name)
                return new_id[inp], new_name[inp]
            
    @staticmethod       
    def available_doctor(D_id, date_time):
        with DatabaseConnection("src/database/data.db") as connection:
            cursor = connection.cursor()
            date_time = cursor.execute(appointment_query.query_available, (D_id, date_time)).fetchone()
            if date_time is None:
                return True
        return False

    
        

