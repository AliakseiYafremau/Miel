from app.models.models import (
      ManagerCandidate,
)

from fastapi import HTTPException
from starlette import status
from sqlalchemy.future import select

async def like_candidate(current_user_id, session, candidate_id):
    like = await create_favorite(current_user_id, session, candidate_id.id)
    return like

async def dislike_candidate(current_user_id, session, candidate_id):
    dislike = await delete_favorite(current_user_id, session, candidate_id.id)
    return dislike

async def create_favorite(current_user_id, session, candidate_id):
    if not await check_obj_exists(current_user_id, candidate_id, session):
        create_obj_invite = ManagerCandidate(candidate_id=candidate_id, done_by=current_user_id, is_favorite=True)
        session.add(create_obj_invite)
        await session.commit()
        await session.refresh(create_obj_invite)
        return create_obj_invite
    else:
        obj = await get_obj_manager_candidate(current_user_id, candidate_id, session)
        if obj.is_favorite:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="The like was set earlier"
            )
        else:
            obj.is_favorite = True
            await session.commit()
            await session.refresh(obj)
            return obj

async def delete_favorite(current_user_id, session, candidate_id):
    if await check_obj_exists(current_user_id, candidate_id, session):
        obj = await get_obj_manager_candidate(current_user_id, candidate_id, session)
        if not obj.is_favorite:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="This candidate does not have the chosen mark"
            )
        else:
            obj.is_favorite = False
            if obj.is_invited == False and obj.note == None and obj.is_viewed == False:
                await session.delete(obj)
                await session.commit()
                return obj
            else:
                await session.commit()
                await session.refresh(obj)
                return obj
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This candidate does not have the chosen mark"
        )

async def check_obj_exists(current_user_id, candidate_id, session):
    obj = await get_obj_manager_candidate(current_user_id, candidate_id, session)
    return True if not obj == None else False

async def get_obj_manager_candidate(current_user_id, candidate_id, session):
    obj = await session.execute(select(ManagerCandidate)
                                .where((ManagerCandidate.candidate_id == candidate_id)&(ManagerCandidate.done_by == current_user_id)))
    obj = obj.scalar_one_or_none()
    return obj