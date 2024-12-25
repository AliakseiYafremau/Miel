from fastapi.params import Depends
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from urllib3 import request

from app.crud.statistics.candidate_crud import read_candidates_statistics
from app.crud.statistics.office_crud import read_office_load, read_office_by_manager_id

from app.models.models import Manager
from app.utils.database.test_data import get_session


async def read_manager_by_id(manager_id: int, session: AsyncSession = Depends(get_session)):
    """Получение руководителя по id"""
    request = select(Manager).where(Manager.id == manager_id)
    result = await session.execute(request)
    manager = result.scalars().first()
    if manager:
        return manager
    return None


# async def read_quotas_by_manager_id(manager_id: int, session: AsyncSession = Depends(get_session)):
#     """Получение числа квот руководителя"""
#     request = select(Manager.quotas).filter(Manager.id == manager_id)
#     result = await session.execute(request)
#     quotas = result.scalar_one()
#     if quotas:
#         return quotas
#     return None


async def read_managers_count(session: AsyncSession = Depends(get_session)):
    """Получение числа руководителей"""
    manager = await session.execute(select(func.count()).select_from(Manager))
    managers_count = manager.scalar_one()
    if managers_count:
        return managers_count
    return None


async def read_manager_statistics_by_id(manager_id: int, session: AsyncSession = Depends(get_session)):
    """Получение статистики руководителя по id"""
    request = select(Manager).where(Manager.id == manager_id)
    result = await session.execute(request)
    manager = result.scalars().first()
    office_load = await read_office_load(manager.office_id, session)
    return {
            "full_name": manager.full_name,
            "quotas": manager.quotas,
            "office": office_load,
    }


async def read_managers_statistics(session: AsyncSession = Depends(get_session)):
    """Получение статистики всех руководителей"""
    request = select(Manager.id)
    result = await session.execute(request)
    managers_ids = result.scalars().all()
    candidates = await read_candidates_statistics(session)
    managers_count = await read_managers_count(session)
    manager_statistics = []
    for manager_id in managers_ids:
        manager_stat = await read_manager_statistics_by_id(manager_id, session)
        manager_statistics.append(manager_stat)

    return {
        "total_managers": managers_count,
        "candidates_statistics": candidates,
        "managers_statistics": manager_statistics,
    }
