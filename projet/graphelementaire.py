import pandas as pd
import plotly_express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import os




# Main
app2 = dash.Dash(__name__)
script_dir = os.path.dirname(__file__)
gapminder = pd.read_csv(os.path.join(script_dir,'life-expectancy-at-birth-vs-co-emissions-per-capita.csv'))

gapminder['Continent'] = gapminder.groupby('Entity')['Continent'].transform(lambda x: x.fillna(x.iloc[0]))

years = sorted(gapminder["Year"].unique())
data = {year: gapminder[gapminder["Year"] == year].dropna(subset=['Life expectancy - Sex: all - Age: at birth - Variant: estimates', 'CO2 emissions (metric tons per capita)']) for year in years}


def graphele():

    layout = html.Div(children=[
        html.Label('Year'),
        dcc.Dropdown(
            id="year-dropdown",
            options=[
                {'label': str(year), 'value': year} for year in years
            ],
            value=2007,
        ),
        dcc.Graph(
            id='graph1',
            figure=px.scatter(data[2007], x="CO2 emissions (metric tons per capita)", y="Life expectancy - Sex: all - Age: at birth - Variant: estimates",
                            color="Continent", hover_name="Entity")
        ),
        html.Div(children=f'''
            The graph above shows the relationship between GDP per capita and
            life expectancy.
        '''),
    ])

    return layout

    
@app2.callback(
        Output(component_id='graph1', component_property='figure'),
        [Input(component_id='year-dropdown', component_property='value')]
    )   

def update_figure(input_value):
    filtered_data = data[input_value].dropna(subset=['Life expectancy - Sex: all - Age: at birth - Variant: estimates', 'CO2 emissions (metric tons per capita)'])
    return px.scatter(filtered_data, x="CO2 emissions (metric tons per capita)", y="Life expectancy - Sex: all - Age: at birth - Variant: estimates",
                      color="Continent", hover_name="Entity")



# RUN app2
if __name__ == '__main__':
    app2.run_server(debug=True)

def graph():
    app2.run_server(debug=True)