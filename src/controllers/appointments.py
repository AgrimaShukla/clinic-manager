'''
This module is for appointment management
- create appointment
- add appointment
- delete appointment
- showing all appointment
'''

import logging
from flask import Flask
from database.database_access import QueryExecutor
from config.database_query import appointment_query, doctor
from config.prompts import PrintPrompts, InputPrompts
from database.database_access import DatabaseConnection

logger = logging.getLogger("Appointment")       

class Clinic:
    
    @staticmethod
    def create_appointment()->None:
        QueryExecutor.non_returning_query(appointment_query.query_create)

    @staticmethod
    def add_appointment(p_id, D_id, patient_name, doctor_name, date_time)->None:
        result = QueryExecutor.non_returning_query(appointment_query.query_insert, (p_id, D_id, patient_name, doctor_name, date_time))
        return result


    @staticmethod
    def delete_appointment(p_id, date_time)->None:
        result = QueryExecutor.non_returning_query(appointment_query.query_delete, (p_id, date_time))
        print(PrintPrompts.APPOINTMENT_DELETED)
        return result

    def get_doctor_for_appointment(self, d_id):
        name = QueryExecutor.returning_query(doctor.query_doc, (d_id, ))
        return name
    
    def get_all_appointments(self, p_id):
        data = QueryExecutor.returning_query(appointment_query.query_appointment, (p_id,))
        response_data = [{
            "patient_name": i[0],"doctor_name": i[1],"date_time": i[2]} for i in data
        ]
        return response_data
    
    
    @staticmethod
    def my_appointments(name, id)->None:
        with DatabaseConnection('src/database/data.db') as connection:
            # new_dict = {}
            new_dict2 = {}
            cursor = connection.cursor()
            try:
                rows = (app for app in cursor.execute(appointment_query.query_select, (name, id)).fetchall())
            except:
                print(PrintPrompts.NOT_FOUND)
            else:
                i = 1
                while True:
                    for _ in range(5):
                        try:
                            row = next(rows)
                            # new_dict[i] = row[0]
                            new_dict2[i] = row[4]
                            print(f"{i}) Name: {row[2]} with Doctor: {row[3]} on Date: {row[4]}\n ")
                            i += 1
                        except StopIteration:
                            logger.debug("Stop Iteration encountered")
                            print(PrintPrompts.NO_APPOINTMENTS)
                            break
                    print(PrintPrompts.APPOINTMENT_MENU)
                    str1 = input(InputPrompts.ENTER)
                    if str1 == '2':
                        inp = int(input(InputPrompts.CANCEL))
                        return new_dict2[inp]
                    elif str1 == '3':
                        break
                    elif str1 != '1':
                        print(PrintPrompts.INVALID_INPUT)

