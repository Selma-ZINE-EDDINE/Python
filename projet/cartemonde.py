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

### CARTE ###
def carte():

    # Obtenez le chemin du répertoire du script en cours d'exécution
    script_dir = os.path.dirname(__file__)

    coords = (0,0) # 48.7453229,2.5073644
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=2) #zoom 2
    sf = lambda x :{'fillColor':'#E88300', 'fillOpacity':0.5, 'color':'#E84000', 'weight':1, 'opacity':1}

    # Construisez le chemin relatif au fichier GeoJSON
    geojson_path = os.path.join(script_dir, 'countries.geojson')


    folium.GeoJson(
        data=geojson_path,
        name="idf",
        style_function= sf
    ).add_to(map)

    #map.save(outfile='C:\\Users\\zinee\\Desktop\\E3\\cours\\S1\\projet_python\\Nouveau dossier\\Python\\projet\\projetmap.html')
    map.save(outfile=os.path.join(script_dir, 'projetmap.html'))
    return map

def interaction() :
    # Obtenez le chemin du répertoire du script en cours d'exécution
    script_dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))
    pays = df['Country']
    coef = df['F2022']

    df['text']='Country : '+ df['Country'].astype(str)+'Increasment Coefficient '+ df['F2022'].astype(str)

    data = [dict(type='choropleth',autocolorscale=False, locations = df['Country'], z=df['F2022'],
             locationmode='world',text = df['text'], colorscale = 'Viridis', colorbar = dict(title='increasment coeff'))]
    
    layout = dict(title='Increasment coefficient',
              geo = dict(scope='world',projection = dict(type ='world'),
                        showlakes =True,lakecolor='rgb(66,165,245)'))

    plotly.offline.iplot({
    "data": data,
    "layout": layout
    })

    return

def pays(chaine):
    p = chaine.split()
    return p[0]



def carte2() :
    script_dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))
    
    coords = (0,0)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=2)
    # Construisez le chemin relatif au fichier GeoJSON
    geojson_path = os.path.join(script_dir, 'countries.geojson')

    df['text']='Country : '+ df['Country'].astype(str)+'Increasment Coefficient '+ df['F2022'].astype(str)
  
    cp = folium.Choropleth(
        geo_data=geojson_path,                              # geographical data
        name='choropleth',
        data=df,                                  # numerical data
        columns=[pays('Country'), 'F2022'],                     # numerical data key/value pair
        key_on='feature.properties.name',       # geographical property used to establish correspondance with numerical data
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Temperature change coefficient'
    ).add_to(map)
    
    df_indexed = df.set_index('Country')

    for s in cp.geojson.data['features']:

        try:
            
            s['properties']['F2022']=df_indexed.loc[s['properties']['name'],'F2022']
        except KeyError:

            s['properties']['F2022'] = 'error'


    folium.GeoJsonTooltip(['F2022','name']).add_to(cp.geojson)
    folium.LayerControl().add_to(map)

    
    map.save(outfile=os.path.join(script_dir, 'map.html'))

def main() :
    carte2()
    pass

if __name__ == '__main__':
    main()

