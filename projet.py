# 1 -Import et definitions des variables globales

from collections import namedtuple
import csv
import decimal
import pandas as pd
import numpy as np
import plotly.graph_objects as go
#import seaborn as sns

import matplotlib.pyplot as plt

from matplotlib import cm

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

# 3 -Definition du main() qui appellent les fonctions secondaires
def main():

    data = read_data_to_dicts('Annual_Surface_Temperature_Change.csv')

    #print(temperatureMoyenne(data,2013))
    historigramme(data)
    #print(data)
    #print(colonne(data,"Indicator"))
    #print(read_data_to_dicts('Annual_Surface_Temperature_Change.csv'))
    
    pass

# 4 -Appel protégé du main()
if __name__ == '__main__':
    main()
