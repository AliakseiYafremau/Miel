from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.crud.manager_crud import (
    read_manager_by_id,
    read_available_candidates,
    read_candidates_by_manager_id,
    read_candidate_by_id,
)
from app.core.logging import logger
from app.utils.authentication import get_current_user
from app.schemas.manager_schema import sortBy

# Роутер для руководителя
manager_router = APIRouter(
    prefix="/manager",
    tags=["Работа с руководителем"],
)


@manager_router.get("/")
async def get_manager(
    current_user_id: Annotated[int, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    logger.debug("Запуск роутера /manager/")

    manager = await read_manager_by_id(current_user_id, session)
    if manager:
        logger.debug("Руководитель найден")
        return manager
    logger.error("Руководитель не найден")
    raise HTTPException(status_code=404, detail="Руководитель не найден")


@manager_router.get("/get_candidates/")
async def get_candidates_of_manager(
    current_user_id: Annotated[int, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    logger.debug("Запуск роутера manager/get_candidates/")

    candidates = await read_candidates_by_manager_id(current_user_id, session)
    return candidates


@manager_router.get("/get_available_candidates/")
async def get_available_candidates(
    current_user_id: Annotated[int, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
    courses: Annotated[List[int] | None, Query()] = None,
    sort_by: Annotated[str, Query(alias="sortBy")] = sortBy.is_invited,
    min_age: int = None,
    max_age: int = None,
):
    logger.debug("Запуск роутера manager/get_available_candidates/")

    candidates = await read_available_candidates(
        session,
        manager_id=current_user_id,
        min_age=min_age,
        max_age=max_age,
        courses=courses,
        sort_by=sort_by,
    )
    return candidates


@manager_router.get("/get_candidate_by_id/")
async def get_candidate_by_id(
    current_user_id: Annotated[int, Depends(get_current_user)],
    candidate_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    logger.debug("Запуск роутера manager/get_candidate_by_id/ с id: %s", candidate_id)

    candidate = await read_candidate_by_id(candidate_id, session)
    if candidate:
        logger.debug("Кандидат найден")
        return candidate
    logger.error("Кандидат не найден")

    raise HTTPException(status_code=404, detail="Кандидат не найден")
