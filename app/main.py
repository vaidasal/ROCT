from datetime import timedelta
from typing import List, Any
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from fastapi import Depends, FastAPI, HTTPException, Body
from fastapi.security import (OAuth2PasswordRequestForm)
from fastapi.encoders import jsonable_encoder


from dependencies import authenticate_user, get_db, get_current_user, is_valid_user, is_valid_admin
from config import settings
from db import crud
from security import create_access_token
from schema.token import Token
from schema.user import User, UserUpdate
import models

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost/docs",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


@app.post("/login")
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.email, "scopes": user.scope},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer", "scope": user.scope}


@app.get("/me", response_model=User, dependencies=[Depends(is_valid_admin)])
def read_user_me(current_user: User = Depends(get_current_user)) -> Any:
    """
    Get current user.
    """
    return current_user

@app.put("/me", response_model=User, dependencies=[Depends(is_valid_user)])
def update_user_me(
    *,
    db: Session = Depends(get_db),
    new_password: str = Body(None),
    firstname: str = Body(None),
    lastname: str = Body(None),
    email: EmailStr = Body(None),
    current_user: User = Depends(get_current_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    print(current_user_data)
    user_in = UserUpdate(**current_user_data)
    print(user_in)
    if new_password is not None:
        user_in.password = new_password
    if firstname is not None:
        user_in.firstname = firstname
    if lastname is not None:
        user_in.lastname = lastname
    if email is not None:
        db_user = crud.get_user_by_email(email=email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        else:
            user_in.email = email

    user = crud.update_user(db, db_obj=current_user, obj_in=user_in)
    return user

@app.post("/users/", response_model=User, dependencies=[Depends(is_valid_user)])
def create_user(user: UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[User], dependencies=[Depends(is_valid_user)])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=User, dependencies=[Depends(is_valid_user)])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/open", response_model=User, dependencies=[Depends(is_valid_user)])
def create_user_open(user_in: UserUpdate, db: Session = Depends(get_db)) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud.get_user_by_email(email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )

    user = crud.create_user(db, user=user_in)
    return user

@app.delete("/{id}", response_model=User, dependencies=[Depends(is_valid_user)])
def delete_item(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
    Delete an item.
    """
    user = crud.get_user(db=db, user_id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    removed_user = crud.remove(db=db, type=models.users.User, id=id)
    return removed_user