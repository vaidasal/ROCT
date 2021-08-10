from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str

class User(UserBase):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    scope: Optional[list] = None

    class Config:
        orm_mode = True


class UserUpdate(User):
    password: str