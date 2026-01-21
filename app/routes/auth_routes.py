from fastapi import APIRouter, Depends, HTTPException, Form
from sqlmodel import Session
from app.db import get_session
from app.crud.users import get_user_by_email, create_user
from app import auth, models
from app.schemas.user import (
    UserCreate,
    Token,
    PasswordResetRequest,
    PasswordResetConfirm,
)
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=Token)
def register(user_in: UserCreate, session: Session = Depends(get_session)):
    existing = get_user_by_email(session, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = create_user(session, user_in.email, user_in.password)
    token = auth.create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
def login(
    username: str = Form(...),
    password: str = Form(...),
    session: Session = Depends(get_session)
):
    user = get_user_by_email(session, username)
    if not user or not auth.verify_password(
        password, user.hashed_password
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


reset_tokens = {}


@router.post("/password-reset/request")
def password_reset_request(
    req: PasswordResetRequest, session: Session = Depends(get_session)
):
    user = get_user_by_email(session, req.email)
    if not user:
        return {"msg": "If account exists, reset token generated."}
    token = auth.create_access_token(
        {"sub": str(user.id)}, expires_delta=timedelta(minutes=30)
    )
    reset_tokens[token] = user.id
    return {"reset_token": token}


@router.post("/password-reset/confirm")
def password_reset_confirm(
    data: PasswordResetConfirm, session: Session = Depends(get_session)
):
    payload = auth.verify_token(data.token)
    if not payload:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
    user_id = int(payload.get("sub"))
    user = session.get(models.User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.hashed_password = auth.get_password_hash(data.new_password)
    session.add(user)
    session.commit()
    return {"msg": "Password updated"}
