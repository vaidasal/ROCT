from pydantic import BaseSettings, PostgresDsn, validator
from typing import Optional, Dict, Any

class Settings(BaseSettings):

    ALGORITHM = "HS256"
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    USERS_OPEN_REGISTRATION = True


settings = Settings()