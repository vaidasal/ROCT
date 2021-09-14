from fastapi import APIRouter

from plotlyVis import PlotlyVis
import plotly.io as plio

router = APIRouter()

@router.get("/dashboard")
async def makeDashboard():
    print("get")
    pltVis = PlotlyVis()
    fig = pltVis.getFig()
    graph = {
        "data": [
            {"x": [1, 2, 3], "y": [2, 5, 3], "type": 'bar'},
        ],
        "layout": {
                    "plot_bgcolor":"transparent", "paper_bgcolor":"transparent",
                    "title":title,
                   "font": {"color":"white"},
                    "yaxis":yaxis,
                   }
    }
    return graph

title = dict(text = "A Fancy Plot", font = {"color":"white"})
yaxis = dict(
      showgrid = True,
      zeroline = True,
      showline = True,
      gridcolor = '#616161',
      gridwidth = 2,
      zerolinecolor = '#616161',
      zerolinewidth = 2,
      linecolor = '#616161',
      linewidth = 2,
      #title = 'Y-AXIS',
      titlefont = dict(
         #family = 'Arial, sans-serif',
         #size = 18,
         #color = 'lightgrey'
      ),
      #showticklabels = True,
      #tickangle = 45,
      #tickfont = dict(
        #family = 'Old Standard TT, serif',
        #size = 14,
        #color = 'black'),
      #tickmode = 'linear',
      #tick0 = 0.0,
      #dtick = 0.25
    )