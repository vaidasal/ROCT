from fastapi import APIRouter, Body

from plotlyVis import PlotlyVis
import db.crud as crud
import plotly.io as plio

router = APIRouter()

@router.post("/dashboard")
async def makeDashboard(rows: list = Body(None)):
    pltVis = PlotlyVis()

    colorList = ["#BB86FC", "#03DAC6", "#B00020"]

    plots = {"crosstext": "Cross Scan","paralleltext": "Parallel Scan", "pointtext": "Point Scan",
             "parallel": [], "cross": [], "point": []}
    print(rows)
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
            durchlaufDauer = 2.38
            prozessDauer = 240
            durchlaufeProNaht = prozessDauer/durchlaufDauer
            nahtLange = 30
            asl.append(nahtLange/durchlaufeProNaht) #AbstanScanLine
            tableNames = ["T0", "T3", "T5"]

            pardf.append(crud.readLocalData(tableNames[i]))
            parleg.append("SeamID: " + str(par[i]["seamid"]))

        plots["parallel"].append(pltVis.getHeatSubFig(pardf, parleg, colorList, asl))
        for i in range(len(pardf)):
            plots["parallel"].append(pltVis.getSlideLine(pardf[i], asl[i], colorList[i]))

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

            crodf.append(crud.readLocalData(tableNames[i]))
            croleg.append("SeamID: " + str(cro[i]["seamid"]))

        plots["cross"].append(pltVis.getHeatSubFig(crodf, croleg, colorList, asl))
        for i in range(len(crodf)):
            plots["cross"].append(pltVis.getSlideLine(crodf[i], asl[i], colorList[i]))

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
            tableNames = ["T0", "T3", "T5"]

            poidf.append(crud.readLocalData(tableNames[i]))
            poileg.append("SeamID: " + str(par[i]["seamid"]))

        plots["point"].append(pltVis.getHeatFig(poidf, poileg, colorList))
        for i in range(len(poidf)):
            plots["point"].append(pltVis.getSlideLine(poidf[i], asl[i], colorList[i]))

            """
            if rows[i]["scantype"] == "cross":
                print("Cross plot")

                # Daten aus Datenbank
                durchlaufDauer = 2.38
                prozessDauer = 240
                durchlaufeProNaht = prozessDauer/durchlaufDauer
                nahtLange = 30
                abstandScanlinie = nahtLange/durchlaufeProNaht

                df = [crud.readLocalData("T3")]

                niceString = "SeamID: " + str(rows[i]["seamid"])
                figHeat = pltVis.getHeatFig(df, niceString, colorList)

                figSlideLine1 = pltVis.getSlideLine(crud.readLocalData("T0"), abstandScanlinie, colorList[0])
                #figSlideLine2 = pltVis.getSlideLine(crud.readLocalData("T5"), abstandScanlinie, colorList[1])

                plots = {**plots, **{"cross": [figHeat, figSlideLine1], "crosstext": "Cross Scan"}}

            if rows[i]["scantype"] == "point":
                print("Point plot")

                # Daten aus Datenbank
                durchlaufDauer = 2.38
                prozessDauer = 240
                durchlaufeProNaht = prozessDauer/durchlaufDauer
                nahtLange = 30
                abstandScanlinie = nahtLange/durchlaufeProNaht

                df = [crud.readLocalData("T3")]

                niceString = "SeamID: " + str(rows[i]["seamid"])
                figHeat = pltVis.getHeatFig(df, niceString, colorList)

                figSlideLine1 = pltVis.getSlideLine(crud.readLocalData("T0"), abstandScanlinie, colorList[0])
                #figSlideLine2 = pltVis.getSlideLine(crud.readLocalData("T5"), abstandScanlinie, colorList[1])

                plots = {**plots, **{"point": [figHeat, figSlideLine1], "pointtext": "Point Scan"}}
                """
        return plots
