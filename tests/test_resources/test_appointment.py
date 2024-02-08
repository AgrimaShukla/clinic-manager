from fastapi.testclient import TestClient
from main import app
from resources.appointments import get_user
from fastapi import status
import pytest

appointment = TestClient(app)



def test_get_appointments(customer_dependency):
        response = appointment.get("/appointment/Uu8y3")
        assert response.status_code == status.HTTP_200_OK

def test_add_appointments(customer_dependency):
        request_data = {"id": "U_567G", "D_id": "D_1334", "patient_name": "Niyati", "date-time": "2024/03/03"}
        response = appointment.post("/appointment", json=request_data)
        assert response.status_code == status.HTTP_201_CREATED
