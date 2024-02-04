from config.database_query import credentials_query, appointment_query, registration, doctor, admin
from database.database_access import QueryExecutor

def create_tables():
    QueryExecutor.non_returning_query(credentials_query.query_create)
    QueryExecutor.non_returning_query(appointment_query.query_create)
    QueryExecutor.non_returning_query(registration.query_create)
    QueryExecutor.non_returning_query(doctor.query_create)
    QueryExecutor.non_returning_query(admin.query_create)
   