from os.path import join

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date,
    DateTime,
    func,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.core.db import Base
from app.utils.file_upload import storageI


# Абстрактная модель
class BaseModel(Base):
    __abstract__ = True  # Не создаст таблицу в БД, так как это абстрактная модель

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )


# Абстрактная модель пользователя
class BaseUser(BaseModel):
    __abstract__ = True  # Не создаст таблицу в БД, так как это абстрактная модель

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    photo = Column(String(255))  # Путь к фото


# Администратор
class Admin(BaseUser):
    __tablename__ = "admins"

    is_superadmin = Column(Boolean, default=False)


# Руководитель
class Manager(BaseUser):
    __tablename__ = "managers"

    full_name = Column(String(100))
    quotas = Column(Integer, index=True)
    office_id = Column(Integer, ForeignKey("offices.id"))

    candidates = relationship("ManagerCandidate", back_populates="manager")
    office = relationship("Office", back_populates="managers")

    @property
    def photo_url(self):
        return f"/static/photo/{self.photo}" if self.photo else None

    def __repr__(self) -> str:
        return f"{self.full_name}"


# Кандидат
class Candidate(BaseModel):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True)
    photo = Column(String(255))  # Путь к фото
    full_name = Column(String(100))
    email = Column(String(100), unique=True)
    date_of_birth = Column(Date)
    location = Column(String(100))
    resume = Column(String(255))  # Путь к резюме
    phone = Column(String(100), unique=True)
    years_of_experience = Column(Integer, default=0)
    is_hired = Column(Boolean, default=False, index=True)
    clients = Column(Integer, default=0)
    objects = Column(Integer, default=0)

    managers = relationship("ManagerCandidate", back_populates="candidate")
    courses = relationship("CandidateCourse", back_populates="candidate")
    skills = relationship("CandidateSkill", back_populates="candidate")

    @property
    def full_photo_path(self):
        return join(storageI, self.photo)

    def __repr__(self) -> str:
        return f"{self.full_name}"


# Офис
class Office(BaseModel):
    __tablename__ = "offices"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    location = Column(String(100))

    managers = relationship("Manager", back_populates="office")

    def __repr__(self) -> str:
        return f"{self.name}"


# Связь между руководителем и кандидатом
class ManagerCandidate(BaseModel):
    __tablename__ = "manager_candidates"

    id = Column(Integer, primary_key=True)
    done_by = Column(Integer, ForeignKey("managers.id"), index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), index=True)
    is_invited = Column(Boolean, default=False, index=True)
    is_viewed = Column(Boolean, default=False, index=True)
    is_favorite = Column(Boolean, default=False, index=True)
    note = Column(String(255))

    manager = relationship("Manager", back_populates="candidates")
    candidate = relationship("Candidate", back_populates="managers", lazy="joined")

    def __repr__(self) -> str:
        return f"{self.candidate.full_name}"


# Курсы кандидата
class CandidateCourse(BaseModel):
    __tablename__ = "candidate_courses"

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), index=True)

    candidate = relationship("Candidate", back_populates="courses", lazy="joined")
    course = relationship("Course", back_populates="candidates", lazy="joined")

    def __repr__(self) -> str:
        return f"{self.course.name}"


# Курсы
class Course(BaseModel):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    candidates = relationship("CandidateCourse", back_populates="course", lazy="joined")

    def __repr__(self) -> str:
        return f"{self.name}"


# Навыки кандидата
class CandidateSkill(BaseModel):
    __tablename__ = "candidate_skills"

    id = Column(Integer, primary_key=True)
    skill_id = Column(Integer, ForeignKey("skills.id"), index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), index=True)

    candidate = relationship("Candidate", back_populates="skills", lazy="joined")
    skill = relationship("Skill", back_populates="candidates", lazy="joined")

    def __repr__(self) -> str:
        return f"{self.candidate.full_name}/{self.skill.name}"


# Навыки
class Skill(BaseModel):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    candidates = relationship("CandidateSkill", back_populates="skill")

    def __repr__(self) -> str:
        return f"{self.name}"
