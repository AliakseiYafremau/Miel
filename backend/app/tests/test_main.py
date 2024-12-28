from httpx import AsyncClient, ASGITransport

from app.main import app


test_client = AsyncClient(
    transport=ASGITransport(app=app),
    base_url="http://test",
)


async def test_create_user():
    response = await test_client.get("/api/docs")
    assert response.status_code == 200