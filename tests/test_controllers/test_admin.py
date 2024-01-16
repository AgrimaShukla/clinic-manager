import pytest
from controllers.admin import Register_admin, Admin

@pytest.fixture
def mock_admin(mocker):
    # reg_admin_obj = Register_admin()
    mock_admin = mocker.Mock()
    mocker.patch('controllers.admin.Admin', mock_admin)
    return mock_admin

class TestAdmin:

    def test_add_admin(self, mocker, mock_admin):
        mocker.patch('controllers.admin.validation', side_effect = ['agrima123', 'Agrima', '9898202920', '21', 'female'])
        mocker.patch('controllers.admin.maskpass.advpass', lambda **kwargs: 'agrima')
        mocker.patch('controllers.admin.encrypt', lambda a: None)
        Register_admin()
        mock_admin.add_admin.assert_called_once()

        
