from fastapi.params import Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Office
from app.utils.database.test_data import get_session


async def get_offices(session: AsyncSession = Depends(get_session)):
    """Получение всех офисов"""
    request = select(Office)
    result = await session.execute(request)
    all_offices = result.scalars().all()
    return all_offices


async def get_office_by_id(id: int, session: AsyncSession = Depends(get_session)):
    """Получение офиса по id"""
    office = await session.get(Office, id)
    if office:
        return office
    return None
