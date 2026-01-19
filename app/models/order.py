# SQLModel models here

from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    total_price: float
    status: str = "pending"
    created_at: datetime = Field(default_factory=datetime.utcnow)
