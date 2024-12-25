from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.crud.invitation_crud import invite_candidate
from app.crud.favorite_crud import (
    like_candidate, dislike_candidate
)
from app.crud.notes_crud import put_note_from_manager, delete_note_from_manager

from app.utils.authentication import get_current_user
from app.schemas.manager_schema import inviteCandidate, NotesManager


candidate_router = APIRouter(
    prefix="/candidate",
    tags=["Работа с руководителем"],
)


@candidate_router.post("/invite_candidate/")
async def invite_candidate_of_manager(
    current_user_id: Annotated[int, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
    candidate: inviteCandidate,
):
    invitation = await invite_candidate(current_user_id, session, candidate)
    return invitation


@candidate_router.post("/like_candidate")
async def like_candidate_from_manager(
    current_user_id: Annotated[int, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
    candidate: inviteCandidate
):
    like = await like_candidate(current_user_id, session, candidate)
    return like

@candidate_router.post("/dislike_candidate")
async def like_candidate_from_manager(
    current_user_id: Annotated[int, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
    candidate: inviteCandidate
):
    dislike = await dislike_candidate(current_user_id, session, candidate)
    return dislike


@candidate_router.post('/put_note')
async def put_note(current_user_id: Annotated[int, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
    candidate: NotesManager):

    note = await put_note_from_manager(current_user_id, session, candidate)
    return note

@candidate_router.post('/delete_note')
async def put_note(current_user_id: Annotated[int, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
    candidate: inviteCandidate):

    note = await delete_note_from_manager(current_user_id, session, candidate)
    return note
