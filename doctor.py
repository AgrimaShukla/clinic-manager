from database_conn import DatabaseConnection
class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def create_doctors():
        with DatabaseConnection('data.db') as connection:
            cursor = connection.execute()
            cursor.execute('CREATE TABLE IF NOT EXISTS doctors(doctor_name)')
          