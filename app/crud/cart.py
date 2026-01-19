# CRUD logic here

from sqlmodel import Session, select
from app.models.cart import Cart


def add_to_cart(session: Session, user_id: int, product_id: int, quantity: int = 1):
    cart_item = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
    session.add(cart_item)
    session.commit()
    session.refresh(cart_item)
    return cart_item

def get_cart(session: Session, user_id: int):
    return session.exec(select(Cart).where(Cart.user_id == user_id)).all()
