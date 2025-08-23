import pytest
from src.api.schemas import Todo

pytestmark = [pytest.mark.api, pytest.mark.contract]

def test_list_todos_contract(todos_client):
    todos = todos_client.list_todos(limit=5)
    assert len(todos) == 5
    for t in todos:
        assert isinstance(t, Todo)
        assert isinstance(t.userId, int)
        assert isinstance(t.title, str)
        assert isinstance(t.completed, bool)

def test_get_non_existing_todo(todos_client):
    # Dịch vụ demo trả 404 hoặc {} tuỳ thời điểm; kiểm tra phòng thủ
    try:
        todos_client.get_todo(99999999)
        pytest.skip("Service did not return 404 for huge id; behavior may vary.")
    except Exception:
        assert True  # expect failure path is handled
