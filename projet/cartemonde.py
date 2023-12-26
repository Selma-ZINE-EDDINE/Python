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


### GEOVIEWS ###
#initialise geoviews
gv.extension('bokeh')

#description geometrique de differentes regions et frontières des pays
(gf.land * gf.ocean * gf.borders).opts(
    'Feature', 
    projection=crs.Mercator(), 
    global_extent=True, 
    width=500
)

### GEOJSON ###

#POUR TELECHARGER FAIS ATTENTION A BIEN ENTRER DANS LE DOC5 afficher le fichier ) ET TELECHARGER. Compare avec les fichiers qui fonctionne pour comparer si pbs, FERMER LE FICHIER AVANT EXECUTION
sf = gpd.read_file("C:\\Users\\zinee\\Desktop\\E3\\cours\\S1\\test_pour_projet-python\\departements-version-simplifiee.geojson")

#print(sf.head())
sf.loc[0].geometry #recupère le département grâce à ses frontières

#numpy engendre un tableau d'entier entre 1 et 10, on crée une colonnue value et conserve les frontières du département grâce à shape[0]
sf['value'] = np.random.randint(1, 10, sf.shape[0])

### GEOVIEWS ###
deps = gv.Polygons(sf, vdims=['nom','value'])


deps.opts(width=600, height=600, toolbar='above', color=dim('value'),
          colorbar=True, tools=['hover'], aspect='equal')

### CARTE ###
def carte():
    coords = (0,0) # 48.7453229,2.5073644
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=2) #zoom 2
    sf = lambda x :{'fillColor':'#E88300', 'fillOpacity':0.5, 'color':'#E84000', 'weight':1, 'opacity':1}

    folium.GeoJson(
        data="C:\\Users\\zinee\\Desktop\\E3\\cours\\S1\\test_pour_projet-python\\countries.geojson",
        name="idf",
        style_function= sf
    ).add_to(map)

    map.save(outfile='C:\\Users\\zinee\\Desktop\\E3\\cours\\S1\\test_pour_projet-python\\map.html')
    return map

### Créez une carte choroplèthe avec vos propres données ###
#df = pd.read_csv('C:\\Users\\zinee\\Desktop\\E3\\cours\\S1\\test_pour_projet-python\\population_france_departements_2019.tsv', sep='\t', thousands=',')
#print(df.head())




def main() :
    #sf = gpd.read_file("C:\\Users\\zinee\\Desktop\\E3\\cours\\S1\\test_pour_projet-python\\departements-version-simplifiee.geojson")
    #carte_instance = carte("C:\\Users\\zinee\\Desktop\\E3\\cours\\S1\\test_pour_projet-python\\world.geojson")
    #sf = gpd.read_file("C:\\Users\\zinee\\Desktop\\E3\\cours\\S1\\test_pour_projet-python\\world.geojson")
    carte()
    pass

if __name__ == '__main__':
    main()


#jf = sf.merge(df, left_on='code', right_on='depcode', suffixes=('','_y'))
#print(jf.head(2))
# declare how the plot should be done

#regions = gv.Polygons(jf, vdims=['nom', 't_total', 'h_total', 'f_total'])
#regions.opts(width=600, height=600, toolbar='above', color=dim('t_total')/1e6, 
             #colorbar=True, tools=['hover'], aspect='equal')