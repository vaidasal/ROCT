import pandas as pd
import re
import csv
import os
import json
from datetime import datetime

class OctCsvReader():

    path = "data/OK__11__W865__2021-06-21__10_25_04.299102.csv"

    paramDict = {
        "frequency": "",
        "points_per_line": "",
        "points_per_interval": "",
        "line_length": "",
        "extend_points": "",
        "reference_points": "",
        "extend_reference_points": "",
        "lag_xy": "",
        "x_start": "",
        "x_end": "",
        "y_start": "",
        "y_end": "",
        "x_ref_coordinate": "",
        "y_ref_coordinate": "",
        "jump_speed": "",
        "scantype": "",
        "par_grouporder": "",
    }

    def readTablesFromCSV(self, path):

        with open(path, newline="") as f:
            reader = csv.reader(f)
            data = list(reader)

        # get empty rows
        dataLen = len(data)
        nanRowList = [0]
        for n in range(dataLen):
            if data[n] == [] and n != dataLen - 1:
                nanRowList.append(n + 1)
        nanRowList.append(dataLen)


        # Messlinien/Punktmessung
        dataDict = {}
        dataLen = len(nanRowList)
        groupOrder = 0

        for n in range(dataLen):

            if nanRowList[n] != len(data):
                seam = data[nanRowList[n]][0]
            else:
                seam = ""

            if not re.search(r"^seam", seam):
                continue

            seamData = data[nanRowList[n] + 1:nanRowList[n + 1] - 1]

            cols = seamData[0][0].split(";")

            if cols[9].replace(" ", "") == "WELDING_DEPTH_POINTS_0":
                # its a point
                if n < dataLen - 1:
                    dataDict[f"T{n}"] = {}
                    dataDict[f"T{n}"]["P"] = pd.DataFrame([lst[0].split(";") for lst in seamData], columns=cols).drop(
                        [0]).to_json(orient="table")
                    dataDict[f"T{n}"]["seam"] = seam[6:]
                    dataDict[f"T{n}"]["groupOrder"] = groupOrder
                    groupOrder += 1
            else:
                # its a line
                if n < dataLen - 2:
                    # First Table
                    dataDict[f"T{n}"] = {}
                    dataDict[f"T{n}"]["L1"] = pd.DataFrame([lst[0].split(";") for lst in seamData], columns=cols).drop(
                        [0]).to_json(orient="table")
                    # Second Table
                    seamData2 = data[nanRowList[n + 1]:nanRowList[n + 2] - 1]
                    cols2 = seamData2[1][0].split(";")
                    dataDict[f"T{n}"]["L2"] = pd.DataFrame([lst[0].split(";") for lst in seamData2], columns=cols2).drop(
                        [0,1]).to_json(orient="table")
                    dataDict[f"T{n}"]["seam"] = seam[6:]
                    dataDict[f"T{n}"]["groupOrder"] = groupOrder
                    groupOrder += 1

        # dataDict={"T1":{"P":table}, "T2": {"L1":table1, "L2":table2}}
        return dataDict


    def getCSVNameDetailFromDir(self, path):
        fileList = []
        namesList = []
        for f in os.listdir(path):
            if f.endswith(".csv"): fileList.append(os.path.join(path,f))
            if f.endswith(".csv"): namesList.append(f)

        fileDetail = []
        for f in namesList:
            sp = f.split("__")
            if len(sp) == 4:
                # old standard
                dt = datetime.strptime(f"{sp[2]} {sp[3].rsplit('.', 1)[0]}", "%Y-%m-%d %H_%M_%S.%f")
                sm = {"status": sp[0], "seamid":
                    #random.randrange(1000, 10000)
                    "3000"
                    , "linenumber": sp[1], "datetime": str(dt), "filename": f}
            else:
                # new standard
                dt = datetime.strptime(f"{sp[3]} {sp[4].rsplit('.', 1)[0]}", "%Y-%m-%d %H_%M_%S.%f")
                sm = {"status": sp[0], "seamid": sp[1], "linenumber": sp[2], "datetime": str(dt), "filename": f}
            fileDetail.append(sm)

        # fileList=[{"Status": "OK", "LineNumber": "W888"...}, {"Status": "OK",...}]
        return (fileList, fileDetail)

    def getCSVNameDetailFromFile(self, path):
        if path.endswith(".csv"):
            fileName = path
        else:
            print("not a csv")
            return

        sp = fileName.split("__")
        if len(sp) == 4:
            # old standard
            dt = datetime.strptime(f"{sp[2]} {sp[3].rsplit('.', 1)[0]}", "%Y-%m-%d %H_%M_%S.%f")
            sm = {"status": sp[0], "seamid":
                #random.randrange(1000, 10000)
                "3001"
                , "linenumber": sp[1], "datetime": str(dt)}
        else:
            # new standard
            dt = datetime.strptime(f"{sp[3]} {sp[4].rsplit('.', 1)[0]}", "%Y-%m-%d %H_%M_%S.%f")
            sm = {"status": sp[0], "seamid": sp[1], "linenumber": sp[2], "datetime": str(dt)}

        fileDetail=sm

        # fileList=[{"Status": "OK", "LineNumber": "W888"...}, {"Status": "OK",...}]
        return (fileDetail)

    def readCSVTables(self, path, fileDetail):

        with open(path[2:]) as f:
            reader = csv.reader(f)
            data = list(reader)

        # get empty rows
        dataLen = len(data)
        nanRowList = [0]
        for n in range(dataLen):
            if data[n] == [] and n != dataLen - 1:
                nanRowList.append(n + 1)
        nanRowList.append(dataLen)


        # Messlinien/Punktmessung
        dataDict = {}
        dataLen = len(nanRowList)
        groupOrder = 0

        for n in range(dataLen):

            if nanRowList[n] != len(data):
                seam = data[nanRowList[n]][0]
            else:
                seam = ""

            if not re.search(r"^seam", seam):
                continue

            seamData = data[nanRowList[n] + 1:nanRowList[n + 1] - 1]

            cols = seamData[0][0].split(";")

            if cols[9].replace(" ", "") == "WELDING_DEPTH_POINTS_0":
                # its a point
                if n < dataLen - 1:
                    dataDict[f"T{n}"] = {}
                    dataDict[f"T{n}"]["P"] = pd.DataFrame([lst[0].split(";") for lst in seamData]).drop(
                        [0]).to_json(orient="values")
                    dataDict[f"T{n}"]["C__P"] = cols
                    dataDict[f"T{n}"]["seam"] = seam[6:]
                    dataDict[f"T{n}"]["groupOrder"] = groupOrder
                    dataDict[f"T{n}"].update(fileDetail)
                    dataDict[f"T{n}"].update(self.paramDict)
                    groupOrder += 1
            else:
                # its a line
                if n < dataLen - 2:
                    # First Table
                    dataDict[f"T{n}"] = {}
                    dataDict[f"T{n}"]["L1"] = pd.DataFrame([lst[0].split(";") for lst in seamData]).drop(
                        [0]).to_json(orient="values")
                    dataDict[f"T{n}"]["C__L1"] = cols

                    # Second Table
                    seamData2 = data[nanRowList[n + 1]:nanRowList[n + 2] - 1]
                    cols2 = seamData2[1][0].split(";")
                    dataDict[f"T{n}"]["L2"] = pd.DataFrame([lst[0].split(";") for lst in seamData2]).drop(
                        [0,1]).to_json(orient="values")
                    dataDict[f"T{n}"]["C__L2"] = cols2
                    dataDict[f"T{n}"]["seam"] = seam[6:]
                    dataDict[f"T{n}"]["groupOrder"] = groupOrder
                    dataDict[f"T{n}"].update(fileDetail)
                    dataDict[f"T{n}"].update(self.paramDict)
                    groupOrder += 1

        # dataDict={"T0":{"P":table}, "T2": {"L1":table1, "L2":table2}}
        return dataDict

    def getDataFrame(self, dataDict, table):
        print(dataDict.keys())
        print(table)
        jsonData = dataDict[table]["L2"]
        list = pd.read_json(jsonData, typ="frame", orient="values")

        df = pd.DataFrame(list)
        df.columns = dataDict[table]["C__L2"]
        return df

    def getAllDataFrame(self, dataDict, table):
        print(dataDict.keys())
        print(table)
        jsonData = dataDict[table]["L2"]
        list = pd.read_json(jsonData, typ="frame", orient="values")
        df2 = pd.DataFrame(list)
        df2.columns = dataDict[table]["C__L2"]

        jsonData = dataDict[table]["L1"]
        list = pd.read_json(jsonData, typ="frame", orient="values")
        df1 = pd.DataFrame(list)
        df1.columns = dataDict[table]["C__L1"]
        return [df1, df2]

    def getPointDataFrame(self, dataDict, table):
        print(dataDict.keys())
        print(table)
        jsonData = dataDict[table]["P"]
        list = pd.read_json(jsonData, typ="frame", orient="values")

        df = pd.DataFrame(list)
        df.columns = dataDict[table]["C__P"]
        return df
