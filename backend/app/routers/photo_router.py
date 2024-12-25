
from fastapi import APIRouter



photo_router = APIRouter(prefix="/upload", tags=["Работа с изображениями"])

# @photo_router.post("/upload/")
# async def upload(
#    photo: UploadFile = File(...),
# ) -> Annotated:
#    logger.debug("Запуск роутера загрузка фото" )
#
#
#    if not photo:
#        raise HTTPException(status_code=401, detail="Неверная почта или пароль")
#
#    return
