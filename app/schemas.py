from pydantic import BaseModel, EmailStr , Field
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str = Field(..., min_length=6, max_length=72)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ProductCreate(BaseModel):
    name: str
    quantity: int
    price_lari: float
    description: Optional[str] = None
    category_id: Optional[int]
    material_id: Optional[int]

class ProductRead(ProductCreate):
    id: int

class CartAdd(BaseModel):
    product_id: int
    quantity: int = 1

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordResetConfirm(BaseModel):
    token: str
    new_password: str
