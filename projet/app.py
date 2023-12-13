
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

#df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
df=pd.read_csv('API_EN.ATM.CO2E.KT_DS2_fr_csv_v2_6236535=csv')
df = df.dropna(subset=['Émissions de CO2'])
fig = px.scatter(df, x="Émissions de CO2", y="Indicator Code",
                 size="Indicator Name", color="Country Code", hover_name="Country Name",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)