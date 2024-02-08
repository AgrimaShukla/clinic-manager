from main import app
from fastapi.testclient import TestClient
from fastapi import status
from utils.registration import DatabasePath
import pytest
from fastapi import HTTPException
auth = TestClient(app)

def test_register(package_mocker):
    package_mocker.patch.object(DatabasePath, 'DBPath', DatabasePath.TESTDB)
    request_data = {
        "username": "ashukla",
        "password": "ashukla",
        "name": "agrima",
        "mobile_number": "9839393939",
        "gender": "female"
    }
    # with pytest.raises(HTTPException) as e:
    response = auth.post("/register", json=request_data)
    print("*"*50)
    # print(e)
    # raise HTTPException(409, detail="User already exists")
# print(e.)
    assert response.status_code== status.HTTP_409_CONFLICT