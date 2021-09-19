import plotly.express as px

from octcsvreader import OctCsvReader
import numpy as np
import pandas as pd

class PlotlyVis:

    path = r"C:\Users\valaune\Desktop\OK__W885__2021-07-30__11_02_47.937988.csv"

    color = "#BB86FC"

    def getHeatFig(self):
        reader = OctCsvReader()
        fileDetail = reader.getCSVNameDetailFromFile(self.path)
        dataJson = reader.readCSVTables(self.path, fileDetail)
        df = reader.getDataFrame(dataJson)
        df = df.drop(["Line Start [us]", "Line End [us]"], axis=1).reset_index(drop=True) # leaves only xz Matrix
        (x,z,i) = self.makeXZ(df)

        trace1 = dict(
            x=x,
            y=z,
            mode='markers',
            name='points',
            marker={"color": self.color, "size":2, "opacity":0.5},
            type='scatter',
            text=i,
        )
        trace2 = dict(
            x=x,
            y=z,
            name='density',
            ncontours= 20,
            colorscale= 'Hot',
            showscale= False,
            type='histogram2dcontour',
        )
        trace3 = dict(
            x=x,
            name= 'x density',
            yaxis= 'y2',
            type='histogram',
            marker={"color": self.color},
            opacity= 0.5,
            xbins={"size": 1/max(i)},
        )
        trace4 = dict(
            y=z,
            name='z density',
            type='histogram',
            xaxis="x2",
            opacity=0.5,
            marker={"color": self.color}
        )

        layout = dict(
            showlegend=False,
            hovermode= 'closest',
            bargap=0.01,
            barmode= 'overlay',
            paper_bgcolor="black",
            plot_bgcolor="black",
            margin={"r":20, "t":40, "b":40, "l":60},
            xaxis={"domain": [0, 0.85], "zeroline": False, "showgrid": False},
            yaxis={"domain": [0, 0.82], "zeroline": False, "showgrid": False},
            xaxis2={"domain": [0.85, 1], "zeroline": True, "showgrid": False, "ticks": "outside"},
            yaxis2={"domain": [0.85, 1], "zeroline": True, "showgrid": False, "ticks": "outside"},
        )

        graph = {
            "data": [trace2, trace1, trace3, trace4],
            "layout": layout,

        }

        return graph

    def makeXZ(self, df):
        x = []
        z = []
        i = []

        for key in df.keys():
            df = df.astype('float64')
            kSer = df.loc[:,key]
            zSer = kSer[kSer!=0]

            z.extend(list(zSer))
            i.extend(list(zSer.index))

            xSer = np.full((1, len(zSer)),key).tolist()[0]
            x.extend(xSer)

        return (x,z,i)


    def getSlideLine(self):
        reader = OctCsvReader()
        fileDetail = reader.getCSVNameDetailFromFile(self.path)
        dataJson = reader.readCSVTables(self.path, fileDetail)
        df = reader.getDataFrame(dataJson)
        df = df.drop(["Line Start [us]", "Line End [us]"], axis=1).reset_index(drop=True).astype('float64') # leaves only xz Matrix

        sheet1 = 0.4
        gap = 0.1
        sheet2 = 1

        ma = df.to_numpy().max()
        mi = min(df.to_numpy().min(), -sheet1-gap-sheet2)


        df = df.to_dict('split')
        cols = df["columns"]
        dfData = df["data"]
        data = []

        # ADD LINE PLOT
        for index in range(len(dfData)):
            data.append({
                "x": cols,
                "y": dfData[index],
                "text": index,
                "mode": "lines+markers",
                "line": {"shape": 'spline', "color": self.color},
                "marker": {"size":4},
                "visible": True if index == 0 else False,
            })

        dataLen = len(data)


        # ADD 3D LINE PLOT
        for i in range(len(dfData)):
            z = []
            x = []
            for index in range(i):
                z = list(np.divide(dfData[i], 6))
                x = [i / 8] * len(cols)
            data.append({"z": z,
                         "x": cols,
                         "y": x,
                         "type": 'scatter3d',
                         "mode": "lines",
                         "scene": "scene1",
                         "visible": True if i == 1 else False,
                         "line": {"width": 8, "color": self.color}
                         })

        # ADD SHEET1 TO FILL
        for index in range(len(dfData)):
            data.append({
                "x": cols,
                "y": list(map(lambda x: x if x < -sheet1 else -sheet1, dfData[index])),
                "mode": "lines",
                "line": {"shape": 'spline', "color": self.color},
                "visible": True if index == 0 else False,
                "fill": "tonexty",
            })
        # ADD GAP TO FILL
        gapLine = -sheet1 - gap
        for index in range(len(dfData)):
            data.append({
                "x": cols,
                "y": list(map(lambda x: x if x < gapLine else gapLine, dfData[index])),
                "mode": "lines",
                "line": {"shape": 'spline', "color": self.color},
                "visible": True if index == 0 else False,
            })

        # ADD SHEET2 TO FILL
        sheet2Line = gapLine - sheet2
        for index in range(len(dfData)):
            data.append({
                "x": cols,
                "y": list(map(lambda x: x if x < sheet2Line else sheet2Line, dfData[index])),
                "mode": "lines",
                "line": {"shape": 'spline', "color": self.color},
                "visible": True if index == 0 else False,
                "fill": "tonexty",
            })

        # ADD 3D SURFACE
        z = []
        x = []
        for index in range(len(dfData)):
            z.append(list(np.divide(dfData[index], 6)))
            x.append(index / 8)
        data.append({"z": z, "x": cols, "y": x, "type": 'surface', "scene": "scene1", "showscale": False})

        sliderSteps = []
        for i in range(dataLen):
            step = dict(
                method="update",
                args=[{"visible": [False] * len(data)}]
            )

            step["args"][0]["visible"][i] = True
            step["args"][0]["visible"][i + dataLen] = True
            step["args"][0]["visible"][i + dataLen * 2] = True
            step["args"][0]["visible"][i + dataLen * 3] = True
            step["args"][0]["visible"][i + dataLen * 4] = True
            step["args"][0]["visible"][len(data) - 1] = True

            sliderSteps.append(step)



        layout = dict(
            showlegend=False,
            hovermode= 'closest',
            paper_bgcolor="black",
            plot_bgcolor="black",
            margin={"r":20, "t":40, "b":120, "l":60},
            xaxis={"showgrid": False, "zeroline": False, "rangeslider": {}, "domain": [0,0.5]},
            yaxis={"showgrid": False, "range": [mi,ma], "autorange": False, "fixedrange": True},
            sliders= [{
                "steps": sliderSteps,
                "currentvalue": {"prefix": "Line: "},
                "len": 0.48,
                "x": 1,
                "lenmode": "fraction",
                "xanchor": "right",
                "transition": {"easing": "linear"},
            }],
            coloraxis= {"colorbar":False},
            scene1=dict(
                domain={"x": [0.5, 1]},
                aspectmode="data",
                xaxis={"showgrid": False, "visible": False},
                yaxis={"showgrid": False, "scaleanchor": "x", "scaleratio": 1, "visible": False},
                zaxis={"showgrid": False, "scaleanchor": "x", "scaleratio": 1, "visible": False},
            ),
        )

        graph = {
            "layout": layout,
            "data": data,
        }

        return graph



