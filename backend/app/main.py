import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.core.db import engine
from app.core.logging import logger
from app.utils.admin_panel import (
    AdminAuth,
    ManagerAdmin,
    OfficeAdmin,
    CandidateAdmin,
    CourseAdmin,
    CandidateCourseAdmin,
    ManagerCandidateAdmin,
    CandidateSkillAdmin,
    SkillAdmin,
)
from app.utils.routers import register_routers

app = FastAPI(debug=True)

# CORS - порты, с которых можно обращаться
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://poopsss-mielfrontreact-9087.twc1.net",
]

# Добавляем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключаем админку
authentication_backend = AdminAuth(secret_key="...")
admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)

admin.add_view(ManagerAdmin)
admin.add_view(OfficeAdmin)
admin.add_view(CandidateAdmin)
admin.add_view(CourseAdmin)
admin.add_view(CandidateCourseAdmin)
admin.add_view(ManagerCandidateAdmin)
admin.add_view(CandidateSkillAdmin)
admin.add_view(SkillAdmin)

# Регистрируем роутеры
register_routers(app)


# Перенаправляем на документацию
@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    logger.info("Запуск сервера...")
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)
