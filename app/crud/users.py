# CRUD logic here

from sqlmodel import Session, select
from app.models.user import User
from app.core.security import get_password_hash


def create_user(session: Session, email: str, password: str):
    user = User(email=email, hashed_password=get_password_hash(password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user_by_email(session: Session, email: str):
    return session.exec(select(User).where(User.email == email)).first()
