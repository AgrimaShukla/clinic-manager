import os
'''
This module is for managing all the queries
'''
class credentials_query:
    query_create = '''CREATE TABLE IF NOT EXISTS Credentials(
                                    uuid text primary key,
                                    role text,
                                    username text,
                                    password text

    )'''
    query_insert = 'INSERT INTO Credentials (uuid, role, username, password) VALUES (?, ?, ?, ?)'
    query_select1 = 'SELECT password, uuid FROM Credentials WHERE username = ?'
    query_select = 'SELECT role FROM Credentials WHERE username = ? AND password = ?'
class appointment_query:
    query_create = '''CREATE TABLE IF NOT EXISTS Appointments(
                                    patient_id text, 
                                    doctor_id text, 
                                    patient_name text, 
                                    doctor_name text, 
                                    date_time text
                                    )'''
    query_insert = 'INSERT INTO Appointments (patient_id, doctor_id, patient_name, doctor_name, date_time) VALUES (?, ?, ?, ?, ?)'
    query_delete = 'DELETE FROM Appointments WHERE patient_id = ? AND date_time = ?'
    query_select = 'SELECT * FROM Appointments WHERE patient_name = ? AND patient_id = ? ORDER BY date_time'
    query_appointment = 'SELECT patient_name, doctor_name, date_time FROM Appointments WHERE patient_id = ?'
    query_available = 'SELECT * from Appointments where doctor_id = ? AND date_time = ?'

class registration:
    query_create = '''CREATE TABLE IF NOT EXISTS REGISTRATION(
                                     id text primary key, 
                                     username text UNIQUE, 
                                     password text, 
                                     name text, 
                                     mobile_number INTEGER UNIQUE, 
                                     age INTEGER, gender text
                                     )'''

    query_insert = 'INSERT INTO REGISTRATION (id, username, password, name, mobile_number, gender) VALUES (?, ?, ?, ?, ?, ?)'
    query_select = 'SELECT id, password, name from REGISTRATION WHERE username = ?'


class doctor:
    query_create = '''CREATE TABLE IF NOT EXISTS DOCTOR(
                                      D_id text primary key, 
                                      name text, 
                                      mobile_number INTEGER UNIQUE, 
                                      age INTEGER, 
                                      gender text, 
                                      specialization text)'''
    query_insert = 'INSERT INTO DOCTOR (D_id, name, mobile_number, age, gender, specialization) VALUES (?, ?, ?, ?, ?, ?)'
    query_delete = 'DELETE FROM DOCTOR WHERE D_id = ?'
    query_select = 'SELECT name, specialization from DOCTOR'
    query_doc_appoint = 'SELECT D_id, name, specialization from DOCTOR'
    query_doc = 'SELECT name FROM DOCTOR WHERE D_id = ?'
    
class admin:
    query_create = '''CREATE TABLE IF NOT EXISTS ADMIN(
                                       A_id text primary key, 
                                       username text UNIQUE, 
                                       password text, 
                                       name text, 
                                       mobile_number INTEGER UNIQUE, 
                                       age INTEGER, 
                                       gender text
                                       )'''
    query_insert = 'INSERT INTO ADMIN (A_id, username, password, name, mobile_number, age, gender) VALUES (?, ?, ?, ?, ?, ?, ?)'
    query_select = 'SELECT password from ADMIN where username = ?'

class DatabasePath:
    DBPath = os.path.abspath(os.curdir) + "/src/database/data.db"
    TESTDB = "tests/test_data.db"