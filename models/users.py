from pymongo import IndexModel, ASCENDING
from pydantic import BaseModel

from pydantic import BaseModel, EmailStr

class Users(BaseModel):
    user_name: str
    password: str
    age: int
    email: EmailStr  # Assuming you want to store email addresses
    full_name: str   # Full name of the user
    is_active: bool  # Indicates whether the user account is active or not

    class Settings:
        name = "user_collection"
        indexes = [
            IndexModel(
                [("user_name", ASCENDING)],
                name="user_name_index",
                unique=True
            )
        ]
