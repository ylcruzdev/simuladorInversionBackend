from beanie import Document
from pydantic import EmailStr, Field

class User(Document):
    name: str
    email: EmailStr
    password: str
    isActive: bool = True

    class Settings:
        name = "users"