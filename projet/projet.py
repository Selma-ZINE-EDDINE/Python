# 1 -Import et definitions des variables globales

from collections import namedtuple
import csv
import decimal
import pandas as pd
import numpy as np
import plotly.graph_objects as go
#import seaborn as sns
import dash
from dash import Dash, dcc, html
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt

from matplotlib import cm

import plotly_express as px
import folium

#import dash_core_components as dcc
#import dash_html_components as html

# 2 -Definition des fonctions secondaires

def read_data_to_dicts(filename):
    data = []
    with open (filename, mode="r", encoding="utf8") as f:
        #for row in f:
        #    data.extend(f)
        data = pd.read_csv(filename)
        f.closed
        return data

def temperatureMoyenne(data,year):
    
    n=data['F'+str(year)]
    return n.mean()


def historigramme(data):
    years = range(1961, 2022,2)
    mean_temps = [temperatureMoyenne(data, year) for year in years]
    color_map = cm.get_cmap('Reds')
    colors = color_map(np.linspace(0, 1, len(years)))

    plt.bar(years, mean_temps, width=2, color=colors, alpha=0.7,edgecolor='black')
    plt.title('\nThe evolution of average temperatures \n in the world depending on the year\n')
    plt.xlabel('Year')
    plt.ylabel('Change in °C from 1951-1980 baseline')
    #plt.style.use('seaborn')
    plt.show()   

def colonne(data, nomColonne):
    return data[nomColonne]

def multicolonne(data,nom1, nom2):
    c= [name for name in data.columns if nom1 or nom2 in name ]
    return data[c]


def obtenir_geojson_pays():
    # Utilisez la bibliothèque GeoPandas pour lire le GeoJSON des frontières des pays
    world = pd.read_json('https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json')
    return world


def obtenir_coordonnees_pays(nom_pays):
    geolocator = Nominatim(user_agent="mon_application")
    location = geolocator.geocode(nom_pays)
    
    if location:
        return location.latitude, location.longitude
    else:
        print(f"Les coordonnées pour le pays '{nom_pays}' n'ont pas pu être trouvées.")
        return None
    
def colorer_pays(nom_pays, couleur,map):
    coords = obtenir_coordonnees_pays(nom_pays)
    
    if coords:
        #map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)
        
        # Ajouter un polygone pour représenter les frontières du pays
        #folium.RegularPolygonMarker(location=coords, fill_color=couleur).add_to(map)
        folium.Marker(location=coords, icon=folium.Icon(color=couleur)).add_to(carte)
        # Sauvegarder la carte dans un fichier HTML
        map.save(outfile=f'map.html')
        
        #print(f"Carte pour {nom_pays} générée avec succès.")
    else:
        print("Impossible de générer la carte.")

def carte():
    coords = (0,0)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=2)
    map.save(outfile='map.html')
    return map

def pays(chaine):
    p = chaine.split()
    return p[0]

def paysPlusChaud(data, map):
    NomPays= colonne(data,"Country")
    coeffAugmentation = colonne(data,"F2022")
    
    for nom_pays, coef in zip(NomPays, coeffAugmentation):
        if coef > 1.5:
            colorer_pays(pays(nom_pays),'red',map)

    
# 3 -Definition du main() qui appellent les fonctions secondaires
def main():
    data = read_data_to_dicts('Annual_Surface_Temperature_Change.csv')   
    #carte_instance = carte()
    #paysPlusChaud(data, carte_instance)
    historigramme(data)
    pass
    #historigramme(data)
# 4 -Appel protégé du main()
if __name__ == '__main__':
    main()
    #app = dash.Dash(__name__)

    #df = pd.read_csv('Annual_Surface_Temperature_Change.csv')

    #fig = px.scatter(df, x="Country", y="F1981",
    #                size="F1981", color="Country", hover_name="Country",
    #                log_x=True, size_max=60)

    #app.layout = html.Div([
    #    dcc.Graph(
    #        id='life-exp-vs-gdp',
    #        figure=fig
    #    )
    #])

    #app.run_server(debug=True)

    
    #dataGeolocalisation = read_data_to_dicts('Annual_Surface_Temperature_Change.csv')
    
