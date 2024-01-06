# 1 -Import et definitions des variables globales
import plotly_express as px
from dash.dependencies import Input, Output
import graphiques


# 3 - Definition des fonctions principales
def interactivite(app):
    """
    Rend interactif le dashboard passé en paramètre.

    Args:
        app: Dashboard rendu interactif.
    
    """
    # graphique elementaire
    @app.callback(
        Output(component_id='graph1', component_property='figure'),
        [Input(component_id='year-dropdown', component_property='value')]
    )
    def update_figure(input_value):
        """
        Retrace le graphique élémentaire selon l'année sélectionnée par l'utilisateur.

        Args:
            input_value: Valeur (année) sélectionné par l'utilisateur.
        
        Returns:
            Returns: Le graphique tracé en fonction de l'année choisis par l'utilisateur.
    
        """
        #graphele()[1] = data
        filtered_data = graphiques.graphele()[1][input_value].dropna(subset=['Life expectancy - Sex: all - Age: at birth - Variant: estimates', 'CO2 emissions (metric tons per capita)'])
        return px.scatter(filtered_data, x="CO2 emissions (metric tons per capita)", y="Life expectancy - Sex: all - Age: at birth - Variant: estimates",
                        color="Continent", hover_name="Entity")
    

