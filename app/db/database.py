from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# URL in Docker #SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://octlab:laser@db:5432/LOCTTool_DB"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://octlab:laser@localhost:5432/LOCTTool_DB"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
from models import models

class DataBase():

    def getColumns(self):
        tableCols = {}
        tableCols["public.user"] = models.User().__table__.columns.keys()
        tableCols["octcsv"] = models.OctCSV().__table__.columns.keys()
        tableCols["csvdata"] = models.CsvData().__table__.columns.keys()
        tableCols["laserpar"] = models.LaserPar().__table__.columns.keys()
        tableCols["octpar"] = models.OCTPar().__table__.columns.keys()
        return tableCols

    def getTable(self, col: str, tableCols: dict):
        keys = tableCols.keys()
        for k in keys:
            if col in tableCols[k]:
                return k
