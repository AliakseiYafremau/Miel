from httpx import AsyncClient



async def test_docs(client: AsyncClient):
    response = await client.get("/api/docs")
    assert response.status_code == 200


async def test_login(client: AsyncClient):
    response = await client.post(
        "/api/auth/login", data={"email": "scds", "password": "cdsc"}
    )
    assert response.status_code == 401
