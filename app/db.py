from sqlmodel import SQLModel, create_engine, Session
import os

# Correct DB URL for Docker
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:nikolozi12@barshop_db:5432/barshop"
)

engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
