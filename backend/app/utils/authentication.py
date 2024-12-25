from typing import Annotated, Dict
from datetime import datetime, timedelta, timezone

from fastapi.security import (
    APIKeyHeader,
)
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from jwt import PyJWTError
import jwt

from app.core.config import settings
from app.core.db import get_session
from app.crud.auth_crud import read_user_by_email


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
header_scheme = APIKeyHeader(name="Authorization", auto_error=False)


def verify_password(password: str, hashed_password: str) -> bool:
    """Проверка пароля"""
    # return pwd_context.verify(password, hashed_password) TODO Расскомментировать после реализации хеширования пароля в админ панели
    return password == hashed_password


def get_password_hash(password: str):
    """Хеширование пароля"""
    # return pwd_context.hash(password) TODO Расскомментировать после реализации хеширования пароля в админ панели
    return password


def create_access_token(data: dict, expires_delta: int) -> str:
    """Создание токена"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.MINUT)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(
    user_data: Dict[str, str], session: AsyncSession = Depends(get_session)
):
    """Проврека входных данных"""
    user = await read_user_by_email(user_data["email"], session)
    if not user:
        return False
    if not verify_password(user_data["password"], user.password):
        return False
    return user


async def get_current_user(
    token: Annotated[str, Depends(header_scheme)],
    session: AsyncSession = Depends(get_session),
):
    """Получение текущего пользователя"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        user_email = payload.get("sub")
        if user_email is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception

    user = await read_user_by_email(user_email, session)
    if not user:
        raise credentials_exception
    return user.id
