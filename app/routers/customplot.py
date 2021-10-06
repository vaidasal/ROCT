from fastapi import APIRouter, Body

from plotlyVis import PlotlyVis
import db.crud as crud

router = APIRouter()

@router.post("/customplot")
async def makeCustomPlot(dataList: list = Body(None)):
    print(dataList)
    pltVis = PlotlyVis()
    colorList = ["#BB86FC", "#03DAC6", "#B00020", "#FFA000", "#CDDC39", "#FF4081", "#795548"]
    plots = {"customtext": "", "custom": []}

    for data in dataList:
        if len(data["rows"]) != 0:
            cusdf = []
            cusleg = []
            pointpath = r"C:\Users\valaune\Desktop\Data\Point\OK__W885__2021-04-26__12_08_31.426051.csv"
            linepath = r"C:\Users\valaune\Desktop\Data\77\OK__W865__2021-06-21__10_25_04.299102.csv"
            scantype = ""
            for row in data["rows"]:
                if scantype == "": scantype = row["type"]
                if scantype != row["type"]: continue

                if scantype == "Point":
                    cusdf.append(crud.readLocalData("T2", pointpath, True))
                elif scantype == "Line":
                    cusdf.append(crud.readLocalData("T0", linepath, "all"))
                cusleg.append("SeamID: " + str(row["seamid"]))
            if scantype == "Point":
                print("point")
                plots["custom"].append(pltVis.getFig(cusdf, cusleg, colorList, data["basketL"],
                                                 data["basketX"], data["basketR"],
                                                 data["chartType"], data["chartTitle"], data["darkmodeCheck"],
                                                 data["xAxName"], data["yAxName"], data["yyAxName"]))
            elif scantype == "Line":
                print("line")
                plots["custom"].append(pltVis.getLnFig(cusdf, cusleg, colorList, data["basketL"],
                                                     data["basketX"], data["basketR"],
                                                     data["chartType"], data["chartTitle"], data["darkmodeCheck"],
                                                     data["xAxName"], data["yAxName"], data["yyAxName"]))

    return plots

@router.post("/getcols")
async def getcols(row: list = Body(None)):
    pointpath = r"C:\Users\valaune\Desktop\Data\Point\OK__W885__2021-04-26__12_08_31.426051.csv"
    linepath = r"C:\Users\valaune\Desktop\Data\77\OK__W865__2021-06-21__10_25_04.299102.csv"
    if len(row) != 0:
        if row[0]["type"] == "Line":
            cols = list(crud.readLocalData("T0", linepath, "all")[0].keys())
            cols = list(filter(lambda x: x != "Timestamp", cols))
            cols = list(filter(lambda x: x != "", cols))
        else:
            cols = list(crud.readLocalData("T2", pointpath, True).keys())
            cols = list(filter(lambda x: x != "Timestamp", cols))
            cols = list(filter(lambda x: x != "", cols))
    return cols