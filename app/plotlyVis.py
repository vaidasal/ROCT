
import numpy as np
import pandas as pd


class PlotlyVis:
    path = r"C:\Users\valaune\Desktop\OK__W885__2021-07-30__11_02_47.937988.csv"

    color = "#BB86FC"
    colorList = ["#BB86FC", "#03DAC6", "#B00020"]


    ################################## POINT ###########################################
    def getHeatFig(self, df, legend, colorList, sheet1, gap, sheet2):
        data = []
        ci = 0
        for d in df:
            color = colorList[ci]
            #df = d.drop(["Line Start [us]", "Line End [us]"], axis=1).reset_index(drop=True) # leaves only xz Matrix
            #(x,z,i) = self.makeXZ(df)

            x = d.iloc[:, 8]
            x = pd.to_datetime(x, unit="us")


            """trace2 = dict(
                x=list(x),
                y=list(d.iloc[:, 9]),
                name='density',
                ncontours= 20,
                colorscale= 'Hot',
                showscale= False,
                type='histogram2dcontour',
                legendgroup=str(ci),
                showlegend=False,
            )"""


            trace1 = dict(
                x=list(x),
                y=list(d.iloc[:, 9]),
                mode= "lines+markers",
                line= {"shape": 'spline', "color": color, "width": 1},
                name='points',
                marker={"color": color, "size":2, "opacity":0.5},
                type='scatter',
                legendgroup=str(ci),
                showlegend=False,
            )

            trace3 = dict(
                x=list(x),
                name= 'x density',
                yaxis= 'y2',
                type='histogram',
                marker={"color": color},
                opacity= 0.5,
                legendgroup=str(ci),
                showlegend=False,
            )
            trace4 = dict(
                y=list(d.iloc[:, 9]),
                name=legend[ci],
                type='histogram',
                xaxis="x2",
                opacity=0.5,
                marker={"color": color},
                legendgroup = str(ci),
            )

            #data.append(trace2)
            data.append(trace1)
            data.append(trace3)
            data.append(trace4)

            ci = ci + 1

            # ADD SHEET1 TO FILL
            data.append({
                "x": list(x),
                "y": list(map(lambda sx: sx if sx < -sheet1 else -sheet1, list(d.iloc[:, 9]))),
                "mode": "lines",
                "line": {"shape": 'spline', "color": color},
                "fill": "tonexty",
                "showlegend": False,
            })
            # ADD GAP TO FILL
            gapLine = -sheet1 - gap
            data.append({
                "x": list(x),
                "y": list(map(lambda sx: sx if sx < gapLine else gapLine, list(d.iloc[:, 9]))),
                "mode": "lines",
                "line": {"shape": 'spline', "color": color},
                "showlegend": False,
            })

            # ADD SHEET2 TO FILL
            sheet2Line = gapLine - sheet2
            data.append({
                "x": list(x),
                "y": list(map(lambda sx: sx if sx < sheet2Line else sheet2Line, list(d.iloc[:, 9]))),
                "mode": "lines",
                "line": {"shape": 'spline', "color": color},
                "fill": "tonexty",
                "showlegend": False,
            })


        layout = dict(
            font={"color": "white"},
            legend={"x": 0, "y":1.1, "orientation": "h"},
            hovermode= 'closest',
            bargap=0.01,
            barmode= 'overlay',
            height= "700px",
            paper_bgcolor="black",
            plot_bgcolor="black",
            margin={"r":20, "t":0, "b":60, "l":60},
            xaxis={"domain": [0, 0.85], "zeroline": False, "showgrid": False,
                   "tickformat": '%s.%f', "title": "Time [s]"},
            yaxis={"domain": [0, 0.82], "zeroline": False, "showgrid": False},
            xaxis2={"domain": [0.85, 1], "zeroline": True, "showgrid": False,
                    "ticks": "outside"},
            yaxis2={"domain": [0.85, 1], "zeroline": True, "showgrid": False,
                    "ticks": "outside"},
        )

        graph = {
            "data": data,
            "layout": layout,
            "config": {"responsive": True},

        }

        return graph

    ################################# CROSS ############################################

    def getHeatSubFig(self, df, legend, colorList, asl):
        data = []
        ci = 0
        for d in df:
            color = colorList[ci]
            df = d.drop(["Line Start [us]", "Line End [us]"], axis=1).reset_index(drop=True) # leaves only xz Matrix
            (x,z,i) = self.makeXZ(df)


            ################
            trace2 = dict(
                x=x,
                y=z,
                name='density',
                ncontours= 20,
                colorscale= 'Hot',
                showscale= False,
                type='histogram2dcontour',
                legendgroup=str(ci),
                showlegend=False,
                opacity=0.7,
            )


            trace1 = dict(
                x=x,
                y=z,
                mode='markers',
                name='points',
                marker={"color": color, "size":2, "opacity":0.5},
                type='scatter',
                text=i,
                legendgroup=str(ci),
                showlegend=False,
            )

            trace3 = dict(
                x=x,
                name= 'x density',
                yaxis= 'y2',
                type='histogram',
                marker={"color": color},
                opacity= 0.5,
                xbins={"size": 1/35},
                legendgroup=str(ci),
                showlegend=False,
            )
            trace4 = dict(
                y=z,
                name=legend[ci],
                type='histogram',
                xaxis="x2",
                opacity=0.5,
                marker={"color": color},
                legendgroup = str(ci),
            )

            data.append(trace2)
            data.append(trace1)
            data.append(trace3)
            #data.append(trace4)


            ##################################
            trace6 = dict(
                x=i,
                y=z,
                xaxis="x3",
                yaxis="y3",
                name='density',
                ncontours=20,
                colorscale='Hot',
                showscale=False,
                type='histogram2dcontour',
                legendgroup=str(ci),
                showlegend=False,
                opacity=0.7,
            )

            trace5 = dict(
                x=i,
                y=z,
                xaxis="x3",
                yaxis="y3",
                mode='markers',
                name='points',
                marker={"color": color, "size": 2, "opacity": 0.5},
                type='scatter',
                text=x,
                legendgroup=str(ci),
                showlegend=False,
            )

            trace7 = dict(
                x=i,
                name='x density',
                xaxis="x3",
                yaxis="y4",
                type='histogram',
                marker={"color": color},
                opacity=0.5,
                legendgroup=str(ci),
                showlegend=False,
            )
            trace8 = dict(
                y=z,
                name=legend[ci],
                type='histogram',
                xaxis="x4",
                yaxis="y3",
                opacity=0.5,
                marker={"color": color},
                legendgroup=str(ci),
            )

            data.append(trace6)
            data.append(trace5)
            data.append(trace7)
            data.append(trace8)
            ################################

            ci = ci + 1


        layout = dict(
            font={"color": "white"},
            legend={"x": 0, "y":1.1, "orientation": "h"},
            hovermode= 'closest',
            bargap=0.1,
            barmode= 'overlay',
            height= "700px",
            paper_bgcolor="black",
            plot_bgcolor="black",
            margin={"r":20, "t":0, "b":40, "l":60},
            grid={"rows":1,"columns":2, "subplots":[["xy","x4y4"]]},
            xaxis={"title": "x TCP [mm]", "domain": [0, 0.49], "zeroline": False,
                   "showgrid": False},
            yaxis={"title": "z Depth [mm]", "domain": [0, 0.82], "zeroline": False,
                   "showgrid": False},
            #xaxis2={"domain": [0.4, 0.5], "zeroline": True, "showgrid": False, "ticks": "outside"},
            yaxis2={"domain": [0.85, 1], "zeroline": True, "showgrid": False,
                    "ticks": "outside"},
            xaxis3={"title": "y Progression", "domain": [0.5, 0.9], "zeroline": False,
                    "showgrid": False, "ticks": "outside"},
            yaxis3={"domain": [0, 0.82], "zeroline": False, "showgrid": False,
                    "ticks": "outside"},
            xaxis4={"domain": [0.91, 1], "zeroline": True, "showgrid": False,
                    "ticks": "outside"},
            yaxis4={"domain": [0.85, 1], "zeroline": True, "showgrid": False,
                    "ticks": "outside", "side": "right", "anchor": "x3"},
        )

        graph = {
            "data": data,
            "layout": layout,
            "config": {"responsive": True},

        }

        return graph

    def makeXZ(self, df):
        x = []
        z = []
        i = []

        for key in df.keys():
            df = df.astype('float64')
            kSer = df.loc[:,key]
            #zSer = kSer
            zSer = kSer[kSer!=0]

            z.extend(list(zSer))
            i.extend(list(zSer.index))

            xSer = np.full((1, len(zSer)),key).tolist()[0]
            x.extend(xSer)

        return (x,z,i)


    def getSlideLine(self, df, scanStep, color, sheet1, gap, sheet2):

        df = df.drop(["Line Start [us]", "Line End [us]"], axis=1).reset_index(drop=True).astype('float64') # leaves only xz Matrix

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
                "line": {"shape": 'spline', "color": color},
                "marker": {"size":4},
                "visible": True if index == 0 else False,
            })

        dataLen = len(data)





        # ADD 3D LINE PLOT
        yStepList = list(np.arange(0, len(dfData) + 1) * scanStep)[1:]

        for i in range(len(dfData)):
            z = []
            x = []
            for index in range(i):
                z = list(np.divide(dfData[i], 1))
                x = [yStepList[index]] * len(cols)

            data.append({"z": z,
                         "x": cols,
                         "y": x,
                         "type": 'scatter3d',
                         "mode": "lines",
                         "scene": "scene1",
                         "visible": True if i == 0 else False,
                         "line": {"width": 12, "color": "red"}
                         })

        # ADD SHEET1 TO FILL
        for index in range(len(dfData)):
            data.append({
                "x": cols,
                "y": list(map(lambda x: x if x < -sheet1 else -sheet1, dfData[index])),
                "mode": "lines",
                "line": {"shape": 'spline', "color": color},
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
                "line": {"shape": 'spline', "color": color},
                "visible": True if index == 0 else False,
            })

        # ADD SHEET2 TO FILL
        sheet2Line = gapLine - sheet2
        for index in range(len(dfData)):
            data.append({
                "x": cols,
                "y": list(map(lambda x: x if x < sheet2Line else sheet2Line, dfData[index])),
                "mode": "lines",
                "line": {"shape": 'spline', "color": color},
                "visible": True if index == 0 else False,
                "fill": "tonexty",
            })

        # ADD 3D SURFACE
        yStepList = list(np.arange(0, len(dfData)) * scanStep)
        z = []
        x = []
        for index in range(len(dfData)):
            z.append(list(np.divide(dfData[index], 1)))
        data.append({"z": z, "x": cols, "y": yStepList, "type": 'surface', "scene": "scene1", "showscale": False})

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
            font={"color": "white"},
            height="600px",
            showlegend=False,
            hovermode= 'closest',
            paper_bgcolor="black",
            plot_bgcolor="black",
            margin={"r":20, "t":20, "b":40, "l":60},
            xaxis={"title": "x TCP [mm]", "showgrid": False, "zeroline": False, "rangeslider": {}, "domain": [0,0.5]},
            yaxis={"title": "z Depth [mm]", "showgrid": False, "range": [mi,ma], "autorange": False, "fixedrange": True},
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
                camera={"eye": {"x": 1, "y": 0.1, "z": 1}},
                aspectmode="data",
                xaxis={"showgrid": False, "visible": False},
                yaxis={"showgrid": False, "scaleanchor": "x", "scaleratio": 1, "visible": False},
                zaxis={"showgrid": False, "scaleanchor": "x", "scaleratio": 1, "visible": False},
            ),
        )


        graph = {
            "layout": layout,
            "data": data,
            "config": {"responsive": True},
        }

        return graph

    ####################################### PARALLEL ####################################

    def getParallelHeatFig(self, df, legend, colorList):
        data = []
        ci = 0
        for d in df:
            color = colorList[ci]
            df = d.drop(["Line Start [us]", "Line End [us]"], axis=1).reset_index(drop=True)  # leaves only xz Matrix
            (x, z, i) = self.makeParallelXZ(df)

            ################
            trace2 = dict(
                x=x,
                y=z,
                name='density',
                ncontours=20,
                colorscale='Hot',
                showscale=False,
                type='histogram2dcontour',
                legendgroup=str(ci),
                showlegend=False,
                opacity=0.7,
            )

            trace1 = dict(
                x=x,
                y=z,
                mode='markers',
                name='points',
                marker={"color": color, "size": 2, "opacity": 0.5},
                type='scatter',
                text=i,
                legendgroup=str(ci),
                showlegend=False,
            )

            trace3 = dict(
                x=x,
                name='x density',
                yaxis='y2',
                type='histogram',
                marker={"color": color},
                opacity=0.5,
                xbins={"size": 1 / 35},
                legendgroup=str(ci),
                showlegend=False,
            )
            trace4 = dict(
                y=z,
                name=legend[ci],
                type='histogram',
                xaxis="x2",
                opacity=0.5,
                marker={"color": color},
                legendgroup=str(ci),
            )

            data.append(trace2)
            data.append(trace1)
            data.append(trace3)
            # data.append(trace4)

            ##################################
            trace6 = dict(
                x=i,
                y=z,
                xaxis="x3",
                yaxis="y3",
                name='density',
                ncontours=20,
                colorscale='Hot',
                showscale=False,
                type='histogram2dcontour',
                legendgroup=str(ci),
                showlegend=False,
                opacity=0.7,
            )

            trace5 = dict(
                x=i,
                y=z,
                xaxis="x3",
                yaxis="y3",
                mode='markers',
                name='points',
                marker={"color": color, "size": 2, "opacity": 0.5},
                type='scatter',
                text=x,
                legendgroup=str(ci),
                showlegend=False,
            )

            trace7 = dict(
                x=i,
                name='x density',
                xaxis="x3",
                yaxis="y4",
                type='histogram',
                marker={"color": color},
                opacity=0.5,
                legendgroup=str(ci),
                showlegend=False,
            )
            trace8 = dict(
                y=z,
                name=legend[ci],
                type='histogram',
                xaxis="x4",
                yaxis="y3",
                opacity=0.5,
                marker={"color": color},
                legendgroup=str(ci),
            )

            data.append(trace6)
            data.append(trace5)
            data.append(trace7)
            data.append(trace8)
            ################################

            ci = ci + 1

        layout = dict(
            font={"color": "white"},
            legend={"x": 0, "y": 1.1, "orientation": "h"},
            hovermode='closest',
            bargap=0.1,
            barmode='overlay',
            height="700px",
            paper_bgcolor="black",
            plot_bgcolor="black",
            margin={"r": 20, "t": 0, "b": 40, "l": 60},
            grid={"rows": 1, "columns": 2, "subplots": [["xy", "x4y4"]]},
            xaxis={"title": "x TCP [mm]", "domain": [0, 0.49], "zeroline": False, "showgrid": False},
            yaxis={"title": "z Depth [mm]", "domain": [0, 0.82], "zeroline": False, "showgrid": False},
            # xaxis2={"domain": [0.4, 0.5], "zeroline": True, "showgrid": False, "ticks": "outside"},
            yaxis2={"domain": [0.85, 1], "zeroline": True, "showgrid": False, "ticks": "outside"},
            xaxis3={"title": "y Progression", "domain": [0.5, 0.9], "zeroline": False, "showgrid": False,
                    "ticks": "outside"},
            yaxis3={"domain": [0, 0.82], "zeroline": False, "showgrid": False, "ticks": "outside"},
            xaxis4={"domain": [0.91, 1], "zeroline": True, "showgrid": False, "ticks": "outside"},
            yaxis4={"domain": [0.85, 1], "zeroline": True, "showgrid": False, "ticks": "outside", "side": "right",
                    "anchor": "x3"},
        )

        graph = {
            "data": data,
            "layout": layout,
            "config": {"responsive": True},

        }

        return graph

    def makeParallelXZ(self, df):
        x = []
        z = []
        i = []

        for key in df.keys():
            df = df.replace("", float("nan")).astype('float64')
            kSer = df.loc[:,key]
            zSer = kSer.dropna()



            z.extend(list(zSer))
            i.extend(list(zSer.index))

            xSer = np.full((1, len(zSer)),key).tolist()[0]
            x.extend(xSer)
        return (x,z,i)


    def getParallelSlideLine(self, df, scanStep, color, sheet1, gap, sheet2):

        df = df.drop(["Line Start [us]", "Line End [us]"], axis=1).reset_index(drop=True).replace("", float("nan")).astype('float64') # leaves only xz Matrix

        ma = np.nanmax(df.to_numpy()) + 0.1
        mi = min(np.nanmin(df.to_numpy()), -sheet1-gap-sheet2) - 0.1


        df = df.to_dict('split')
        cols = df["columns"]
        dfData = df["data"]
        data = []

        xmi = min(np.float_(cols)) - 0.1
        xma = max(np.float_(cols)) + 0.1

        # ADD LINE PLOT
        for index in range(len(dfData)):
            yl = ~np.isnan(dfData[index])

            data.append({
                "x": list(np.array(cols)[yl]),
                "y": list(np.array(dfData[index])[yl]),
                "text": index,
                "mode": "markers",
                "marker": {"size":8, "color": color},
                "visible": True if index == 0 else False,
            })

        dataLen = len(data)


        # ADD 3D LINE PLOT
        yStepList = list(np.arange(0, len(dfData)) * scanStep)
        xStepList = list(np.arange(0, len(dfData)) * 0.1)

        for i in range(len(dfData)):
            z = []
            x = []
            for index in range(i):
                yl = ~np.isnan(dfData[i])

                z = list(np.array(dfData[i])[yl])
                x = [-xStepList[index]] * len(list(np.array(dfData[index])[yl]))

            scs = [yStepList[i]] * len(cols)
            #if i < 3: print(np.add(np.float_(cols), scs))
            data.append({"z": z,
                         "x": x,
                         "y": list(np.add(np.float_(cols), scs)),
                         "type": 'scatter3d',
                         "mode": "markers",
                         "scene": "scene1",
                         "visible": True,
                         "marker": {"size": 2, "color": color, "opacity": 0.2,"line": {"color": color}}
                         })


        # ADD SHEET0 TO FILL
        for index in range(len(dfData)):
            data.append({
                "x": list(np.float_(cols)),
                "y": list(map(lambda x: x if (x != float("nan")) and (x < 0) else 0,
                              list(np.float_(dfData[index])))),
                "mode": "lines",
                "line": {"shape": 'spline', "color": color},
                "visible": True if index == 0 else False,
                "fill": "tonexty",
            })

        # ADD SHEET1 TO FILL
        for index in range(len(dfData)):
            data.append({
                "x": list(np.float_(cols)),
                "y": list(map(lambda x: x if (x != float("nan")) and (x < -sheet1) else -sheet1, list(np.float_(dfData[index])))),
                "mode": "lines",
                "line": {"shape": 'spline', "color": color},
                "visible": True if index == 0 else False,
                "fill": "tonexty",
            })
        # ADD GAP TO FILL
        gapLine = -sheet1 - gap
        for index in range(len(dfData)):
            data.append({
                "x": list(np.float_(cols)),
                "y": list(map(lambda x: x if (x != float("nan")) and (x < gapLine) else gapLine, list(np.float_(dfData[index])))),
                "mode": "lines",
                "line": {"shape": 'spline', "color": color},
                "visible": True if index == 0 else False,
            })

        # ADD SHEET2 TO FILL
        sheet2Line = gapLine - sheet2
        for index in range(len(dfData)):
            data.append({
                "x": list(np.float_(cols)),
                "y": list(map(lambda x: x if (x != float("nan")) and (x < sheet2Line) else sheet2Line, list(np.float_(dfData[index])))),
                "mode": "lines",
                "line": {"shape": 'spline', "color": color},
                "visible": True if index == 0 else False,
                "fill": "tonexty",
            })

        sliderSteps = []
        for i in range(dataLen):
            step = dict(
                method="update",
                args=[{"visible": [False] * len(data), "marker": [{}] * len(data)}]
            )

            step["args"][0]["visible"][i] = True
            step["args"][0]["marker"][i] = {"size":8, "color": "red"}
            step["args"][0]["visible"][dataLen: dataLen * 2] = [True] * dataLen
            step["args"][0]["marker"][dataLen: + dataLen] = [{"size": 2, "color": color, "opacity": 0.2,
                                                      "line": {"color": color}}] * dataLen
            step["args"][0]["marker"][i + dataLen] = {"size": 4, "color": "red", "opacity": 0.8,
                                                      "line": {"color": "red"}}
            step["args"][0]["visible"][i + dataLen * 2] = True
            step["args"][0]["visible"][i + dataLen * 3] = True
            step["args"][0]["visible"][i + dataLen * 4] = True
            step["args"][0]["visible"][i + dataLen * 5] = True
            #step["args"][0]["visible"][len(data) - 1] = True

            sliderSteps.append(step)



        layout = dict(
            font={"color": "white"},
            height="600px",
            showlegend=False,
            hovermode= 'closest',
            paper_bgcolor="black",
            plot_bgcolor="black",
            margin={"r":20, "t":20, "b":40, "l":60},
            xaxis={"title": "x TCP [mm]", "showgrid": False, "zeroline": False, "domain": [0,0.5], "range": [xmi,xma]},
            yaxis={"title": "z Depth [mm]", "showgrid": False, "range": [mi,ma], "autorange": False},
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
                camera={"eye": {"x": 1.8, "y": 0, "z": 0}, "center": {"x": 0, "y": -0.2, "z": 0}},
                aspectmode="data",
                xaxis={"showgrid": True, "visible": True, "gridcolor": "grey", "showline": False,
                       "showticklabels": False, "title": {"text": ""}},
                yaxis={"showgrid": False, "scaleanchor": "x", "scaleratio": 1, "visible": False},
                zaxis={"showgrid": False, "scaleanchor": "x", "scaleratio": 1, "visible": False, "range": [mi, -mi]},
            ),
        )


        graph = {
            "layout": layout,
            "data": data,
            "config": {"responsive": True},
        }

        return graph


    ######################## CUSTOM ##############################
    def getFig(self, df, legend, colorList, bL, bX, bR, type):
        data = []
        ci = 0
        li = 0
        bx = bX
        if len(bx) == 0:
            bx = ["index"]

        types = {'line': dict(mode="lines"),
                 'marker': dict(mode="markers"),
                 'line and marker': dict(mode="lines+markers"),
                 'bar': dict(type="bar"),
                 'histogram': dict(type="histogram")}

        for d in df:

            if bx[0] == "index":
                x = list(range(len(d)))
            elif bx[0] != "timestamp":
                x = list(d.loc[:, bx[0]])

            for l in bL:
                color = colorList[ci]
                if bx[0] == "timestamp":
                    lind = list(d.keys()).index(l)
                    print(lind)
                    x = d.iloc[:, lind-1]
                    x = pd.to_datetime(x, unit="us")
                trace1 = dict(
                    x=list(x),
                    y=list(d.loc[:, l]),
                    name=f"{legend[li]} - {l}",
                    mode= "lines+markers",
                    line= {"shape": 'spline', "color": color, "width": 1},
                    marker={"color": color, "size":2, "opacity":0.5},
                    type='scatter',
                )
                trace1.update(types[type[0]])

                data.append(trace1)

                ci = ci + 1

            for r in bR:
                color = colorList[ci]
                if bx[0] == "timestamp":
                    rind = list(d.keys()).index(r)
                    print(rind)
                    x = d.iloc[:, rind-1]
                    x = pd.to_datetime(x, unit="us")
                trace2 = dict(
                    x=list(x),
                    y=list(d.loc[:, r]),
                    name=f"{legend[li]} - {r}",
                    mode= "lines+markers",
                    line= {"shape": 'spline', "color": color, "width": 1},
                    marker={"color": color, "size":2, "opacity":0.5},
                    type='scatter',
                    yaxis="y2",
                )
                trace2.update(types[type[1]])
                data.append(trace2)

                ci = ci + 1
            li = li + 1


        layout = dict(
            font={"color": "white"},
            hovermode='closest',
            paper_bgcolor="black",
            plot_bgcolor="black",
            legend={"orientation": "h", "y": -0.25},
            xaxis={"tickformat": '%s.%f', "title": "Time [s]"} if bx[0] == "timestamp" else {},
            yaxis2={"side": "right", "overlaying": "y"}
        )

        graph = {
            "data": data,
            "layout": layout,
            "config": {"responsive": True},

        }

        return graph



