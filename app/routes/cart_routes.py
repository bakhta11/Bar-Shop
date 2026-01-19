#from fastapi import APIRouter, Depends, HTTPException, Header
#from sqlmodel import Session
#from ..db import get_session
#from .. import crud, auth
#from app.schemas.cart import Cart


#router = APIRouter(prefix='/cart')

#def get_current_user_id(authorization: str = Header(...)):
#    if not authorization.startswith('Bearer '):
#        raise HTTPException(status_code=401, detail='Invalid auth header')
#    token = authorization.split(' ', 1)[1]
#    payload = auth.verify_token(token)
#    if not payload:
#        raise HTTPException(status_code=401, detail='Invalid token')
#    return int(payload.get('sub'))

#@router.post('/add')
#def add_to_cart(item: CartAdd, user_id: int = Depends(get_current_user_id), session: Session = Depends(get_session)):
#    crud.add_to_cart(session, user_id, item.product_id, item.quantity)
#    return {"msg": "added"}

#@router.get('/my')
#def view_cart(user_id: int = Depends(get_current_user_id), session: Session = Depends(get_session)):
#    return crud.get_cart(session, user_id)

from fastapi import APIRouter
from app.schemas.cart import CartAdd

router = APIRouter(prefix="/cart", tags=["Cart"])


@router.post("/")
def add_to_cart(item: CartAdd):
    return {"message": "Added to cart", "item": item}
