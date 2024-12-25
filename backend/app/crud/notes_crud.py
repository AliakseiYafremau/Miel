from app.models.models import (
      ManagerCandidate,
)
from sqlalchemy.future import select
from fastapi import HTTPException
from starlette import status

async def put_note_from_manager(current_user_id, session, candidate):
    note = await create_notes(current_user_id, session, candidate)
    return note


async def create_notes(current_user_id, session, candidate):
    if not await check_obj_exists(current_user_id, candidate, session):
        create_obj = ManagerCandidate(candidate_id=candidate.id, done_by=current_user_id, note=candidate.note)
        session.add(create_obj)
        await session.commit()
        await session.refresh(create_obj)
        return create_obj
    else:
        obj = await get_obj_manager_candidate(current_user_id, candidate, session)
        obj.note = candidate.note
        await session.commit()
        await session.refresh(obj)
        return obj


async def check_obj_exists(current_user_id, candidate, session):
    obj = await get_obj_manager_candidate(current_user_id, candidate, session)
    return True if not obj == None else False

async def get_obj_manager_candidate(current_user_id, candidate, session):
    obj = await session.execute(select(ManagerCandidate)
                                .where((ManagerCandidate.candidate_id == candidate.id)&(ManagerCandidate.done_by == current_user_id)))
    obj = obj.scalar_one_or_none()
    return obj


async def delete_note_from_manager(current_user_id, session, candidate):
    note = await delete_notes(current_user_id, session, candidate)
    return note


async def delete_notes(current_user_id, session, candidate):
    if await check_obj_exists(current_user_id, candidate, session):
        obj = await get_obj_manager_candidate(current_user_id, candidate, session)
        if obj.note:
            obj.note = None
            if obj.is_invited == False and obj.is_favorite == False and obj.is_viewed == False:
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
                detail="This candidate has no notes"
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This candidate has no notes"
        )