from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.crud.statistics.candidate_crud import read_candidates_statistics
from app.crud.statistics.course_crud import read_courses_count
from app.crud.statistics.manager_crud import read_managers_statistics, read_manager_statistics_by_id
from app.crud.statistics.office_crud import read_office_load, read_all_offices_load, read_all_offices_count

from app.schemas.statistics_schema import OfficeStatistics, ManagerStatistics, OfficeLoadStatistics, StatisticsResponse
from app.schemas.statistics_schema import CandidatesStatistics
from app.utils.database.test_data import get_session

statistics_router = APIRouter(prefix="/statistics", tags=["Работа со статистикой"])


@statistics_router.get("/manager/{manager_id}", response_model=ManagerStatistics)
async def get_manager_stat_by_id(manager_id: int, session: AsyncSession = Depends(get_session)):
    """Получить статистику руководителя по id"""
    manager_stat = await read_manager_statistics_by_id(manager_id, session)
    return ManagerStatistics(**manager_stat)


@statistics_router.get("/managers", response_model=StatisticsResponse)
async def get_managers_statistics(session: AsyncSession = Depends(get_session)):
    """Получить общую статистику по руководителям"""
    managers_stat = await read_managers_statistics(session)
    return StatisticsResponse(**managers_stat)


@statistics_router.get("/candidates", response_model=CandidatesStatistics)
async def get_candidates_statistics(session: AsyncSession = Depends(get_session)):
    """Получить общую статистику по кандидатам."""
    candidate_statistics = await read_candidates_statistics(session)
    return CandidatesStatistics(**candidate_statistics)


@statistics_router.get("/offices", response_model=OfficeStatistics)
async def get_offices_statistics(session: AsyncSession = Depends(get_session)):
    """Получить общую статистику по офисам"""
    all_offices_count = await read_all_offices_count(session)
    all_offices = await read_all_offices_load(session)
    statistics = {
        'total': all_offices_count,
        'office_load': all_offices,
    }
    return OfficeStatistics(**statistics)

@statistics_router.get("/office/{office_id}", response_model=OfficeLoadStatistics)
async def get_office_stat_by_id(office_id: int, session: AsyncSession = Depends(get_session)):
    """Получить статистику офиса по id"""
    office_stat = await read_office_load(office_id, session)
    return OfficeLoadStatistics(**office_stat)


@statistics_router.get("/courses")
async def get_course_statistics(session: AsyncSession = Depends(get_session)):
    """Получение статистики по курсам с кандидатами"""
    courses = await read_courses_count(session)
    return courses
