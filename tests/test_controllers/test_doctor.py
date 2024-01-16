from controllers.doctor import Doctor, QueryExecutor, DatabaseConnection
import pytest

# @pytest.fixture
# def doctor_fixture(mocker):
    
#     return obj_doctor

@pytest.fixture
def mock_database_connection(mocker):
    mock_connection = mocker.MagicMock(spec = DatabaseConnection)
    mocker.patch('database.database_access.DatabaseConnection', return_value = mock_connection)
    mock_cursor = mocker.MagicMock()
    mock_connection.__enter__.return_value.cursor.return_value = mock_cursor
    mock_connection.__exit__.return_value = None
    return mock_cursor


class TestDoctor:
    def test_init_func(self, mocker):
        mocker.patch('controllers.doctor.validate_dname', lambda : 'agrime')
        mocker.patch('controllers.doctor.validate_mobile_no', lambda : '9092020020')
        mocker.patch('controllers.doctor.validate_age', lambda : '21')
        mocker.patch('controllers.doctor.validate_gender', lambda : 'female')
        mocker.patch('controllers.doctor.validate_special', lambda : 'ortho')
        mock_add_doctor = mocker.Mock()
        mocker.patch.object(Doctor, 'add_doctor', mock_add_doctor)
        Doctor()
        mock_add_doctor.assert_called_once()

    def test_create_doctor(self, mocker):
        mock_obj = mocker.Mock()
        mocker.patch.object(QueryExecutor, 'non_returning_query', mock_obj)
        Doctor.create_doctor()
        mock_obj.assert_called_once()

    def test_delete_doctor(self, mocker):
        mock_query = mocker.Mock()
        mocker.patch.object(QueryExecutor, 'non_returning_query', mock_query)

    # def test_available_doctor(self, mocker, mock_database_connection):
    #     mock_cursor = mock_database_connection
    #     mock_cursor.execute().fetchall.return_value = [('agrima', ), ('21', )]
    #     Doctor.available_doctor('D_123', '01-11-2024')
    #     mock_cursor.execute.assert_called_once()
        
