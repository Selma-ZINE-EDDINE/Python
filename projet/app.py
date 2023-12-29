import pandas as pd
import plotly_express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


gapminder = pd.read_csv('co2-emissions-vs-gdp.csv')


years = sorted(gapminder["Year"].unique())
data = {year: gapminder[gapminder["Year"] == year].dropna(subset=['Population (historical estimates)', 'GDP per capita']) for year in years}

# Main
app = dash.Dash(__name__)

app.layout = html.Div(children=[
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
        figure=px.scatter(data[2007], x="GDP per capita", y="Annual CO₂ emissions (per capita)",
                          color="Entity", size="Population (historical estimates)", hover_name="Entity",size_max=100)
    ),
    html.Div(children=f'''
        The graph above shows the relationship between GDP per capita and
        Annual CO₂ emissions for the year 2007.
    '''),
])

@app.callback(
    Output(component_id='graph1', component_property='figure'),
    [Input(component_id='year-dropdown', component_property='value')]
)
def update_figure(input_value):
    filtered_data = data[input_value].dropna(subset=['Population (historical estimates)', 'GDP per capita'])
    return px.scatter(filtered_data, x="GDP per capita", y="Annual CO₂ emissions (per capita)",
                      color="Entity", size="Population (historical estimates)", hover_name="Entity",size_max=100)

# RUN APP
if __name__ == '__main__':
    app.run_server(debug=True)


"""import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Charger les données
df = pd.read_csv('co2-emissions-vs-gdp.csv')  # Remplacez 'votre_fichier.csv' par le chemin de votre fichier CSV

# Années disponibles dans les données
available_years = sorted(df['Year'].unique())

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Mise en page du tableau de bord
app.layout = html.Div(children=[
    html.H1(children='Dashboard avec les données fournies'),

    dcc.Slider(
        id='Year-slider',
        #min=min(available_years),
        min = 2000,
        max=max(available_years),
        step=1,
        value=min(available_years),
        marks={str(Year): str(Year) for Year in available_years}
    ),

    dcc.Graph(
        id='scatter-plot'
    )
])

# Callback pour mettre à jour le graphique en fonction de la valeur du curseur
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('Year-slider', 'value')]
)
def update_scatter_plot(selected_year):
    filtered_df = df[df['Year'] == selected_year]
    fig = px.scatter(filtered_df, x='GDP per capita', y='Annual CO₂ emissions (per capita)',
                     color='Continent', size='Population (historical estimates)',
                     hover_name='Entity', title=f'Scatter Plot ({selected_year})')
    return fig

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)

"""

"""
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

df = pd.read_csv('co2-emissions-vs-gdp.csv')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='Year-slider',
        min=2000,
        max=df['Year'].max(),
        step=None,
        value=2000,
        marks={str(Year): str(Year) for Year in df['Year'].unique()}
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('Year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df['Year'] == selected_year]

    fig = px.scatter(filtered_df, x="GDP per capita", y="Annual CO₂ emissions (per capita)",
                     size="Population (historical estimates)", color="Entity", hover_name="Entity")

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
"""