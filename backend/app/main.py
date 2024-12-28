import uvicorn
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.db import engine
from app.core.logging import logger
from app.utils.adjusment import register_routers, add_prefix, get_docs_url
from app.utils.admin_panel import add_admin_panel


app = FastAPI(
    docs_url=add_prefix("/docs"),
    openapi_url=get_docs_url(show_docs=True),
    redoc_url=None,
)

# CORS - порты, с которых можно обращаться
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://poopsss-mielfrontreact-9087.twc1.net",
    "http://5.22.217.204",
]

# Добавляем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(add_prefix("/static"), StaticFiles(directory="static"), name="static")

# Подключаем админку
add_admin_panel(app, engine)

# Регистрируем роутеры
register_routers(app)


if __name__ == "__main__":
    logger.info("Запуск сервера...")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
