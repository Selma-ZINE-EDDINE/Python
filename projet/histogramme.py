# 1 -Import et definitions des variables globales
import os
import sys
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
    plt.title('\nThe evolution of average temperatures change \n in the world depending on the year\n')
    plt.xlabel('Year')
    plt.ylabel('Change in °C from 1951-1980 baseline')
    #plt.style.use('seaborn')
    plt.show()   

def colonne(data, nomColonne):
    return data[nomColonne]
    
# 3 -Definition du main() qui appellent les fonctions secondaires
def main():
    # Obtenez le chemin du répertoire du script en cours d'exécution
    script_dir = os.path.dirname(__file__)

    data = read_data_to_dicts(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))   
    historigramme(data)
    pass

# 4 -Appel protégé du main()
if __name__ == '__main__':
    main()

    
