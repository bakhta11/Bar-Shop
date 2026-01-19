# APIRouter logic here

from fastapi import APIRouter, Depends
from sqlmodel import Session
from db.session import get_session
from crud.user import create_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def register(email: str, password: str, session: Session = Depends(get_session)):
    return create_user(session, email, password)
