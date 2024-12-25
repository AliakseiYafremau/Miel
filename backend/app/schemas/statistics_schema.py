from pydantic import BaseModel
from typing import List, Dict


class InvitationStatistics(BaseModel):
    """Модель для динамики приглашений"""

    date: str
    count: int


class CandidatesStatistics(BaseModel):
    """Модель для статистики по кандидатам"""

    total: int
    last_day: int
    last_week: int
    last_month: int
    favorite: int
    invited: int
    hired: int


class CandidatesByAgeStatistics(BaseModel):
    """Модель для распределения кандидатов по возрастным категориям"""

    under_20: int
    between_20_and_30: int
    over_30: int


class CourseStatistics(BaseModel):
    """Модель для статистики по курсам"""

    id: int
    name: str
    candidates: int


class ActivityStatistics(BaseModel):
    """Модель для общей активности"""

    invitation_trend: List[InvitationStatistics]


class OfficeLoadStatistics(BaseModel):
    """Модель для загрузки офиса"""

    name: str
    location: str
    total_candidates: int
    invited_candidates: int
    hired_candidates: int


class OfficeStatistics(BaseModel):
    """Модель для информации об офисе"""

    total: int
    office_load: List[OfficeLoadStatistics]


class ManagerStatistics(BaseModel):
    """Модель для информации о менеджере"""

    full_name: str
    quotas: int
    office: OfficeLoadStatistics


class StatisticsResponse(BaseModel):
    """Модель для основного ответа"""
    total_managers: int
    candidates_statistics: CandidatesStatistics
    managers_statistics: List[ManagerStatistics]
