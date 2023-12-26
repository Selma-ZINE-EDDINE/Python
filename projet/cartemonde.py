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


def main() :
    carte()
    pass

if __name__ == '__main__':
    main()

