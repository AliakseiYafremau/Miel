from datetime import date
from typing import List
from enum import Enum

from pydantic import BaseModel


class getOffice(BaseModel):
    """Модель для сериализации офиса"""

    id: int
    name: str
    location: str

    # created_at: datetime
    # updated_at: datetime

    class ConfigDict:
        from_attributes = True


class getCourse(BaseModel):
    """Модель для сериализации курса"""

    id: int
    name: str

    # created_at: datetime
    # updated_at: datetime

    class ConfigDict:
        from_attributes = True


class getSkill(BaseModel):
    """Модель для сериализации навыка"""

    id: int
    name: str

    # created_at: datetime
    # updated_at: datetime

    class ConfigDict:
        from_attributes = True


class getCoursesOfCandidate(BaseModel):
    """Модель для сериализации курсов кандидата"""

    id: int
    course: getCourse

    # created_at: datetime
    # updated_at: datetime

    class ConfigDict:
        from_attributes = True


class getSkillsOfCandidate(BaseModel):
    """Модель для сериализации навыков кандидата"""

    id: int
    skill: getSkill
    # created_at: datetime
    # updated_at: datetime

    class ConfigDict:
        from_attributes = True


class getCandidate(BaseModel):
    """Модель для сериализации кандидата"""

    id: int
    email: str
    full_name: str = ""
    phone: str
    date_of_birth: date
    photo: str = "1.jpg"
    location: str
    resume: str | None
    years_of_experience: int
    clients: int
    objects: int
    is_hired: bool

    # updated_at: datetime
    # created_at: datetime

    courses: List[getCoursesOfCandidate] = []
    skills: List[getSkillsOfCandidate] = []

    class ConfigDict:
        from_attributes = True


class getCandidatesOfManager(BaseModel):
    """Модель для сериализации кандидатов руководителя"""

    id: int
    is_invited: bool
    is_viewed: bool
    is_favorite: bool
    note: str | None

    # created_at: datetime
    # updated_at: datetime

    candidate: getCandidate

    class ConfigDict:
        from_attributes = True


class getManager(BaseModel):
    """Модель для сериализации руководителя"""

    id: int
    full_name: str
    quotas: int
    email: str
    photo: str | None = "1.jpg" #TODO Сделать так, чтоб по умолчанию бралась дефолтная картинка
    office_id: int
    password: str

    # created_at: datetime
    # updated_at: datetime

    office: getOffice
    candidates: List[getCandidatesOfManager] = []

    class ConfigDict:
        from_attributes = True


class sortBy(str, Enum):
    is_invited = "is_invited"
    is_free = "is_free"


class inviteCandidate(BaseModel):
    id: int


class NotesManager(BaseModel):
    id: int
    note: str
