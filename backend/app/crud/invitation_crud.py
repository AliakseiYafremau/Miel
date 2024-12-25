from app.crud.manager_crud import read_manager_by_id
from app.models.models import (
    ManagerCandidate,
)
from app.crud.favorite_crud import check_obj_exists, get_obj_manager_candidate
from fastapi import HTTPException
from starlette import status


async def invite_candidate(current_user_id, session, candidate_id):
    if await check_quotas(current_user_id, session):
        invitation = await create_invitation(current_user_id, session, candidate_id.id)
        return invitation
    else:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="Not enough quotas to send invites",
        )


async def check_quotas(current_user_id, session):
    manager = await read_manager_by_id(current_user_id, session)
    if manager.quotas > 0:
        return True


async def create_invitation(current_user_id, session, candidate_id):
    manager = await read_manager_by_id(current_user_id, session)
    if not await check_obj_exists(current_user_id, candidate_id, session):
        create_obj_invite = ManagerCandidate(candidate_id=candidate_id, done_by=current_user_id, is_invited=True)
        manager.quotas = manager.quotas - 1
        session.add(create_obj_invite)
        await session.commit()
        await session.refresh(create_obj_invite)
        await session.refresh(manager)
        return create_obj_invite
    else:
        obj = await get_obj_manager_candidate(current_user_id, candidate_id, session)
        if obj.is_invited:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="The candidate was invited earlier by this user"
            )
        else:
            obj.is_invited = True
            manager.quotas = manager.quotas - 1
            await session.commit()
            await session.refresh(manager)
            await session.refresh(obj)
            return obj
