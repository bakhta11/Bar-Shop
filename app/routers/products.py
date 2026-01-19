# APIRouter logic here

from fastapi import APIRouter, Depends
from sqlmodel import Session
from db.session import get_session
from crud.product import create_product, get_products
from models.product import Product

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/")
def create(product: Product, session: Session = Depends(get_session)):
    return create_product(session, product)

@router.get("/")
def list_products(session: Session = Depends(get_session)):
    return get_products(session)
