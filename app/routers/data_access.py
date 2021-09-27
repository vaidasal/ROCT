from fastapi import APIRouter

from sqlalchemy.orm import Session

from fastapi import Depends, Body

import os
import json


from dependencies import get_db, get_current_user, is_valid_user
from db import crud, database
from schema.user import User
from models.models import CsvData, OctCSV, OCTPar, LaserPar
from octcsvreader import OctCsvReader
from mqtt import Mqtt


router = APIRouter()

@router.post("/addparameters", dependencies=[Depends(is_valid_user)])
async def addParameter(db: Session = Depends(get_db), current_user: User = Depends(get_current_user), form_data: dict = Body(None)):
    userid = current_user.id
    chip = json.loads(form_data["chipForm"][0]["chp"])
    chip.remove("Start")

    laser = form_data["laser"][0]
    laser["userid"] = userid
    for key in laser.keys():
        laser[key] = laser[key] if laser[key] != "" else None
    laserData = LaserPar(**laser)
    laserDataId = crud.createEntry(db=db, new_obj=laserData)

    for c in range(len(chip)):
        s = chip[c].split(' ')
        data = form_data[s[0].lower()][int(s[1])]
        for key in data.keys():
            data[key] = data[key] if data[key] != "" else None
        data["scantype"] = s[0].lower()
        data["grouporder"] = c
        data["userid"] = userid
        data["laser_id"] = laserDataId
        data = OCTPar(**data)
        _ = crud.createEntry(db=db, new_obj=data)






@router.get("/refresh", dependencies=[Depends(is_valid_user)])
async def refreshCSV(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    print("refreshing")
    userid = current_user.id
    dataList = []
    reader = OctCsvReader()
    currPath = os.getcwd()
    (fileList, detailList) = reader.getCSVNameDetailFromDir(os.path.join(currPath, "data"))

    mqtt = Mqtt()
    mqtt.sendMessage("{just a test message}")

    for n in range(len(fileList)):

        filesInDb = db.execute(f"SELECT filename FROM octcsv WHERE filename = '{detailList[n]['filename']}'").first()
        #add not to turn filter on
        if filesInDb:
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

@router.get("/octcsv", dependencies=[Depends(is_valid_user)])
async def getOctCSV(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    data = crud.get_octcsv(db, skip=skip, limit=limit)
    return data

@router.get("/settings", dependencies=[Depends(is_valid_user)])
async def getSettings(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    print(current_user.id)
    data = db.execute("SELECT * FROM settings WHERE userid = {}".format(current_user.id)).first()
    return data




@router.post("/postparamtable", dependencies=[Depends(is_valid_user)])
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

    col = "laserpar.id as laser_id, octpar.id as octpar_id, octpar.scantype as scantype, " + ", ".join(colslist)
    stri = """
        SELECT {} FROM octcsv
        FULL OUTER JOIN laserpar ON laserpar.seam_id = octcsv.seamid
        FULL OUTER JOIN octpar ON octcsv.id = octpar.octcsv_id
        FULL OUTER JOIN public.user ON octcsv.userid = public.user.id;
    """
    tableData.extend(db.execute(stri.format(col)).all())
    print("table: ",tableData)
    return tableData