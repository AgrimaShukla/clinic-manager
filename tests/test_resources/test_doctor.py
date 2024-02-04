from fastapi.testclient import TestClient
from main import app
from resources.doctor import user_dependency, get_user
from fastapi import status
import pytest

doctor = TestClient(app)


def override_user_dependency():
        return {'username': 'agrima18', 'id': 'Aex6cZquuS', 'role': "admin"}

app.dependency_overrides[get_user] = override_user_dependency
# app.dependency_overrides[user_dependency] = override_user_dependency

def test_get_doctor():
        response = doctor.get("/doctor")
        assert response.status_code == status.HTTP_200_OK

def test_add_doctor():
        request_data = {"name": "Aayush", "mobile_no": 98292019202, "age": 24, "gender": "male", "specialization": "ortho"}
        response = doctor.post("/doctor", json=request_data)
        print(str(response))
        assert response.status_code == status.HTTP_201_CREATED


def test_delete_doctor():
        response = doctor.request("DELETE", "/doctor/D_1334")
        assert response.status_code == status.HTTP_200_OK
        