from database_conn import DatabaseConnection
class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age =  age
        self.gender = gender
    @staticmethod
    def create_patient():
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS patients(patient_id text primary key, patient_name text, age INTEGER, gender text)')
            
    @staticmethod
    def add_patient(patient_id, patient_name, age, gender):
        with DatabaseConnection('data.db') as connection:
            Patient.create_patient()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO patients VALUES(?, ?, ?, ?)", (patient_id, patient_name, age, gender))
            