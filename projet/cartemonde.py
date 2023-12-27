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


def pays(chaine):
    p = chaine.split()
    return p[0]

def carte() :
    script_dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))
    
    coords = (0,0)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=2)
    # Construisez le chemin relatif au fichier GeoJSON
    geojson_path = os.path.join(script_dir, 'countries.geojson')

    df['text']='Country : '+ df['Country'].astype(str)+'Increasment Coefficient '+ df['F2022'].astype(str)
  
    cp = folium.Choropleth(
        geo_data=geojson_path,                              # geographical data
        name='Temperature change in the world in 2022',
        data=df,                                  # numerical data
        columns=[pays('Country'), 'F2022'],                     # numerical data key/value pair
        key_on='feature.properties.name',       # geographical property used to establish correspondance with numerical data
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Temperature change coefficient in 2022'
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
    carte()
    pass

if __name__ == '__main__':
    main()

