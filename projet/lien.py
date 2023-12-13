"""
@app.callback(
    Output(component_id='graph1', component_property='figure'), # (1)
    [Input(component_id='year-dropdown', component_property='value')] # (2)
)
def update_figure(input_value): # (3)
    return px.scatter(data[input_value], x="gdpPercap", y="lifeExp",
                    color="continent",
                    size="pop",
                    hover_name="country") # (4)

"""