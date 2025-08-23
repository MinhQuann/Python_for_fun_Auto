from pydantic import BaseModel, Field

class Todo(BaseModel):
    userId: int = Field(..., ge=0)
    id: int | None = None
    title: str
    completed: bool
