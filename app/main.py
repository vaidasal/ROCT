# activate venv: source venv/Py3VEnv/bin/activate
# activate venv on win: venv\Scripts\activate

from sqlalchemy.orm import Session

from fastapi import Depends, FastAPI, Body

import os
import json


from dependencies import get_db, get_current_user, is_valid_user
from db import crud, database
from schema.user import User
from schema.octcsv import OctCSV
from models.models import CsvData, OctCSV, OCTPar, LaserPar
from octcsvreader import OctCsvReader



from fastapi.middleware.cors import CORSMiddleware
from routers import users

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost/docs",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

app.include_router(users.router)


@app.post("/addparameters", dependencies=[Depends(is_valid_user)])
async def addParameter(db: Session = Depends(get_db), current_user: User = Depends(get_current_user), form_data: dict = Body(None)):
    userid = current_user.id
    chip = json.loads(form_data["chipForm"][0]["chp"])
    chip.remove("Start")

    laser = form_data["laser"][0]
    laser["userid"] = userid
    for key in laser.keys():
        laser[key] = laser[key] if laser[key] != "" else None
    laserData = LaserPar(**laser)
    db.add(laserData)
    db.commit()
    db.refresh(laserData)

    for c in range(len(chip)):
        s = chip[c].split(' ')
        data = form_data[s[0].lower()][int(s[1])]
        for key in data.keys():
            data[key] = data[key] if data[key] != "" else None
        data["scantype"] = s[0].lower()
        data["grouporder"] = c
        data["userid"] = userid
        data["laser_id"] = laserData.id
        data = OCTPar(**data)
        db.add(data)
    db.commit()





@app.get("/refresh", dependencies=[Depends(is_valid_user)])
async def refreshCSV(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    print("refreshing")
    userid = current_user.id
    dataList = []
    reader = OctCsvReader()
    currPath = os.getcwd()
    (fileList, detailList) = reader.getCSVNameDetailFromDir(os.path.join(currPath, "data"))

    for n in range(len(fileList)):

        filesInDb = db.execute(f"SELECT filename FROM octcsv WHERE filename = '{detailList[n]['filename']}'").first()
        #add not to turn filter on
        if not filesInDb:
            # File wasnt imported yet
            print(f"importing: {detailList[n]['filename']}")
            data = reader.readTablesFromCSV(fileList[n])
            detailList[n]["userid"] = userid
            data["fileinfo"] = detailList[n]
            dataList.append(data)

    for data in dataList:
        info = data['fileinfo']
        keys = list(data.keys())
        keys.remove('fileinfo')
        seamid = data['fileinfo']['seamid']
        for key in keys:
            dkey = data[key].keys()
            print(data[key]["seam"])
            type = "Point" if len(dkey) == 3 else "Line"
            tData = info
            tData["linenumber"] = data[key]["seam"]
            tData["grouporder"] = data[key]["groupOrder"]
            tData["type"] = type

            tdata = OctCSV(**tData)
            id = crud.createEntry(db, tdata)
            ndata = CsvData(data=data[key], octcsv_id=id)
            _ = crud.createEntry(db, ndata)

            sqlstr = """SELECT l.id as l_id,o.id as o_id, o.grouporder as o_group FROM public.laserpar as l 
                                    INNER JOIN public.octpar as o ON l.id = o.laser_id 
                                    WHERE l.seam_id = {}"""
            octParam = db.execute(sqlstr.format(seamid)).all()
            if octParam:
                print("octParam",octParam)
                for go in octParam:
                    print("go",go)
                    if go[2] == tData["grouporder"]:
                        print("go012",go[0],go[1],go[2] )
                        sqlst = """UPDATE octpar SET octcsv_id = {} WHERE id = {}"""
                        db.execute(sqlst.format(id, go[1]))
                        sqlst = """UPDATE laserpar SET octcsv_id = {} WHERE id = {}"""
                        db.execute(sqlst.format(id, go[0]))
            db.commit()

    return "success"

@app.get("/octcsv", dependencies=[Depends(is_valid_user)])
async def getOctCSV(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    data = crud.get_octcsv(db, skip=skip, limit=limit)
    return data

@app.get("/settings", dependencies=[Depends(is_valid_user)])
async def getSettings(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    print(current_user.id)
    data = db.execute("SELECT * FROM settings WHERE userid = {}".format(current_user.id)).first()
    return data




@app.post("/postparamtable", dependencies=[Depends(is_valid_user)])
async def paramTable(db: Session = Depends(get_db), cols: list = Body(None)):
    dataBase = database.DataBase()
    tableDict = dataBase.getColumns()
    colsDict = {}
    colslist = []
    for col in cols:
        colslist.append(str(dataBase.getTable(col, tableDict))+"."+col)
        if dataBase.getTable(col, tableDict) in colsDict.keys():
            colsDict[dataBase.getTable(col, tableDict)].append(col)
        else:
            colsDict[dataBase.getTable(col, tableDict)] = [col]
    tableData = []

    col = "laserpar.id as laser_id, octpar.id as octpar_id, " + ", ".join(colslist)
    stri = """
        SELECT {} FROM octcsv
        FULL OUTER JOIN laserpar ON laserpar.seam_id = octcsv.seamid
        FULL OUTER JOIN octpar ON octcsv.id = octpar.octcsv_id
        FULL OUTER JOIN public.user ON octcsv.userid = public.user.id;
    """
    tableData.extend(db.execute(stri.format(col)).all())
    print("table: ",tableData)
    return tableData