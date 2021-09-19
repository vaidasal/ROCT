from fastapi import APIRouter

from plotlyVis import PlotlyVis
import plotly.io as plio

router = APIRouter()

@router.get("/dashboard")
async def makeDashboard():
    print("get")
    pltVis = PlotlyVis()
    figHeat = pltVis.getHeatFig()
    figHeat["layout"].update(dict(font= {"color": "white"},))

    figSlideLine = pltVis.getSlideLine()
    figSlideLine["layout"].update(dict(font={"color": "white"}, ))

    return (figHeat,figSlideLine)



title = dict(text = "Keyholeshape", font = {"color":"white"})
yaxis = dict(
      showgrid = False,
      zeroline = False,
      showline = False,
      gridcolor = '#616161',
      gridwidth = 1,
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