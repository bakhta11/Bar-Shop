# cart schemas
#from pydantic import BaseModel


#class CartCreate(BaseModel):
#    product_id: int
#    quantity: int


#class CartRead(CartCreate):
#    id: int

#    class Config:
#        from_attributes = True

from sqlmodel import SQLModel, Field


class CartAdd(SQLModel):
    product_id: int
    quantity: int


class Cart(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    product_id: int
    quantity: int
