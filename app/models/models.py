from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey, Float
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
    laserpar = relationship("LaserPar", backref="user", lazy=True)
    octpar = relationship("OCTPar", backref="user", lazy=True)

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
    grouporder = Column(Integer)
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

class LaserPar(Base):
    __tablename__ = 'laserpar'
    id = Column(Integer, primary_key=True)
    octcsv_id = Column(Integer, ForeignKey("octcsv.id"))
    userid = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    seam_id = Column(Integer)
    octcsv = relationship("OctCSV", backref=backref("laserpar", uselist=False, passive_deletes=True))
    seam_length = Column(Float)
    speed = Column(Float)
    step_size_oct_tester = Column(Float)

    def __repr__(self):
        return 'octcsv_id: {}'.formatpostgre(self.octcsv_id)


class OCTPar(Base):
    __tablename__ = 'octpar'
    id = Column(Integer, primary_key=True)
    octcsv_id = Column(Integer, ForeignKey("octcsv.id"))
    userid = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    octcsv = relationship("OctCSV", backref=backref("octpar", uselist=False, passive_deletes=True))
    frequency = Column(Float)
    points_per_line = Column(Integer)
    points_per_interval = Column(Integer)
    line_length = Column(Float)
    extend_points = Column(Integer)
    reference_points = Column(Integer)
    extend_reference_points = Column(Integer)
    lag_xy = Column(Float)
    x_start = Column(Float)
    x_end = Column(Float)
    y_start = Column(Float)
    y_end = Column(Float)
    x_ref_coordinate = Column(Float)
    y_ref_coordinate = Column(Float)
    jump_speed = Column(Float)
    scantype = Column(String)
    grouporder = Column(Integer)

    def __repr__(self):
        return 'octcsv_id: {}'.formatpostgre(self.octcsv_id)

