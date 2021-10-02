from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import cast, Date
from typing import Any, Dict, Union, TypeVar, Optional
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

from models import models
from schema import user
import security
from db.base_class import Base
from db.database import engine
from octcsvreader import OctCsvReader


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(email: str) -> Optional[user.UserUpdate]:
    Session = sessionmaker(engine)
    session = Session()
    try:
        return session.query(models.User).filter(models.User.email == email).first()
    finally:
        session.close()

def get_user_by_id(id: int) -> Optional[user.UserUpdate]:
    Session = sessionmaker(engine)
    session = Session()
    try:
        return session.query(models.User).filter(models.User.id == id).first()
    finally:
        session.close()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_octcsv(db: Session, skip: int = 0, limit: int = 100):
    data = db.query(models.OctCSV).offset(skip).limit(limit).all()
    return data


def create_user(db: Session, user: user.UserUpdate):
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(
        email=user.email, password=hashed_password,
        firstname=user.firstname, lastname=user.lastname, scope=user.scope
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, *, db_obj: user, obj_in: Union[user.UserUpdate, Dict[str, Any]]
) -> user.User:
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    print(update_data)
    if "password" in update_data:
        hashed_password = security.get_password_hash(update_data["password"])
        del update_data["password"]
        update_data["password"] = hashed_password
    return update(db, db_obj=db_obj, obj_in=update_data)


def update(
        db: Session,
        *,
        db_obj: TypeVar("ModelType", bound=Base),
        obj_in: Union[TypeVar("UpdateSchemaType", bound=BaseModel), Dict[str, Any]]
) -> TypeVar("ModelType", bound=Base):
    obj_data = jsonable_encoder(db_obj)
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_a_db():
    session = sessionmaker(engine)
    try:
        yield session.begin()
    finally:
        session.close()

def remove(db: Session, type: TypeVar("ModelType", bound=Base),  *, id: int) -> TypeVar("ModelType", bound=Base):
    obj = db.query(type).get(id)
    db.delete(obj)
    db.commit()
    return obj

def createEntry(
        db: Session,
        new_obj: TypeVar("ModelType", bound=Base)
) -> TypeVar("ModelType", bound=Base):
    db.add(new_obj)
    db.commit()
    db.refresh(new_obj)
    return new_obj.id

def readLocalData(table, path, point):
    reader = OctCsvReader()
    fileDetail = reader.getCSVNameDetailFromFile(path)
    dataJson = reader.readCSVTables(path, fileDetail)
    if point:
        df = reader.getPointDataFrame(dataJson, table)
    else:
        df = reader.getDataFrame(dataJson, table)
    return df
