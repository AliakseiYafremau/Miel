
from fastapi.params import Depends
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.office_crud import get_office_by_id
from app.crud.statistics.candidate_crud import read_candidate_count, read_available_candidates_count, \
    read_invited_candidates
from app.models.models import Candidate, Manager, Office
from app.utils.database.test_data import get_session


async def read_all_offices_count(session: AsyncSession = Depends(get_session)):
    """Получение количества всех офисов"""
    request = select(func.count()).select_from(Office)
    result = await session.execute(request)
    all_offices = result.scalar_one()
    return all_offices


async def read_office_load(
    office_id: int, session: AsyncSession = Depends(get_session)
):
    """Получение загруженности офиса по id офиса"""
    request = await session.execute(select(Office).where(Office.id == office_id))
    office = request.scalars().first()

    if not office:
        return None

    total_candidates = await read_candidate_count(session)
    invited_candidates = await read_invited_candidates(session)
    hired_candidates = await read_available_candidates_count(True, session)

    return {
        "name": office.name,
        "location": office.location,
        "total_candidates": total_candidates,
        "invited_candidates": invited_candidates,
        "hired_candidates": hired_candidates,
    }


async def read_all_offices_load(session: AsyncSession = Depends(get_session)):
    """Получение загруженности всех офисов"""
    # Извлечение всех идентификаторов офисов
    result = await session.execute(select(Office.id))
    office_ids = result.scalars().all()

    # Список для хранения статистики по всем офисам
    offices_stats = []

    # Обход каждого офиса и получение его статистики
    for office_id in office_ids:
        office_load = await read_office_load(office_id, session)
        offices_stats.append(office_load)

    return offices_stats


async def read_office_by_manager_id(manager_id: int, session: AsyncSession = Depends(get_session)):
    """Получение офиса по id"""
    request = select(Office).join(Office, Manager.office_id == manager_id)
    result = await session.execute(request)
    office = result.scalars().first()

    if office:
        return {
            'id': office.id,
            'name': office.name,
            'location': office.location,
        }

    return office
