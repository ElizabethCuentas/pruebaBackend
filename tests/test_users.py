import pytest
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from httpx import ASGITransport
from uuid import uuid4
from app.main import app

@pytest.mark.asyncio
async def test_create_and_login_user():
    unique_email = f"{uuid4().hex}@test.com"
    user_data = {
        "nombres": "Elizabeth",
        "apellidos": "Cuentas",
        "email": unique_email,
        "password": "secure123"
    }

    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post("/user/", json=user_data)
            assert response.status_code == 201

            login_response = await ac.get("/user/login", params={
                "email": user_data["email"],
                "password": user_data["password"]
            })

            assert login_response.status_code == 200
            assert "access_token" in login_response.json()
