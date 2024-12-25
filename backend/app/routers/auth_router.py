from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.core.config import settings
from app.core.logging import logger
from app.schemas.auth_schema import TokenSchema
from app.utils.authentication import authenticate_user, create_access_token


auth_router = APIRouter(
    prefix="/auth",
    tags=["Работа с авторизацией"],
)


@auth_router.post("/login/")
async def login(
    email: Annotated[str, Form(...)],
    password: Annotated[str, Form(...)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    logger.debug("Запуск роутера auth/login/ с email: %s", email)

    input_data = {"email": email, "password": password}
    user = await authenticate_user(input_data, session)
    if not user:
        raise HTTPException(status_code=401, detail="Неверная почта или пароль")

    token = create_access_token(
        data={"sub": str(user.email)}, expires_delta=settings.MINUT
    )

    return TokenSchema(access_token=token, token_type="bearer")
