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
    """
    Retourne la lecture du fichier passé en paramètre.

    Args:
        filename: nom du fichier à lire.
    
    Returns:
        data: fichier lu.
   
    """
    data = []
    with open (filename, mode="r", encoding="utf8") as f:
        data = pd.read_csv(filename)
        f.closed
        return data
    
def temperatureMoyenne(data,year):
    """
    Retourne la température moyenne mondiale sur l'année 'year' de 'data'

    Args:
        data: Fichier dans lequel on récupère les données
        year: Année durant laquelle on calcule la température moyenne
    
    Returns:
        n.mean(): Moyenne de la température mondiale sur une année
   
    """
    
    n=data['F'+str(year)]
    return n.mean()

def match_name(chaine):
    """
    Retourne le nom du pays correspondant au fichier geojson

    Args:
        chaine: pays dont on veut savoir le nom correspondant à celui utilisé dans le fichier geojson
    
    Returns:
        String: Nom du pays selon le fichier geojson
   
    """
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
    elif "China, P.R.: Mainland" in chaine:
        return "China"
    elif "United States"==chaine:
        return "United States of America"
    else:
        return chaine
    


def mappe(x, state_id_map):
    """
    Mappe les noms des pays aux noms compatibles du geojson.
    Ainsi, les pays nons retrouvés dans le fichier geojson sont ignorés sans faire
    buggé le code.

    Args:
        x: Contient le nom d'un pays selon le fichier csv
        state_id_map: Contient les noms de pays selon le fichier geojson
    
    Returns:
        state_id_map.get(x,None): Ajoute dans state_id_map le nom du pays x si il existe dans le fichier
        geojson.
   
    """
    return state_id_map.get(x, None)

# 3 - Definition des fonctions principales

#### HISTOGRAMME ####
def histogramme():
    """
    Trace un histogramme de la température moyenne mondiale en fonction de différentes années.

    Returns:
        fig: l'histogramme tracé.
   
    """
    script_dir = os.path.dirname(__file__) #permet au compilateur de chercher le fichier dans le dossier où se trouve le programme
    data = read_data_to_dicts(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))
    
    years = range(1961, 2022)
    mean_temps = [temperatureMoyenne(data, year) for year in years] 
    nb = len(data) #nb = nb de bars = nb de ligne dans la dataframe

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
    """
    Dessine une carte du monde mettant en valeur le coefficient d'augmentation de la température pour les pays.
    
    Returns:
        fig: Carte du monde mettant en valeur le coefficient d'augmentation de la température pour les pays.
   
    """
    pio.renderers.default = 'browser' #carte lisible sur Internet
    script_dir = os.path.dirname(__file__) #permet au compilateur de chercher le fichier dans le dossier où se trouve le programme

    df = pd.read_csv(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))  

    geo = json.load(open(os.path.join(script_dir, 'countries.geojson'),"r"))
    

    state_id_map = {} #servira à mapper les noms des pays à ceux de la dataframe
    for feature in geo["features"]:
        feature["id"] = feature["properties"]["name"] #ajoute id qui est la cle associé aux noms des pays du geojson
        state_id_map[feature["properties"]["name"]]=feature["id"] #lie la cle au nom du pays

    #apply(match_name) permet de convertir les noms des pays df à ceux correspondant  dans geo
    #apply(lambda x: mappe(x, state_id_map)) permet d'éviter les bugs pour les noms des pays que match_name n'a pas permis de renommer tel que dans geo
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

#### GRAPHIQUE ELEMENTAIRE ####
def graphele():
    """
    Trace un graphique elementaire interactif de l'espérance de vie en fonction de l'émission de CO2 et de l'année.
    
    Returns:
        fig: Le graphique elementaire interactif tracé.
        data: Les données utilisées pour tracer le graphique.
        years: Les années du graphique (permettra de choisir une année pour tracer le graphique)
   
    """

    script_dir = os.path.dirname(__file__)
    gapminder = pd.read_csv(os.path.join(script_dir,'life-expectancy-at-birth-vs-co-emissions-per-capita.csv'))

    gapminder['Continent'] = gapminder.groupby('Entity')['Continent'].transform(lambda x: x.fillna(x.iloc[0]))

    years = sorted(gapminder["Year"].unique())
    data = {year: gapminder[gapminder["Year"] == year].dropna(subset=['Life expectancy - Sex: all - Age: at birth - Variant: estimates', 'CO2 emissions (metric tons per capita)']) for year in years}
    fig = px.scatter(data[2007], x="CO2 emissions (metric tons per capita)", 
                    y="Life expectancy - Sex: all - Age: at birth - Variant: estimates",
                    color="Continent", hover_name="Entity")  
    
    return fig, data, years