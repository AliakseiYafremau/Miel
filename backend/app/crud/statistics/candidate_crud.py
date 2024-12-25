from fastapi.params import Depends
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from datetime import date, timedelta


from app.models.models import (
    Candidate,
    CandidateCourse,
    ManagerCandidate,
)
from app.utils.database.test_data import get_session


async def read_candidate_count_filter_date(date: date, session: AsyncSession = Depends(get_session)):
    """Получение количества кандидатов по интервалу дней"""
    request = (
        select(func.count()).select_from(Candidate).filter(Candidate.created_at >= date)
    )
    result = await session.execute(request)
    candidate_count_filter_date = result.scalar_one()
    return candidate_count_filter_date


async def read_candidates_statistics(session: AsyncSession = Depends(get_session)):
    """Получение статистики по кандидатам"""
    total_candidates = await read_candidate_count(session)
    last_day_candidates = await read_candidate_count_filter_date(
        date.today() - timedelta(days=1), session
    )
    last_week_candidates = await read_candidate_count_filter_date(
        date.today() - timedelta(weeks=1), session
    )
    last_month_candidates = await read_candidate_count_filter_date(
        date.today() - timedelta(days=30), session
    )
    favorite_candidates = await read_favorite_candidates(session)
    invited_candidates = await read_invited_candidates(session)
    hired_candidates = await read_available_candidates_count(True, session)
    return {
        "total": total_candidates,
        "last_day": last_day_candidates,
        "last_week": last_week_candidates,
        "last_month": last_month_candidates,
        "favorite": favorite_candidates,
        "invited": invited_candidates,
        "hired": hired_candidates,
    }


async def read_available_candidates_count(is_hired: bool, session: AsyncSession = Depends(get_session)):
    """Получение количества доступных/приглашенных кандидатов"""
    request = (
        select(func.count())
        .select_from(Candidate)
        .filter(Candidate.is_hired == is_hired)
    )
    result = await session.execute(request)
    available_candidates = result.scalar_one()
    return available_candidates


async def read_candidate_count(session: AsyncSession = Depends(get_session)):
    """Получение общего числа кандидатов"""
    request = select(func.count()).select_from(Candidate)
    result = await session.execute(request)
    count = result.scalar_one()
    return count


async def read_candidates_count_by_course_id(
    course_id: int, session: AsyncSession = Depends(get_session)
):
    """Получение количества кандидатов по id курса"""
    request = (
        select(func.count())
        .select_from(Candidate)
        .join(CandidateCourse)
        .filter(CandidateCourse.course_id == course_id)
    )
    result = await session.execute(request)
    candidates_count = result.scalar_one()
    return candidates_count


async def read_favorite_candidates(session: AsyncSession = Depends(get_session)):
    """Получение количества избранных кандидатов"""
    request = (
        select(func.count(Candidate.id.distinct()))
        .select_from(Candidate)
        .join(ManagerCandidate, Candidate.id == ManagerCandidate.candidate_id)
        .where(ManagerCandidate.is_favorite == True)
    )
    result = await session.execute(request)
    favorite_candidates_count = result.scalar_one()
    return favorite_candidates_count


async def read_invited_candidates(session: AsyncSession = Depends(get_session)):
    """Получение количества приглашенных кандидатов"""
    request = (
        select(func.count(Candidate.id.distinct()))
        .select_from(Candidate)
        .join(ManagerCandidate, Candidate.id == ManagerCandidate.candidate_id)
        .where(ManagerCandidate.is_invited == True)
    )
    result = await session.execute(request)
    invited_candidates_count = result.scalar_one()
    return invited_candidates_count


def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year

    # Проверяем, был ли день рождения в текущем году
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age


# Пример использования
# birthdate = date(1990, 5, 15)  # Например, 15 мая 1990 года
# age = calculate_age(birthdate)
# print(f"Возраст: {age} лет")


async def read_candidates_by_age(
    age_min: int, age_max: int, session: AsyncSession = Depends(get_session)
):
    """Получение количества кандидатов по возрасту"""
    request = (
        select(func.count())
        .select_from(Candidate)
        .filter(
            date.today() - timedelta(days=(365 * age_min))
            < Candidate.date_of_birth
            < date.today() - timedelta(days=(365 * age_max))
        )
    )
    result = await session.execute(request)
    candidate_by_age = result.scalar_one()
    return candidate_by_age
