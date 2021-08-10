from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# URL in Docker #SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://octlab:laser@db:5432/LOCTTool_DB"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://octlab:laser@localhost:5432/LOCTTool_DB"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
        "scope": ["Administrator"],
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Chains",
        "email": "alicechains@example.com",
        "password": "$2b$12$gSvqqUPvlXP2tfVFaWK1Be7DlH.PKZbv5H8KnzzVgXXbVxpva.pFm",
        "disabled": True,
        "scope": ["User"],
    },
}

