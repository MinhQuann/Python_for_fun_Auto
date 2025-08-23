import pytest
from src.api.schemas import Todo

pytestmark = pytest.mark.api

@pytest.mark.smoke
def test_get_todo_1_smoke(todos_client):
    todo = todos_client.get_todo(1)
    assert isinstance(todo, Todo)
    assert todo.id == 1
    assert isinstance(todo.title, str)

def test_create_todo_smoke(todos_client):
    new = Todo(userId=1, title="learn pytest", completed=False)
    created = todos_client.create_todo(new)
    assert created.title == new.title
    assert created.completed is False
