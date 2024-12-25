from datetime import datetime
from typing import List
from enum import Enum

from pydantic import BaseModel


class getOffice(BaseModel):
    """Модель для сериализации офиса"""

    id: int
    name: str
    location: str

    class Config:
        from_attributes = True


class getSkill(BaseModel):
    """Модель для сериализации навыка"""

    id: int
    name: str

    class Config:
        from_attributes = True


class getManager(BaseModel):
    """Модель для сериализации руководителя"""

    id: int
    email: str
    full_name: str
    quotas: int
    office: getOffice
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class getCandidate(BaseModel):
    """Модель для сериализации кандидата"""

    id: int
    photo: str
    full_name: str
    email: str
    location: str
    resume: str
    phone: str
    is_hired: bool
    clients: int
    objects: int
    skills: List[getSkill] | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class sortBy(str, Enum):
    is_invited = "is_invited"
    is_free = "is_free"


class inviteCandidate(BaseModel):

    id: int

class NotesManager(BaseModel):

    id: int
    note: str
