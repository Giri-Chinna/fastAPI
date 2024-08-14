from fastapi import status
from ..routers.todos import get_current_user, get_db
from .utils import TestingSessionLocal, override_get_current_user, override_get_db, client, app, Todos, test_todo


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_read_all_authenticted(test_todo):
    response = client.get("/todos/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{"id": 1, "title": "Test Todo", "description": "Test Description", "priority": 1, "complete": False, "owner_id": 1}]
    
def test_read_one_authenticted(test_todo):
    response = client.get("/todos/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"id": 1, "title": "Test Todo", "description": "Test Description", "priority": 1, "complete": False, "owner_id": 1}

def test_read_all_authenticted_not_found(test_todo):
    response = client.get("/todos/todo/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found'}

def test_create_todo_authenticted(test_todo):
    request_data = {
        "title": "New Todo",
        "description": "New Description",
        "priority": 2,
        "complete": False
    }
    response = client.post("/todos/todo", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 2).first()
    assert model.title == request_data.get('title')
    assert model.description == request_data.get('description')

def test_update_todo(test_todo):
    request_data = {
        'title': 'Updated Todo',
        'description': 'Test Description',
        'priority': 1,
        'complete': False
    }

    response = client.put("/todos/todo/1", json=request_data)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model.title == request_data.get('title')
    assert model.description == request_data.get('description')

def test_update_todo_not_found(test_todo):
    request_data = {
        'title': 'Updated Todo',
        'description': 'Test Description',
        'priority': 1,
        'complete': False
    }

    response = client.put("/todos/todo/999", json=request_data)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found'}

def test_delete_todo(test_todo):
    response = client.delete('/todos/todo/1')
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None

def test_delete_todo_not_found():
    response = client.delete('/todos/todo/999')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found'}