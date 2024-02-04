from fastapi.testclient import TestClient
import main
from fastapi import status

main.server()
client = TestClient(main.server())

def test_check_Connection():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status': 'All good'}

def test_bool():
    pass
    # assert type('HEllo') is not str