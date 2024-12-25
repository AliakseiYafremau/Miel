from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.db import get_session
from app.models.models import Manager


""" # Создание пользователя не используем!!!
def create_user(db: Session, name: str, email: str, age: int):
    new_user = BaseUser(name=name, email=email, age=age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/users/")
def create_user(name: str, email: str, age: int, db: AsyncSession = Depends(get_session)):
    return create_user(db, name, email, age)
"""


async def read_user_by_email(
    email: str, session: Annotated[AsyncSession, Depends(get_session)]
):
    """Поиск пользователя по email"""
    result = await session.execute(select(Manager).filter(Manager.email == email))
    user = result.scalars().first()
    if user:
        return user
    return None
