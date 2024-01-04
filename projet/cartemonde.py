import geopandas as gpd
import os
import sys
import numpy as np
import geoviews as gv
import geoviews.feature as gf
import xarray as xr
from cartopy import crs
from geoviews import dim
import pandas as pd
import folium
import plotly.express as px
import plotly
import plotly.graph_objects as go
import json
import plotly.io as pio

def pays(chaine):
    p = chaine.split()
    return p[0]

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


def compatible_F2022(chaine):
    if "China" in chaine:
        return
    return

def carte() :
    script_dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))
    
    coords = (0,0)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=2)
    # Construisez le chemin relatif au fichier GeoJSON
    geojson_path = os.path.join(script_dir, 'countries.geojson')

    df['text']='Country : '+ df['Country'].astype(str)+'Increasment Coefficient '+ df['F2022'].astype(str)
    #df['Compatible_Country']
    df['Compatible_Country']=df['Country'].apply(match_name)

    aggregated_df = df.groupby('Compatible_Country', as_index=False)['F2022'].sum()

    cp = folium.Choropleth(
        geo_data=geojson_path,                              # geographical data
        name='Temperature change in the world in 2022',
        data=df,                                  # numerical data
        columns=['Compatible_Country', 'F2022'],                     # numerical data key/value pair
        key_on='feature.properties.name',       # geographical property used to establish correspondance with numerical data
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Temperature change coefficient in 2022'
    ).add_to(map)
    
    df_indexed = df.set_index('Compatible_Country')

    for s in cp.geojson.data['features']:
        try:            
            s['properties']['F2022']=df_indexed.loc[s['properties']['name'],'F2022']
        except KeyError:
            s['properties']['F2022'] = 'error'


    folium.GeoJsonTooltip(['F2022','name']).add_to(cp.geojson)
    folium.LayerControl().add_to(map)

    
    map.save(outfile=os.path.join(script_dir, 'map.html'))
    return map

def carte_monde() :
    script_dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))
    
    coords = (0,0)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=2)
    # Construisez le chemin relatif au fichier GeoJSON
    geojson_path = os.path.join(script_dir, 'countries.geojson')

    df['text']='Country : '+ df['Country'].astype(str)+'Increasment Coefficient '+ df['F2022'].astype(str)
    #df['Compatible_Country']
    df['Compatible_Country']=df['Country'].apply(match_name)


    fig=go.Figure()
    fig=px.choropleth(
        df,
        geojson=geojson_path,                                                                
        locations=df['Compatible_Country'],                     
        key_on='feature.properties.name',       
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Temperature change coefficient in 2022'
    ).add_to(map)
    
    df_indexed = df.set_index('Compatible_Country')

    for s in fig.geojson.data['features']:
        try:            
            s['properties']['F2022']=df_indexed.loc[s['properties']['name'],'F2022']
        except KeyError:
            s['properties']['F2022'] = 'error'


    folium.GeoJsonTooltip(['F2022','name']).add_to(fig.geojson)
    folium.LayerControl().add_to(map)

    
    map.save(outfile=os.path.join(script_dir, 'map.html'))
    return fig

def carte_plotly():
    script_dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(script_dir, 'Annual_Surface_Temperature_Change.csv'))
    
    # Construisez le chemin relatif au fichier GeoJSON
    geojson_path = os.path.join(script_dir, 'countries.geojson')

    df['text'] = 'Country : ' + df['Country'].astype(str) + 'Increasment Coefficient ' + df['F2022'].astype(str)
    df['Compatible_Country'] = df['Country'].apply(match_name)


    fig = go.Figure()

    fig.add_choropleth(
        geojson=geojson_path,
        locations=df['Compatible_Country'],
        z=df['F2022'],
        colorscale='YlGn',
        colorbar_title='Temperature change coefficient in 2022',
        featureidkey='feature.properties.name',
        text=df['text'],
        hoverinfo='location+text',
    )
    fig.update_layout(
        geo_scope='world'
    )

    return fig

def mappe(x, state_id_map):
    # Fonction pour mapper les noms des pays aux noms compatibles du geojson
    return state_id_map.get(x, None)

def carte_essaie():
    pio.renderers.default = 'browser'
    script_dir = os.path.dirname(__file__)

    df = pd.read_csv(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))  
    #geojson_path = os.path.join(script_dir, 'countries.geojson')

    geo = json.load(open(os.path.join(script_dir, 'countries.geojson'),"r"))
    

    state_id_map = {} #servira à mapper les noms des pays à ceux de la dataframe
    for feature in geo["features"]:
        feature["id"] = feature["properties"]["name"] #ajoute id qui est la cle associé aux noms des pays du geojson
        state_id_map[feature["properties"]["name"]]=feature["id"] #lie la cle au nom du pays

    df['Compatible_Country'] = df['Country'].apply(match_name).apply(lambda x: mappe(x, state_id_map))

    #df["F2022"] = df["F2022"].apply(lambda x: x.replace(",", ""))


    #df['id']=df["Compatible_Country"].apply(lambda x: state_id_map[x]) #lie la cle au nom compatible du pays

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
    #fig.show()
    return fig

def main() :
    carte_essaie()
    pass

if __name__ == '__main__':
    main()

