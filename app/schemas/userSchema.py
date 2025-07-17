from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    nombres: str
    apellidos: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str
    username: str
    nombres: str
    apellidos: str
    email: EmailStr

class UserLogin(BaseModel):
    username: str
    password: str
