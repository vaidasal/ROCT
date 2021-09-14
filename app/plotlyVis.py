import plotly.express as px

class PlotlyVis:

    dataframe = px.data.gapminder().rename(columns={
        'year': 'Year',
        'lifeExp': 'Life Expectancy',
        'pop': 'Population',
        'gdpPercap': 'GDP Per Capita'
    })

    def getFig(self):
        country = 'United States'
        metric = 'Population'
        subset = self.dataframe[self.dataframe.country == country]
        fig = px.line(subset, x='Year', y=metric, title=f'{metric} in {country}')
        return fig