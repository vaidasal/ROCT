from sqlalchemy.orm import Session

from models import users
import schema

def get_user(db: Session, user_id: int):
    print("##############################")
    print(db)
    print(user_id)
    print(db.query(users.User))
    dd = db.query(users.User).filter(users.User.id == user_id).first()
    return dd


def get_user_by_email(db: Session, email: str):
    return db.query(users.User).filter(users.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(users.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.user.UserCreate):
    hashed_password = user.password
    db_user = users.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

