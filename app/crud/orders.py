# CRUD logic here

from sqlmodel import Session
from app.models.order import Order


def create_order(session: Session, user_id: int, total_price: float):
    order = Order(user_id=user_id, total_price=total_price)
    session.add(order)
    session.commit()
    session.refresh(order)
    return order
