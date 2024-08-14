from fastapi.testclient import TestClient
import pytest
from ..main import app
from fastapi import status

client = TestClient(app)

def test_health_check():
    response = client.get('/health')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status': 'ok'}