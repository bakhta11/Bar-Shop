#from fastapi import APIRouter, Depends
#from sqlmodel import Session
#from ..db import get_session
#from .. import crud
#from app.schemas.product import Product


#router = APIRouter(prefix='/products')

#@router.post('/', response_model=ProductRead)
#def create_product(p: ProductCreate, session: Session = Depends(get_session)):
#    prod = crud.create_product(session, **p.dict())
#    return prod

#@router.get('/', response_model=list[ProductRead])
#def list_products(session: Session = Depends(get_session)):
#    return crud.list_products(session)

from fastapi import APIRouter
from app.schemas.product import Product, ProductCreate

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=Product)
def create_product(product: ProductCreate):
    return Product(id=1, **product.dict())
