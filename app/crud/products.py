# CRUD logic here

from sqlmodel import Session, select
from app.models.product import Product


def create_product(session: Session, product: Product):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

def get_products(session: Session):
    return session.exec(select(Product)).all()

def get_product(session: Session, product_id: int):
    return session.get(Product, product_id)

def delete_product(session: Session, product_id: int):
    product = session.get(Product, product_id)
    if product:
        session.delete(product)
        session.commit()
    return product
