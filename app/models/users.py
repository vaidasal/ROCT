from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    firstname = Column(String)
    lastname = Column(String)
    password = Column(String, nullable=False)
    scope = Column(JSON)
    created = Column(DateTime, default=func.now())

    def __repr__(self):
        return 'id: {}, email: {}'.format(self.id, self.email)