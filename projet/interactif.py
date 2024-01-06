import plotly_express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import graphiques
#from dashboard import app


def interactivite(app):
    """
    Rend interactif le graphique élémentaire.
    L'utilisateur peur sélectionner une année pour tracer le graphique.

    Args:
        app: Le dashboard sur lequel est le graphique élémentaire.
    
    Returns:
        Returns: Le graphique tracé en fonction de l'année choisis par l'utilisateur.
   
    """
    # graphique elementaire
    @app.callback(
        Output(component_id='graph1', component_property='figure'),
        [Input(component_id='year-dropdown', component_property='value')]
    )
    def update_figure(input_value):
        #graphele()[1] = data
        filtered_data = graphiques.graphele()[1][input_value].dropna(subset=['Life expectancy - Sex: all - Age: at birth - Variant: estimates', 'CO2 emissions (metric tons per capita)'])
        return px.scatter(filtered_data, x="CO2 emissions (metric tons per capita)", y="Life expectancy - Sex: all - Age: at birth - Variant: estimates",
                        color="Continent", hover_name="Entity")
    

