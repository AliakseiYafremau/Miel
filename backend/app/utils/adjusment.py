from app.core.config import settings

from app.routers.photo_router import photo_router
from app.routers.manager_router import manager_router
from app.routers.auth_router import auth_router
from app.routers.invitation_router import candidate_router
from app.routers.statistics_router import statistics_router


def add_prefix(url: str, api_prefix: str = settings.API_PREFIX):
    if api_prefix:
        return api_prefix + url
    return url


def register_routers(app, api_prefix: str = settings.API_PREFIX):
    app.include_router(manager_router, prefix=api_prefix)
    app.include_router(auth_router, prefix=api_prefix)
    app.include_router(candidate_router, prefix=api_prefix)
    app.include_router(photo_router, prefix=api_prefix)
    app.include_router(statistics_router, prefix=api_prefix)


def get_docs_url(show_docs: bool = settings.SHOW_DOCS):
    if show_docs:
        return add_prefix("/openapi.json")
    return None
