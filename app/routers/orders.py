# APIRouter logic here

from fastapi import APIRouter, Depends
from sqlmodel import Session
from db.session import get_session
from crud.order import create_order

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
def create(user_id: int, total_price: float, session: Session = Depends(get_session)):
    return create_order(session, user_id, total_price)
