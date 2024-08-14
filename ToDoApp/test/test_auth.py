from .utils import TestingSessionLocal, override_get_db, app, test_user
from ..routers.auth import get_current_user, get_db, auth_user, create_access_token, SECRET_KEY, ALGORITHM
from jose import jwt
from datetime import timedelta
import pytest
from fastapi import HTTPException

app.dependency_overrides[get_db] = override_get_db

def test_auth_user(test_user):
    db = TestingSessionLocal()

    authed_user = auth_user(test_user.username, 'test_password', db)
    assert authed_user is not None
    assert authed_user.username == test_user.username

    authed_user = auth_user('non_existent_user', 'test_password', db)
    assert authed_user is False

    authed_user = auth_user(test_user.username, 'wrong_password', db)
    assert authed_user is False

def test_create_access_token():
    username = 'test_user'
    user_id = 1
    role = 'user'
    expires_delta = timedelta(days=1)

    token = create_access_token(username, user_id, role, expires_delta)

    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert decoded_token.get('sub') == username
    assert decoded_token.get('user_id') == user_id
    assert decoded_token.get('role') == role

@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    encode = {'sub': 'test_user', 'user_id': 1, 'role': 'admin' }
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    current_user = await get_current_user(token)

    assert current_user == {'username': 'test_user', 'id': 1, 'user_role': 'admin' }

@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    encode = {'role': 'user'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    with pytest.raises(HTTPException) as e:
        await get_current_user(token)

    assert e.value.status_code == 401
    assert e.value.detail == 'Invalid Token'