from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from app.db import get_session
from app import auth
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    """
    Extract and verify JWT token from Authorization header.
    Returns the user ID from the token.
    """
    payload = auth.verify_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail='Invalid or expired token')

    user_id = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=401, detail='Invalid token payload')

    return int(user_id)


def get_current_user(
    user_id: int = Depends(get_current_user_id),
    session: Session = Depends(get_session)
) -> User:
    """
    Get the current authenticated user from the database.
    """
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    if not user.is_active:
        raise HTTPException(status_code=403, detail='User account is inactive')

    return user


def get_current_admin_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Verify that the current user is an admin.
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail='Admin privileges required'
        )

    return current_user
