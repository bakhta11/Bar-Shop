# APIRouter logic here

from fastapi import APIRouter, Depends
from sqlmodel import Session
from db.session import get_session
from crud.cart import add_to_cart, get_cart

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/")
def add(user_id: int, product_id: int, quantity: int = 1, session: Session = Depends(get_session)):
    return add_to_cart(session, user_id, product_id, quantity)

@router.get("/{user_id}")
def view(user_id: int, session: Session = Depends(get_session)):
    return get_cart(session, user_id)
