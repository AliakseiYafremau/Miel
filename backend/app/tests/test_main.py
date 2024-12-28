from httpx import AsyncClient, ASGITransport
import pytest

from app.tests.confest import get_test_session as session
from app.tests.confest import app


@pytest.fixture(scope="module")
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


async def test_docs(client: AsyncClient):
    response = await client.get("/api/docs")
    assert response.status_code == 200
