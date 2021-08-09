from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    firstname = Column(String, unique=False)
    lastname = Column(String, unique=False)
    password = Column(String, unique=False, nullable=False)
    created = Column(DateTime, default=func.now())

    def __repr__(self):
        return 'id: {}, email: {}'.format(self.id, self.email)