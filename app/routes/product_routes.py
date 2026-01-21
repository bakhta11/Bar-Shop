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

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db import get_session
from app.schemas.product import Product, ProductCreate
from app.crud.products import create_product, get_products, get_product, delete_product
from app.dependencies import get_current_admin_user
from app.models.user import User

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=Product)
def create_product_endpoint(
    product_data: ProductCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_admin_user)
):
    """
    Create a new product. Requires admin privileges.
    """
    from app.models.product import Product as ProductModel
    product = ProductModel(**product_data.dict())
    return create_product(session, product)


@router.get("/", response_model=list[Product])
def list_products(session: Session = Depends(get_session)):
    """
    List all products. Available to all users (no authentication required).
    """
    return get_products(session)


@router.get("/{product_id}", response_model=Product)
def get_product_endpoint(
    product_id: int,
    session: Session = Depends(get_session)
):
    """
    Get a specific product by ID. Available to all users (no authentication required).
    """
    product = get_product(session, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/{product_id}")
def delete_product_endpoint(
    product_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_admin_user)
):
    """
    Delete a product. Requires admin privileges.
    """
    product = delete_product(session, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
