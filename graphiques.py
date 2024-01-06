'''
Definis un histogramme, une carte du monde et un graphique élémentaire traçable sur un dashboard.
'''
# 1 -Import et definitions des variables globales
import os
import json
import pandas as pd
import plotly_express as px
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

def temperature_moyenne(data,year):
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
        chaine: pays dont on veut savoir le nom correspondant
        à celui utilisé dans le fichier geojson
    
    Returns:
        String: Nom du pays selon le fichier geojson
   
    """
    if "Russian" in chaine:
        return "Russian"
    if "Costa Rica" in chaine:
        return "Costa Rica"
    if "Venezuela" in chaine:
        return "Venezuela"
    if "Dominican Republic" in chaine:
        return "Dominican Republic"
    if "Mauritania" in chaine:
        return "Mauritania"
    if "Ivory" in chaine:
        return "Ivory Coast"
    if "Central African" in chaine:
        return "Central African Republic"
    if "Congo, Dem" in chaine:
        return "Democratic Republic of the Congo"
    if "Tanzania" in chaine:
        return "United Republic of Tanzania"
    if "South Sudan" in chaine:
        return "South Sudan"
    if "Ethiopia" in chaine:
        return "Ethiopia"
    if "Mozambique" in chaine:
        return "Mozambique"
    if "Madagascar" in chaine:
        return "Madagascar"
    if "Egypt" in chaine:
        return "Egypt"
    if "Congo, Rep" in chaine:
        return "Republic of the Congo"
    if "Ethiopia" in chaine:
        return "Ethiopia"
    if "Kazakhstan" in chaine:
        return "Kazakhstan"
    if "Yemen" in chaine:
        return "Yemen"
    if "Korea, Dem" in chaine:
        return "North Korea"
    if "Korea, Rep" in chaine:
        return "South Korea"
    if "Netherlands, The" in chaine:
        return "Netherlands"
    if "Poland" in chaine:
        return "Poland"
    if "Belarus" in chaine:
        return "Belarus"
    if "Estonia" in chaine:
        return "Estonia"
    if "Czech" in chaine:
        return "Czech Republic"
    if "Slovenia" in chaine:
        return "Slovenia"
    if "Croatia" in chaine:
        return "Croatia"
    if "Iran" in chaine:
        return "Iran"
    if "Afghanistan" in chaine:
        return "Afghanistan"
    if "Uzbekistan" in chaine:
        return "Uzbekistan"
    if "Serbia" in chaine:
        return "Serbia"
    if "Macedonia" in chaine:
        return "Macedonia"
    if "Moldova" in chaine:
        return "Moldova"
    if "Kyrgy" in chaine:
        return "Kyrgysztan"
    if "Syria" in chaine:
        return "Syria"
    if "China, P.R.: Mainland" in chaine:
        return "China"
    if "United States"==chaine:
        return "United States of America"
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
        state_id_map.get(x,None): Ajoute dans state_id_map le
        nom du pays x si il existe dans le fichier
        geojson.
   
    """
    return state_id_map.get(x, None)

def couleurs(temp):
    '''
    Retourne la catégorie dans laquelle se trouve la tempéarature
    passé en paramètre.

    Args:
        temp: température dont on veut la catégorie.
    
    Returns:
        String: Catégorie de la température.
    '''
    if temp<0:
        return 'coefficient < 0'
    if temp>=0 and temp<1:
        return '0 < coefficient < 1'
    return '1 < coefficient'

# 3 - Definition des fonctions principales

