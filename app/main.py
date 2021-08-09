#python-multipart OAuth2 form data
#python-jose[cryptography]
#passlib[bcrypt]
#psycopg2 (pstgresql)

from datetime import timedelta

from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import (OAuth2PasswordRequestForm)

from models.user import User
from dependencies import authenticate_user, get_current_active_user, get_current_user
from config import settings
from db.session import fake_users_db
from security import create_access_token
from schema.token import Token


app = FastAPI()


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    # get scopes: form_data.scopes
    access_token = create_access_token(
        data={"sub": user.username, "scopes": user.scope},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Security(get_current_active_user, scopes=["Administrator"])):
    return [{"item_id": "Foo", "owner": current_user.username}]


@app.get("/status/")
async def read_system_status(current_user: User = Depends(get_current_user)):
    return {"status": "ok"}