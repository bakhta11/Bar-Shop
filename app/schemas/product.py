from sqlmodel import SQLModel, Field
from typing import Optional


class ProductBase(SQLModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int = 0
    image_url: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
