from fastapi.testclient import TestClient
from main import app
from resources.doctor import get_user
from fastapi import status
import pytest

doctor = TestClient(app)




# app.dependency_overrides[user_dependency] = override_user_dependency

def test_get_doctor(admin_dependency):
        
        response = doctor.get("/doctor")
        assert response.status_code == status.HTTP_200_OK

def test_add_doctor(admin_dependency):
        request_data = {"name": "Aayush", "mobile_no": 98292019202, "age": 24, "gender": "male", "specialization": "ortho"}
        response = doctor.post("/doctor", json=request_data)
        assert response.status_code == status.HTTP_201_CREATED


def test_delete_doctor(admin_dependency):
        response = doctor.delete("/doctor/D_1334")
        assert response.status_code == status.HTTP_200_OK
        