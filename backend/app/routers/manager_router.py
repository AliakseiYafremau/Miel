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
from app.schemas import manager_schema
from app.core.logging import logger
from app.core.config import settings
from app.utils.authentication import get_current_user
from app.schemas.manager_schema import sortBy

# Роутер для руководителя
manager_router = APIRouter(
    prefix="/manager",
    tags=["Работа с руководителем"],
)


@manager_router.get("/", response_model=manager_schema.getManager)
async def get_manager(
    current_user_id: Annotated[int, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    logger.debug(f"{settings.API_PREFIX}/manager/ | Запрос на эндпоинт")

    manager = await read_manager_by_id(current_user_id, session)
    if manager:
        logger.debug(f"{settings.API_PREFIX}/manager/ | Руководитель найден")
        return manager
    logger.error(f"{settings.API_PREFIX}/manager/ | Руководитель найден")
    raise HTTPException(status_code=404, detail="Руководитель не найден")


@manager_router.get(
    "/get_candidates/", response_model=List[manager_schema.getCandidate]
)
async def get_candidates_of_manager(
    current_user_id: Annotated[int, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    logger.debug(f"{settings.API_PREFIX}/get_candidates/ | Запрос на эндпоинт")

    candidates = await read_candidates_by_manager_id(current_user_id, session)
    return candidates


@manager_router.get(
    "/get_available_candidates/", response_model=List[manager_schema.getCandidate]
)
async def get_available_candidates(
    current_user_id: Annotated[int, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
    courses: Annotated[List[int] | None, Query()] = None,
    sort_by: Annotated[str, Query(alias="sortBy")] = sortBy.is_invited,
    min_age: int = None,
    max_age: int = None,
):
    logger.debug(f"{settings.API_PREFIX}/get_available_candidates/ | Запрос на эндпоинт")

    candidates = await read_available_candidates(
        session,
        manager_id=current_user_id,
        min_age=min_age,
        max_age=max_age,
        courses=courses,
        sort_by=sort_by,
    )
    return candidates


@manager_router.get("/get_candidate_by_id/", response_model=manager_schema.getCandidate)
async def get_candidate_by_id(
    current_user_id: Annotated[int, Depends(get_current_user)],
    candidate_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    logger.debug(f"{settings.API_PREFIX}/get_available_candidates/ | Запрос на эндпоинт по id({candidate_id})")

    candidate = await read_candidate_by_id(candidate_id, session)
    if candidate:
        logger.debug("Кандидат найден")
        return candidate
    logger.error("Кандидат не найден")

    raise HTTPException(status_code=404, detail="Кандидат не найден")
