import plotly_express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import graphiques
import interactif
from interactif import interactivite

# Initialise the app
app = dash.Dash(__name__)


#Constructor
app.layout = html.Div(children=[
    html.H1(children='Temperature change in the world'),
    html.Div(children=f'''
            The dashboard higlights the consequences of pollution. It shows the temperature change and the impact of carbon emission.
        '''),
    #carte
    html.Div(children=[
        html.H2(children='1 - Map of temperature change coefficient in 2022'),
        html.Div(children=f'''
            The map higlights that all countries are concerned by temperature change.
        '''),
        dcc.Graph(
           id='map-graph',
           figure=graphiques.carte()  
        )]),  

    #histogramme
     html.Div(children=[
        html.H2(children='2 - Histogram of world increasment coefficient depending of the year'), 
        html.Div(children=f'''
            The histogram shows that the temperature increase faster and faster.
        '''),
        dcc.Graph(
            id='histogramme',
            figure=graphiques.histogramme()
        )]),  

    #graphique élémentaire
    html.Div([
        html.H2(children='3 - Relationship between C02 emissions and life expectancy'),
        html.Div(children=f'''
            The graph above shows the relationship between C02 emissions and
            life expectancy.
        '''),
        html.Label('Year'),
        dcc.Dropdown(
            id="year-dropdown",
            options=[
                {'label': str(year), 'value': year} for year in graphiques.graphele()[2] #graphele()[2] = years
            ],
            value=2007,
        ),
        dcc.Graph(  #render interactive graph
            id='graph1',
            figure=graphiques.graphele()[0]     #graphele()[0] = fig
        ),
        
        ]),
    html.Div(children=f'''
             To conclude, year by year, the temperature increase faster and faster in the entire world.
             Moreover, the CO2 emission reduce our life expectancy. So, government must put in place
             strict rules to protect our life and our planet.
        '''),
])

# Add controls to build the interaction
interactivite(app)


# RUN app2
if __name__ == '__main__':
    app.run_server(debug=True)


