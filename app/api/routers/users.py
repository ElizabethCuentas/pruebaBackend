from fastapi import APIRouter, HTTPException
from app.schemas.userSchema import UserCreate, UserOut, UserLogin
from app.services import userService
from typing import List

router = APIRouter()

@router.get("/", response_model=List[UserOut])
async def get_users():
    return await userService.get_all_users()

@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate):
    return await userService.create_user(user)

@router.get("/login", response_model=UserOut)
async def login_user(credentials: UserLogin):
    user = await userService.login_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
