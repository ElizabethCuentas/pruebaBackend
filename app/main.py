from fastapi import FastAPI
from app.api.routers import cats, users

app = FastAPI(title="Cat & User API")

app.include_router(cats.router, prefix="/breeds", tags=["Cats"])
app.include_router(users.router, prefix="/user", tags=["Users"])
