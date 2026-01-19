# SQLModel models here

from sqlmodel import SQLModel, Field
from typing import Optional

class Cart(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    product_id: int = Field(index=True)
    quantity: int = 1
