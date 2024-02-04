import pytest
from utils.create_tables import create_tables
from config.database_query import credentials_query, admin, appointment_query, registration, doctor

from database.database_access import DatabasePath, QueryExecutor

@pytest.fixture(scope='package',autouse=True)
def create_test_db(package_mocker):
    package_mocker.patch.object(DatabasePath, 'DBPath', DatabasePath.TESTDB)

    create_tables()
    # yield
    # QueryExecutor.non_returning_query('DROP DATABASE test_data')

@pytest.fixture(scope='package', autouse=True)
def insert_into_table():
    QueryExecutor.non_returning_query(credentials_query.query_insert, ('Uu8y3', 'user', 'ashukla', 'ashukla'))
    QueryExecutor.non_returning_query(admin.query_insert, ('Uu8y3', 'ashukla', 'ashukla', 'Agrima', 92092020202, 23, 'female'))
    QueryExecutor.non_returning_query(appointment_query.query_insert, ('Uu8y3', 'D_1334', 'niyati', 'harshit', '2024/03/02'))
    QueryExecutor.non_returning_query(doctor.query_insert, ('D_1334', 'harshit', 8374029380, 34, 'male', 'ortho'))
    yield
    QueryExecutor.non_returning_query('DROP TABLE Credentials')
    QueryExecutor.non_returning_query('DROP TABLE Appointments')
    QueryExecutor.non_returning_query('DROP TABLE DOCTOR')
    QueryExecutor.non_returning_query('DROP TABLE ADMIN')
    QueryExecutor.non_returning_query('DROP TABLE REGISTRATION')
