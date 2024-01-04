# 1 -Import et definitions des variables globales
import os
import pandas as pd
import plotly_express as px
import pandas as pd
import plotly.express as px
import json
import plotly.io as pio

# 2 -Definition des fonctions secondaires

def read_data_to_dicts(filename):
    data = []
    with open (filename, mode="r", encoding="utf8") as f:
        data = pd.read_csv(filename)
        f.closed
        return data
    
def temperatureMoyenne(data,year):
    
    n=data['F'+str(year)]
    return n.mean()

def match_name(chaine):
    if "Russian" in chaine:
        return "Russian"
    elif "Costa Rica" in chaine:
        return "Costa Rica"
    elif "Venezuela" in chaine:
        return "Venezuela"
    elif "Dominican Republic" in chaine:
        return "Dominican Republic"
    elif "Mauritania" in chaine:
        return "Mauritania"
    elif "Ivory" in chaine:
        return "Ivory Coast"
    elif "Central African" in chaine:
        return "Central African Republic"
    elif "Congo, Dem" in chaine:
        return "Democratic Republic of the Congo"
    elif "Tanzania" in chaine:
        return "United Republic of Tanzania"
    elif "South Sudan" in chaine:
        return "South Sudan"
    elif "Ethiopia" in chaine:
        return "Ethiopia"
    elif "Mozambique" in chaine:
        return "Mozambique"
    elif "Madagascar" in chaine:
        return "Madagascar"
    elif "Egypt" in chaine:
        return "Egypt"
    elif "Congo, Rep" in chaine:
        return "Republic of the Congo"
    elif "Ethiopia" in chaine:
        return "Ethiopia"
    elif "Kazakhstan" in chaine:
        return "Kazakhstan"
    elif "Yemen" in chaine:
        return "Yemen"
    elif "Korea, Dem" in chaine:
        return "North Korea"
    elif "Korea, Rep" in chaine:
        return "South Korea"
    elif "Netherlands, The" in chaine:
        return "Netherlands"
    elif "Poland" in chaine:
        return "Poland"
    elif "Belarus" in chaine:
        return "Belarus"
    elif "Estonia" in chaine:
        return "Estonia"
    elif "Czech" in chaine:
        return "Czech Republic"
    elif "Slovenia" in chaine:
        return "Slovenia"
    elif "Croatia" in chaine:
        return "Croatia"
    elif "Iran" in chaine:
        return "Iran"
    elif "Afghanistan" in chaine:
        return "Afghanistan"
    elif "Uzbekistan" in chaine:
        return "Uzbekistan"
    elif "Serbia" in chaine:
        return "Serbia"
    elif "Macedonia" in chaine:
        return "Macedonia"
    elif "Moldova" in chaine:
        return "Moldova"
    elif "Kyrgy" in chaine:
        return "Kyrgysztan"
    elif "Syria" in chaine:
        return "Syria"
    else:
        return chaine
    
def mappe(x, state_id_map):
    # Fonction pour mapper les noms des pays aux noms compatibles du geojson
    return state_id_map.get(x, None)

# 3 - Definition des fonctions principales

#### HISTOGRAMME ####
def histogramme():
    script_dir = os.path.dirname(__file__)
    data = read_data_to_dicts(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))
    
    years = range(1961, 2022)
    mean_temps = [temperatureMoyenne(data, year) for year in years] 
    nb = len(data) #nb de bars = nb de ligne dans la dataframe

    fig = px.histogram(data,
                       x=years,
                       y=mean_temps, 
                       nbins=nb,
                       barmode='relative',
                       labels={'x':'years','y':'world increasment coefficient'},
                       opacity=0.8,
                       log_y=True,
                       color = years
                       )
    
    fig.update_layout( yaxis_title="world increasment coefficient" ) #pour ne pas avoir "sum of ..."
    return fig

#### CARTE ####
def carte():
    pio.renderers.default = 'browser'
    script_dir = os.path.dirname(__file__)

    df = pd.read_csv(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))  

    geo = json.load(open(os.path.join(script_dir, 'countries.geojson'),"r"))
    

    state_id_map = {} #servira à mapper les noms des pays à ceux de la dataframe
    for feature in geo["features"]:
        feature["id"] = feature["properties"]["name"] #ajoute id qui est la cle associé aux noms des pays du geojson
        state_id_map[feature["properties"]["name"]]=feature["id"] #lie la cle au nom du pays

    df['Compatible_Country'] = df['Country'].apply(match_name).apply(lambda x: mappe(x, state_id_map))

    # Filtrer les lignes où Compatible_Country est None (pays non reconnu)
    df = df[df['Compatible_Country'].notna()]

    # Ajouter l'ID uniquement pour les pays reconnus
    df['id'] = df["Compatible_Country"].apply(lambda x: state_id_map[x])

    fig=px.choropleth(
        df,
        locations='id',
        geojson=geo,                                                                          
        color='F2022',                         
    )

    return fig