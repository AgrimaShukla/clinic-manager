from fastapi.testclient import TestClient
from main import app
from resources.doctor import user_dependency, get_user
from fastapi import status
import pytest

appointment = TestClient(app)


def override_user_dependency():
        return {'username': 'agrima18', 'id': 'Aex6cZquuS', 'role': "user"}

app.dependency_overrides[get_user] = override_user_dependency

# def test_get_appointments():
#         response = appointment.get("/appointment/Uu8y3")
#         assert response.status_code == status.HTTP_200_OK
