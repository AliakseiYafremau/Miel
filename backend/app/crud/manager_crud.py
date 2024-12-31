import datetime
from typing import Annotated, List

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload, joinedload, aliased

from app.core.db import get_session
from app.models.models import (
    Manager,
    Candidate,
    ManagerCandidate,
    CandidateCourse,
    CandidateSkill,
)
from app.schemas.manager_schema import sortBy
from app.core.logging import logger


async def read_manager_by_id(
    manager_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Поиск руководителя по id"""
    logger.debug(
        f"[yellow]read_manager_by_id[/] | Поиск руководителя по id({manager_id})"
    )

    request = (
        select(Manager)
        .where(Manager.id == manager_id)
        .options(
            joinedload(Manager.candidates).selectinload(ManagerCandidate.candidate)
        )
        .options(selectinload(Manager.office))
    )

    result = await session.execute(request)
    manager = result.scalars().first()

    if manager:
        logger.debug("[yellow]read_manager_by_id[/] | Руководитель найден")
        return manager
    logger.error("[yellow]read_manager_by_id[/] | Руководитель не найден")
    return None


async def read_candidates_by_manager_id(
    manager_id: int, session: Annotated[AsyncSession, Depends(get_session)]
):
    """Получение кандидатов руководителя по id"""
    logger.debug(
        f"[yellow]read_candidates_by_manager_id[/] | Получение кандидатов руководителя по id({manager_id})"
    )

    request = (
        select(Candidate)
        .join(ManagerCandidate, Candidate.id == ManagerCandidate.candidate_id)
        .options(joinedload(Candidate.courses).joinedload(CandidateCourse.course))
        .options(joinedload(Candidate.skills).joinedload(CandidateSkill.skill))
        .where(ManagerCandidate.done_by == manager_id)
    )

    result = await session.execute(request)
    candidates = result.unique().scalars().all()

    return candidates


async def read_available_candidates(
    session: Annotated[AsyncSession, Depends(get_session)],
    manager_id: int = None,
    min_age: int = None,
    max_age: int = None,
    courses: List[int] = None,
    sort_by: str = None,
):
    """Получение доступных кандидатов"""
    logger.debug(
        "[yellow]read_available_candidates[/] | Получение доступных кандидатов"
    )

    request = select(Candidate).where(Candidate.is_hired == False)
    subquery = aliased(
        ManagerCandidate,
        select(ManagerCandidate)
        .where(ManagerCandidate.done_by == manager_id)
        .subquery(),
    )

    request = (
        select(Candidate)
        .join(ManagerCandidate, Candidate.id == ManagerCandidate.candidate_id)
        .where(Candidate.is_hired == False)
        .options(joinedload(Candidate.courses).joinedload(CandidateCourse.course))
        .options(joinedload(Candidate.skills).joinedload(CandidateSkill.skill))
        .options(joinedload(Candidate.managers.of_type(subquery)))
        .group_by(
            Candidate, ManagerCandidate.is_invited
        )  # Указываем конкретные столбцы
    )

    # Фильтрация по возрасту
    if min_age:
        logger.debug(
            f"[yellow]read_available_candidates[/] | Фильтрация по возрасту({min_age})"
        )

        today = datetime.date.today()
        max_date = today.replace(year=today.year - min_age)
        request = request.where(Candidate.date_of_birth <= max_date)

    if max_age:
        logger.debug(
            f"[yellow]read_available_candidates[/] | Фильтрация по возрасту({max_age})"
        )

        today = datetime.date.today()
        min_date = today.replace(year=today.year - max_age)
        request = request.where(Candidate.date_of_birth >= min_date)

    # Фильтрация по курсам
    if courses:
        logger.debug(
            f"[yellow]read_available_candidates[/] | Фильтрация по курсам({courses})"
        )

        request = request.join(Candidate.courses).where(
            CandidateCourse.course_id.in_(courses)
        )

    # Сортировка
    if sort_by == sortBy.is_invited:
        logger.debug(
            "[yellow]read_available_candidates[/] | Сортировка по приглашенности"
        )

        request = request.order_by(ManagerCandidate.is_invited == True)
    elif sort_by == sortBy.is_free:
        logger.debug(
            "[yellow]read_available_candidates[/] | Сортировка по свободности"
        )

        request = request.order_by(ManagerCandidate.is_invited == False)

    result = await session.execute(request)
    available_candidates = result.unique().scalars().all()

    return available_candidates


async def read_candidate_by_id(
    candidate_id: int, session: Annotated[AsyncSession, Depends(get_session)]
):
    """Поиск кандидата по id"""
    logger.debug(
        f"[yellow]read_candidate_by_id[/] | Поиск кандидата по id({candidate_id})"
    )

    request = (
        select(Candidate)
        .where(Candidate.id == candidate_id)
        .options(joinedload(Candidate.courses).joinedload(CandidateCourse.course))
        .options(joinedload(Candidate.skills).joinedload(CandidateSkill.skill))
    )

    result = await session.execute(request)
    candidate = result.scalars().first()

    if candidate:
        logger.debug("[yellow]read_candidate_by_id[/] | Кандидат найден")
        return candidate
    logger.error("[yellow]read_candidate_by_id[/] | Кандидат не найден")

    return None
