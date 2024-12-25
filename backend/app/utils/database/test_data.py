from faker import Faker
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import (
    Admin,
    Manager,
    Candidate,
    Office,
    Course,
    ManagerCandidate,
    CandidateCourse,
)
from app.core.db import AsyncSessionFactory


fake = Faker("ru_RU")


# Создаем сессию вручную
async def get_session() -> AsyncSession:
    return AsyncSessionFactory()


# Основная функция для заполнения базы данных
async def populate_database(
    num_offices: int = 5,
    num_admins: int = 3,
    num_managers: int = 10,
    num_candidates: int = 50,
    num_courses: int = 10,
    max_candidates_per_manager: int = 3,
    max_courses_per_candidate: int = 3,
):
    session = await get_session()  # Получаем сессию вручную
    try:
        # Создаем офисы
        offices = []
        for _ in range(num_offices):
            office = Office(
                name=fake.company(),
                location=fake.city(),
            )
            session.add(office)
            offices.append(office)
        await session.commit()

        # Создаем администраторов
        for _ in range(num_admins):
            admin = Admin(
                email=fake.email(),
                password=fake.password(),
                is_superadmin=fake.boolean(),
            )
            session.add(admin)
        await session.commit()

        # Создаем руководителей
        for _ in range(num_managers):
            manager = Manager(
                email=fake.email(),
                password=fake.password(),
                full_name=fake.name(),
                quotas=fake.random_int(min=1, max=50),
                office_id=fake.random_element([office.id for office in offices]),
            )
            session.add(manager)
        await session.commit()

        # Создаем кандидатов
        candidates = []
        for _ in range(num_candidates):
            candidate = Candidate(
                full_name=fake.name(),
                email=fake.unique.email(),
                phone=fake.unique.phone_number(),
                location=fake.city(),
                photo=fake.file_path(depth=1, category="image"),
                resume=fake.file_path(depth=1, category="text"),
                is_hired=fake.boolean(),
                clients=fake.random_int(min=0, max=20),
                objects=fake.random_int(min=0, max=10),
                date_of_birth=fake.date_between(start_date="-30y", end_date="-18y"),
                years_of_experience=fake.random_int(min=0, max=20),
            )
            session.add(candidate)
            candidates.append(candidate)
        await session.commit()

        # Связываем кандидатов с руководителями (каждого кандидата может назначить несколько менеджеров)
        for candidate in candidates:
            num_managers_for_candidate = fake.random_int(
                min=1, max=max_candidates_per_manager
            )
            for _ in range(num_managers_for_candidate):
                manager_candidate = ManagerCandidate(
                    done_by=fake.random_int(
                        min=1, max=num_managers
                    ),  # Пример связи с руководителем
                    candidate_id=candidate.id,
                    is_viewed=fake.boolean(),
                )
                session.add(manager_candidate)
        await session.commit()

        # Создаем курсы
        courses = []
        for _ in range(num_courses):
            course = Course(
                name=fake.job(),
            )
            session.add(course)
            courses.append(course)
        await session.commit()

        # Связываем кандидатов с курсами (каждого кандидата может пройти несколько курсов)
        for candidate in candidates:
            num_courses_for_candidate = fake.random_int(
                min=1, max=max_courses_per_candidate
            )
            for _ in range(num_courses_for_candidate):
                candidate_course = CandidateCourse(
                    candidate_id=candidate.id,
                    course_id=fake.random_element([course.id for course in courses]),
                )
                session.add(candidate_course)
        await session.commit()

    finally:
        # Явно закрываем сессию
        await session.close()


if __name__ == "__main__":
    asyncio.run(
        populate_database(
            num_offices=3,
            num_admins=2,
            num_managers=5,
            num_candidates=20,
            num_courses=5,
        )
    )
