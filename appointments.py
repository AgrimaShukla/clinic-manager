from tabulate import tabulate
import csv, patient, doctor
from time import strptime
from datetime import datetime
from database_conn import DatabaseConnection
class Appointment:
    def __init__(self, doctor, patient, date_time):
        self.doctor = doctor
        self.patient =  patient
        self.date_time = date_time
           
class Clinic:
    
    @staticmethod
    def create_appointment():
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Appointments(patient_id text, patient_name text, doctor_name text, date_time text)')

    @staticmethod
    def add_appointment(p_id, patient_name, doctor_name, date_time):
        with DatabaseConnection('data.db') as connection:
            Clinic.create_appointment()
            cursor = connection.cursor()
            print(p_id)
            cursor.execute("INSERT INTO Appointments (patient_id, patient_name, doctor_name, date_time) VALUES (?, ?, ?, ?)", (p_id, patient_name, doctor_name, date_time))

    @staticmethod
    def all_appointment():
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            while True:
                cursor.execute("SELECT * FROM Appointments ")
                row = cursor.fetchone()
                if row is None:
                    break
                yield row


    @staticmethod
    def delete_appointment(name, date_time):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Appointments WHERE patient_name = ? AND date_time = ?", (name, date_time))

    @staticmethod
    def my_appointments(name):
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            txt = cursor.execute("SELECT patient_name, date_time from Appointments WHERE patient_name = ?", (name,))
            print(tabulate(txt))


