import pytest

from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.db import get_session
from app.models.models import Base
from app.main import app


test_db_url = "sqlite+aiosqlite:///./test.db"
test_engine = create_async_engine(test_db_url, echo=True)

TestAsyncSessionFactory = sessionmaker(
    bind=test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_test_session() -> AsyncGenerator:
    async with TestAsyncSessionFactory() as session:
        yield session


@pytest.fixture(scope="module", autouse=True)
async def setup():
    async with test_engine.connect() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with test_engine.connect() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="module")
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


app.dependency_overrides[get_session] = get_test_session
