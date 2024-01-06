'''
Génère un dashboard présentant des graphiques montrant
l'impact négatif de la pollution dans le monde.
'''
# 1 -Import et definitions des variables globales
import dash
from dash import dcc
from dash import html
import graphiques
from interactif import interactivite


# 2 - Initialise the app
app = dash.Dash(__name__)


# 3 - Constructor
app.layout = html.Div(children=[
    html.H1(children='Temperature change in the world'),
    html.Div(children='''
            The dashboard higlights the consequences of pollution. It shows the temperature change and the impact of carbon emission.
        '''),
    # carte
    html.Div(children=[
        html.H2(children='1 - Map of temperature coefficient change in 2022'),
        html.Div(children='''
            The map higlights that almost all countries are concerned by temperature change.
        '''),
        dcc.Graph(
           id='map-graph',
           figure=graphiques.carte(),
           style={"height": 700}
        )]),

    # histogramme
     html.Div(children=[
        html.H2(children='2 - Histogram of world increasment coefficient depending of the year'),
        html.Div(children='''
            The histogram shows that the temperature increase faster and faster.
        '''),
        dcc.Graph(
            id='histogramme',
            figure=graphiques.histogramme()
        )]),

    # graphique élémentaire
    html.Div([
        html.H2(children='3 - Relationship between C02 emissions and life expectancy'),
        html.Div(children='''
            The graph above shows the relationship between C02 emissions and
            life expectancy.
        '''),
        html.Label('Year'),
        dcc.Dropdown(
            id="year-dropdown",
            options=[
                {'label': str(year), 'value': year} for year in
                graphiques.graphele()[2]#graphele()[2] = years
            ],
            value=2007,
        ),
        dcc.Graph(  # render interactive graph
            id='graph1',
            figure=graphiques.graphele()[0]     #graphele()[0] = fig
        ),
        ]),
    html.Div(children='''
             To conclude, year by year, the temperature increase faster and faster in the entire world.
             Moreover, the CO2 emission reduce our life expectancy. So, government must put in place
             strict rules to protect our life and our planet.
        '''),
])

# 4 - Add controls to build the interaction
interactivite(app)

#5 - RUN app
if __name__ == '__main__':
    app.run_server(debug=True)