#### HISTOGRAMME ####
def histogramme():
    """
    Trace un histogramme de la température moyenne mondiale
    en fonction de différentes années.

    Returns:
        fig: l'histogramme tracé.

    """
    script_dir = os.path.dirname(__file__)#permet au compilateur de
    #chercher le fichier dans le dossier où se trouve le programme
    data = read_data_to_dicts(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))

    years = range(1962, 2022)
    nb = len(data) #nb = nb de bars = nb de ligne dans la dataframe

    # Liste des couleurs en fonction des températures moyennes pour chaque année
    colores = [couleurs(temperature_moyenne(data, year)) for year in range(1962, 2022)]
    mean_temp_abs=[abs(temperature_moyenne(data, year)) for year in years]

    fig = px.histogram(data,
                       x=years,
                       y=mean_temp_abs,
                       nbins=nb,
                       barmode='relative',
                       labels={'x':'years','y':'world increasment coefficient'},
                       opacity=0.8,
                       log_y=True,
                       color=colores,
                       color_discrete_map = {'coefficient < 0':'blue',
                                            '0 < coefficient < 1':'orange',
                                            '1 < coefficient':'red'},
                        title="Histogram of world increasment coefficient depending of the year",
                       )

    fig.update_layout( yaxis_title="world increasment coefficient" )#pour ne pas avoir "sum of ..."
    return fig

#### CARTE ####
def carte():
    """
    Dessine une carte du monde mettant en valeur le coefficient
    d'augmentation de la température pour les pays.
    
    Returns:
        fig: Carte du monde mettant en valeur le coefficient
        d'augmentation de la température pour les pays.

    """
    pio.renderers.default = 'browser'#carte lisible sur Internet
    script_dir = os.path.dirname(__file__)#permet au compilateur de chercher
    #le fichier dans le dossier où se trouve le programme


    df = read_data_to_dicts(os.path.join(script_dir,'Annual_Surface_Temperature_Change.csv'))
    geo = json.load(open(os.path.join(script_dir, 'countries.geojson'),"r"))

    state_id_map = {}#servira à mapper les noms des pays à ceux
    #de la dataframe
    for feature in geo["features"]:
        feature["id"] = feature["properties"]["name"] #ajoute id qui est
        #la cle associé aux noms des pays du geojson
        state_id_map[feature["properties"]["name"]]=feature["id"] #lie la
        #cle au nom du pays

    #apply(match_name) permet de convertir les noms des pays df à
    #ceux correspondant  dans geo
    #apply(lambda x: mappe(x, state_id_map)) permet d'éviter
    #les bugs pour les noms des pays que match_name n'a pas permis
    #de renommer tel que dans geo
    df['Compatible_Country']=df['Country'].apply(match_name).apply(lambda x:mappe(x, state_id_map))

    # Filtrer les lignes où Compatible_Country est None (pays non reconnu)
    df = df[df['Compatible_Country'].notna()]

    # Ajouter l'ID uniquement pour les pays reconnus
    df['id'] = df["Compatible_Country"].apply(lambda x: state_id_map[x])

    fig=px.choropleth(
        df,
        locations='id',
        geojson=geo,
        color='F2022',
        title="Map of temperature coefficient change in 2022",
    )

    return fig

#### GRAPHIQUE ELEMENTAIRE ####
def graphele():
    """
    Trace un graphique elementaire interactif de l'espérance de vie
    en fonction de l'émission de CO2 et de l'année.
    
    Returns:
        fig: Le graphique elementaire interactif tracé.
        data: Les données utilisées pour tracer le graphique.
        years: Les années du graphique (permettra de choisir une
        année pour tracer le graphique)
   
    """

    script_dir = os.path.dirname(__file__)
    gapminder = pd.read_csv(os.path.join(script_dir,
            'life-expectancy-at-birth-vs-co-emissions-per-capita.csv'))

    gapminder['Continent'] = gapminder.groupby('Entity')[
        'Continent'].transform(lambda x: x.fillna(x.iloc[0]))

    years = sorted(gapminder["Year"].unique())
    data = {year: gapminder[gapminder["Year"] == year].dropna(
        subset=[
        'Life expectancy - Sex: all - Age: at birth - Variant: estimates',
        'CO2 emissions (metric tons per capita)']) for year in years}
    fig = px.scatter(data[2007],
                    x="CO2 emissions (metric tons per capita)",
                    y="Life expectancy - Sex: all - Age: at birth - Variant: estimates",
                    color="Continent", hover_name="Entity",
                    title="Relationship between C02 emissions and life expectancy",)

    return fig, data, years
