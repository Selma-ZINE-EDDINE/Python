# filename = 'dash-01.py'

#
# Imports
#
import pandas as pd
import plotly_express as px


df = pd.read_csv('POSITION-TEMP-POP.csv')
fig = px.scatter(df, x='POP.91', y='PIB91', color='PAYS 2000', size='SURFACE', title='Population vs PIB en 1991')
fig.show()



"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

#
# Data
#

data =pd.read_csv('POSITION-TEMP-POP.csv')
data = data.dropna(subset=['PAYS'])
#
# Main
#

if __name__ == '__main__':

    app = dash.Dash(__name__) # (3)

    fig = px.scatter(data, x="PRECIPIT.", y="TEMP.JANV.",
                 size="POP.91", color="PAYS", hover_name="CAPITALE",
                 log_x=True, size_max=60)


    app.layout = html.Div([
    dcc.Graph(
        id='precipitation-exp-vs-temperature',
        figure=fig
    )
    ])

    #
    # RUN APP
    #

    app.run_server(debug=True) # (8)



"""

"""from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

#df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
df=pd.read_csv('POSITION-TEMP-POP.csv')
df = df.dropna(subset=['PAYS'])
fig = px.scatter(df, x="PRECIPIT.", y="TEMP.JANV.",
                 size="POP.91", color="PAYS", hover_name="CAPITALE",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='precipitation-exp-vs-temperature',
        figure=fig
    )
])



if __name__ == '__main__':
    app.run(debug=True)"""