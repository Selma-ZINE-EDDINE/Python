import pandas as pd
import plotly_express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import os

import cartemonde
from cartemonde import carte, carte_plotly

import histogramme


script_dir = os.path.dirname(__file__)
gapminder = pd.read_csv(os.path.join(script_dir,'life-expectancy-at-birth-vs-co-emissions-per-capita.csv'))

gapminder['Continent'] = gapminder.groupby('Entity')['Continent'].transform(lambda x: x.fillna(x.iloc[0]))

years = sorted(gapminder["Year"].unique())
data = {year: gapminder[gapminder["Year"] == year].dropna(subset=['Life expectancy - Sex: all - Age: at birth - Variant: estimates', 'CO2 emissions (metric tons per capita)']) for year in years}

# Initialise the app
app2 = dash.Dash(__name__)


#Constructor
app2.layout = html.Div(children=[
    html.H1(children='Temperature change in the world'),
    html.Div(children=f'''
            The dashboard higlights the temperature change in the world and the consequences  of C02 emissons 
             life expectancy.
        '''),
    #carte
    html.Div(children=[
        html.H2(children='1 - Map of temperature change coefficient in 2022'),
        html.Div(children=f'''
            The map higlights that all countries are concerned by temperature change.
        '''),
        dcc.Graph(
           id='map-graph',
           figure=carte_plotly()  
        )]),  

    #histogramme
     html.Div(children=[
        html.H2(children='2 - Histogram of world increasment coefficient depending of the year'), 
        html.Div(children=f'''
            The histogram shows that the temperature increase faster and faster.
        '''),
        dcc.Graph(
            id='histogramme',
            figure=histogramme.histogramme()
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
                {'label': str(year), 'value': year} for year in years
            ],
            value=2007,
        ),
        dcc.Graph(  #render interactive graph
            id='graph1',
            figure=px.scatter(data[2007], x="CO2 emissions (metric tons per capita)", y="Life expectancy - Sex: all - Age: at birth - Variant: estimates",
                            color="Continent", hover_name="Entity")      
        ),
        
        ]),
    html.Div(children=f'''
            To conclude, despides the consequence of C02 emissions to our life expectancy
             and the consequence of climate change, the pollution and the temperature continue to increase faster and faster
             which increase temperature in the entire world.
        '''),
])

# Add controls to build the interaction
@app2.callback(
    Output(component_id='graph1', component_property='figure'),
    [Input(component_id='year-dropdown', component_property='value')]
)
def update_figure(input_value):
    filtered_data = data[input_value].dropna(subset=['Life expectancy - Sex: all - Age: at birth - Variant: estimates', 'CO2 emissions (metric tons per capita)'])
    return px.scatter(filtered_data, x="CO2 emissions (metric tons per capita)", y="Life expectancy - Sex: all - Age: at birth - Variant: estimates",
                      color="Continent", hover_name="Entity")
def display_map():
    return carte_plotly()



# RUN app2
if __name__ == '__main__':
    app2.run_server(debug=True)


