from fastapi import status
from ..routers.users import get_current_user, get_db
from .utils import TestingSessionLocal, override_get_current_user, override_get_db, client, app, Todos, test_todo, test_user, Users

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/user/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'test_user'
    assert response.json()['email'] == 'test_uaer@gmail.com'
    assert response.json()['phone_number'] == '1234567890'
    assert response.json()['role'] == 'admin'
    assert response.json()['first_name'] == 'Test'
    assert response.json()['last_name'] == 'User'

def test_update_password_success(test_user):
    request_data = {
        'password': 'test_password',
        'new_password': 'new_password'
    }

    response = client.put("/user/password", json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_update_password_fail(test_user):
    request_data = {
        'password': 'wrong_password',
        'new_password': 'new_password'
    }
    response = client.put("/user/password", json=request_data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Not valid password'}

    response = client.put("/user/password", json=request_data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_update_phone_number(test_user):
    response = client.put("/user/phone_number/0987654321")
    assert response.status_code == status.HTTP_204_NO_CONTENT
