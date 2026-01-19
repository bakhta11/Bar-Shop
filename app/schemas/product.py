from sqlmodel import SQLModel, Field


class ProductBase(SQLModel):
    name: str
    price: float


class ProductCreate(ProductBase):
    pass


class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
