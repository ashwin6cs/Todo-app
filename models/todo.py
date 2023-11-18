from pydantic import BaseModel

class Todo(BaseModel):
    user_id: str
    name: str
    description: str
    complete: bool


