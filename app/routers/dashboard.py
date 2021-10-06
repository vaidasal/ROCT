from fastapi import APIRouter, Body

from plotlyVis import PlotlyVis
import db.crud as crud

router = APIRouter()


@router.post("/dashboard")
async def makeDashboard(rowsdict: dict = Body(None)):
    pltVis = PlotlyVis()

    colorList = ["#BB86FC", "#03DAC6", "#B00020", "#FFA000", "#CDDC39", "#FF4081", "#795548"]

    plots = {"crosstext": "Cross Scan","paralleltext": "Parallel Scan", "pointtext": "Point Scan",
             "parallel": [], "cross": [], "point": []}

    rows = rowsdict["rows"]
    darkmode = rowsdict["mode"]

    if len(rows) != 0:
        par = []
        cro = []
        poi = []

        for row in rows:
            if row["scantype"] == "parallel": par.append(row)
            elif row["scantype"] == "cross": cro.append(row)
            elif row["scantype"] == "point": poi.append(row)

        ########## PARALLEL
        pardf = []
        parleg = []
        asl = []
        for i in range(len(par)):
            print("Parallel plot")

            # Daten aus Datenbank
            durchlaufDauer = 8.81
            prozessDauer = 240
            durchlaufeProNaht = prozessDauer/durchlaufDauer
            nahtLange = 30
            asl.append(nahtLange/durchlaufeProNaht) #AbstanScanLine
            tableNames = ["T0", "T3", "T5"]
            sheet1 = 0.6
            gap = 0.3
            sheet2 = 1
            path = r"C:\Users\valaune\Desktop\Data\77\OK__W865__2021-06-21__10_25_04.299102.csv"

            pardf.append(crud.readLocalData(tableNames[i], path, False))
            parleg.append("SeamID: " + str(par[i]["seamid"]))

        plots["parallel"].append(pltVis.getParallelHeatFig(pardf, parleg, colorList, darkmode))
        plots["parallel"].append(pltVis.makeParalelSynced(pardf, parleg, colorList, darkmode))
        for i in range(len(pardf)):
            plots["parallel"].append(pltVis.getParallelSlideLine(pardf[i], asl[i], colorList[i], sheet1, gap, sheet2, darkmode))

        ######## CROSS
        crodf = []
        croleg = []
        asl = []
        for i in range(len(cro)):
            print("Cross plot")

            # Daten aus Datenbank
            durchlaufDauer = 2.38
            prozessDauer = 240
            durchlaufeProNaht = prozessDauer / durchlaufDauer
            nahtLange = 30
            asl.append(nahtLange / durchlaufeProNaht)  # AbstandScanLine
            tableNames = ["T0", "T3", "T5"]
            sheet1 = 0.6
            gap = 0.3
            sheet2 = 1
            path = r"C:\Users\valaune\Desktop\Data\OK__W885__2021-07-30__11_02_47.937988.csv"

            crodf.append(crud.readLocalData(tableNames[i], path, False))
            croleg.append("SeamID: " + str(cro[i]["seamid"]))

        plots["cross"].append(pltVis.getHeatSubFig(crodf, croleg, colorList, asl, darkmode))
        for i in range(len(crodf)):
            plots["cross"].append(pltVis.getSlideLine(crodf[i], asl[i], colorList[i], sheet1, gap, sheet2, darkmode))

        ######## POINT
        poidf = []
        poileg = []
        asl = []
        for i in range(len(poi)):
            print("Point plot")

            # Daten aus Datenbank
            durchlaufDauer = 2.38
            prozessDauer = 240
            durchlaufeProNaht = prozessDauer / durchlaufDauer
            nahtLange = 30
            asl.append(nahtLange / durchlaufeProNaht)  # AbstandScanLine
            tableNames = ["T2", "T3", "T5"]
            sheet1 = 0.3
            gap = 0.1
            sheet2 = 1
            path = r"C:\Users\valaune\Desktop\Data\Point\OK__W885__2021-04-26__12_08_31.426051.csv"

            poidf.append(crud.readLocalData(tableNames[i], path, True))
            print(poi)
            poileg.append("SeamID: " + str(poi[i]["seamid"]))

        plots["point"].append(pltVis.getHeatFig(poidf, poileg, colorList, sheet1, gap, sheet2, darkmode))
        #for i in range(len(poidf)):
        #    plots["point"].append(pltVis.getSlideLine(poidf[i], asl[i], colorList[i], sheet1, gap, sheet2))


        return plots
