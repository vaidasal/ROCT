from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    firstname = Column(String)
    lastname = Column(String)
    password = Column(String, nullable=False)
    scope = Column(String)
    created = Column(DateTime, default=func.now())
    octcsvs = relationship("OctCSV", backref="user", lazy=True)

    def __repr__(self):
        return 'id: {}, email: {}'.format(self.id, self.email)

class OctCSV(Base):
    __tablename__ = 'octcsv'
    id = Column(Integer, primary_key=True)
    status = Column(String)
    seamid = Column(Integer, nullable=False)
    linenumber = Column(String)
    type = Column(String)
    filename = Column(String)
    datetime = Column(DateTime)
    userid = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))

    def __repr__(self):
        return 'seamID: {}, lineNumber: {}'.formatpostgre(self.id, self.linenumber)

class CsvData(Base):
    __tablename__ = 'csvdata'
    id = Column(Integer, primary_key=True)
    octcsv_id = Column(Integer, ForeignKey("octcsv.id"))
    octcsv = relationship("OctCSV", backref=backref("csvdata", uselist=False, passive_deletes=True))
    data = Column(JSONB)

    def __repr__(self):
        return 'octcsv_id: {}'.formatpostgre(self.octcsv_id)

