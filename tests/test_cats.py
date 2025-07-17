import pytest
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from httpx import ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_get_all_breeds():
    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.get("/breeds/")
            assert response.status_code == 200
            assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_search_breeds():
    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.get("/breeds/search/?q=sib")
            assert response.status_code == 200
            assert isinstance(response.json(), list)
