from fastapi.security import SecurityScopes, OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status, Security
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session
from typing import Optional

from security import TokenData, verify_password
from schema.user import User
from db.database import SessionLocal
from db import crud
from config import settings



oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={"admin": "Full Access", "user": "Limited Access"},
)

async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", "")
        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception
    user = crud.get_user_by_email(email=token_data.username)
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user


async def is_valid_user(current_user: User = Security(get_current_user, scopes="user")):
    return current_user

async def is_valid_admin(current_user: User = Security(get_current_user, scopes="admin")):
    return current_user

def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    user = crud.get_user_by_email(email=email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



