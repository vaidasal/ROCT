from pydantic import BaseModel
from typing import Optional
import json

class OctCSV(BaseModel):
    status: Optional[str] = None
    seamid: Optional[int] = None
    linenumber: Optional[str] = None
    datetime: Optional[str] = None
    type: Optional[str] = None
    userid: Optional[int] = None

    class Config:
        orm_mode = True

class CsvData(BaseModel):
    data: Optional[str] = None