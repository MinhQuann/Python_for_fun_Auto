from .base_api import BaseAPI
from .schemas import Todo
from typing import List

class TodosAPI(BaseAPI):
    def get_todo(self, todo_id: int) -> Todo:
        resp = self.get(f"/todos/{todo_id}")
        resp.raise_for_status()
        return Todo.model_validate(resp.json())

    def list_todos(self, limit: int = 10) -> List[Todo]:
        resp = self.get("/todos")
        resp.raise_for_status()
        data = resp.json()[:limit]
        return [Todo.model_validate(x) for x in data]

    def create_todo(self, todo: Todo) -> Todo:
        resp = self.post("/todos", json=todo.model_dump(exclude_none=True))
        # Dịch vụ demo thường trả 201 + body echo lại
        assert resp.status_code in (200, 201)
        return Todo.model_validate(resp.json())
