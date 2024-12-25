from fastapi.params import Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.models.models import Course
from app.utils.database.test_data import get_session


async def read_course_by_id(
    course_id: int, session: AsyncSession = Depends(get_session)
):
    """Получение курса по id"""
    course = await session.get(Course, course_id)
    if course:
        return course
    return None


async def read_courses_count(session: AsyncSession = Depends(get_session)):
    """Получение количества курсов"""
    request = select(Course.id)
    result = await session.execute(request)
    courses_count = result.scalars().all()
    return courses_count
