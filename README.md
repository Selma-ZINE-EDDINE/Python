## **French Version** 
(an English Version is given at the end)

# Guide d'utilisateur

Clônez le projet dans Visual Studio Code.
Ouvrez le fichier main.py et lancez le programme. Un lien est généré. Cliquez dessus pour ouvrir le dashboard dans votre navigateur.
Le premier graphique est une carte du monde qui montre le coefficient d'augmentation de la température en 2022. Vous pouvez zoomer et survoler avec la souris pour afficher le nom du pays et le coefficient d'augmentation précis.

Ensuite, le deuxième graphique est un histogramme. Il montre le coefficient d'augmentation mondial au fil des années. En bleu, les coefficients représentés sont négatifs, en orange, ils sont inférieurs à un et supérieurs à zéro, et en rouge, les coefficients sont supérieurs à 1. Vous pouvez survoler avec la souris sur les barres pour afficher le coefficient précis.

Enfin, le dernier graphique est un graphique élémentaire qui montre l'espérance de vie en fonction des émissions de CO2. Vous pouvez sélectionner l'année pour tracer le graphique.

# Rapport d'Analyse

Ce dashboard illustre l'impact de la pollution : le changement de température et le danger des émissions de CO2 sur notre espérance de vie.

La carte révèle que le coefficient de température est positif dans presque tous les pays, indiquant que tout le monde est touché par le changement de température.

L'histogramme souligne que le coefficient de température est de plus en plus élevé. Il est donc crucial de prendre des mesures strictes pour stopper cette augmentation.

Enfin, le graphique élémentaire démontre que les émissions de CO2 réduisent notre espérance de vie. Il met en évidence l'impact direct de la pollution sur nos vies.

En conclusion, les graphiques de ce dashboard illustrent l'impact de la pollution sur la vie humaine et la planète. Des mesures strictes devraient être prises à l'échelle mondiale pour réduire la pollution, car elle touche le monde entier.

# Guide de developpeur

Le code est composé de trois modules : main.py, graphiques.py et interactif.py.

Le fichier main.py crée le dashboard. Il importe les composants Dash ainsi que les modules graphiques.py et interactif.py. Ensuite, il initialise l'application. Il construit l'application et inclut les graphiques. Pour ajouter un graphique, il faut l'appeler dans le constructeur. Ensuite, main.py appelle le module de mise à jour (interactif.py) pour permettre l'interactivité avec l'utilisateur. Enfin, il lance l'application.

Le module graphiques.py permet de définir différents graphiques. Tout d'abord, il importe les composants json, pandas et plotly_express. Ensuite, il définit des fonctions secondaires qui aident à créer les fonctions graphiques. Ensuite, il définit les fonctions graphiques : un histogramme (histogramme()), une carte (carte()) et un graphique élémentaire (graphele()).

Enfin, le fichier interactif.py est utilisé pour définir l'interactivité entre l'utilisateur et un graphique. Il importe dash.dependencies, plotly_express et graphiques.py. Il définit les composants dynamiques et les fonctions pour assurer l'interactivité entre l'utilisateur et un graphique dynamique précédemment configuré (configuré dans graphiques.py et main.py).

# Sources
Annual_Surface_Temperature_Change.csv: International Monetary Fund (IMF)
https://climatedata.imf.org/datasets/4063314923d74187be9596f10d034914/explore


life-expectancy-at-birth-vs-co-emissions-per-capita.csv: Our World in Data
https://ourworldindata.org/grapher/life-expectancy-at-birth-vs-co-emissions-per-capita

countries.geojson : GeoJSON Maps
https://geojson-maps.ash.ms/

---

## **English Version**

# User Guide

Clone the project in Visual Studio Code.
Open the file main.py and launch the program. A link is generated. Click on it to open the dashboard in your browser.

The first graphic is a world map that shows the incresment coefficient of temperature in 2022. You can zoom and hover your mouse over it to display the name of the country and the precise incresment coefficient.

Next, the second graphic is a histogram. It shows the world incresment coefficient during the years. In blue, you can see negative coefficients, in orange, coefficients inferior to one and superior to zero, and in red, you can see coefficients superior to 1. You can hover your mouse over the bars to display the precise coefficient.

Finally, the last graphic is an elementary chart that shows life expectancy as a function of CO2 emissions. You can select the year use for the chart.

# Analisis Report

This dashboard illustrates the impact of pollution: the change in temperature and the danger of CO2 emissions on our life expectancy.

The map reveals that the temperature coefficient is positive in almost all countries, indicating that everyone in the world is affected by temperature change.

The histogram shows that the temperature coefficient is consistently high. Therefore, it is crucial to take strict measures to stop this increase.

Finally, the elementary chart demonstrates that CO2 emissions reduce our life expectancy. It highlights the direct impact of pollution on our lives.

In conclusion, this dashboard illustrates the impact of pollution on human life and the planet. Strict measures should be taken globally to reduce pollution as it affects the entire world.

# Developper Guide

The code is composed of three modules: main.py, graphiques.py, and interactif.py.

The file main.py creates the Dashboard. First, it imports the Dash components, and the modules graphiques.py and interactif.py. Then, it initializes the application. It constructs the app and includes the graphics. To add a graphic, you have to call it in the constructor. Next, main.py calls the update module to enable interactivity with the user. Finally, it runs the app.

The module graphiques.py allows defining different graphics. First, it imports json, pandas, and plotly_express components. Then, it defines secondary functions that help create graphic functions. Next, it defines graphic functions: a histogram (histogramme()), a map (carte()), and an elementary graphic (graphele()).

Finally, the file interactif.py is used to define interactivity between the user and a graphic. It imports dash.dependencies, plotly_express, and graphiques.py. It defines the dynamic component and contents function to make the interactivity between the user and a previously configured dynamic graphic (configured in graphiques.py and main.py).

# Sources

Annual_Surface_Temperature_Change.csv: International Monetary Fund (IMF)
https://climatedata.imf.org/datasets/4063314923d74187be9596f10d034914/explore


life-expectancy-at-birth-vs-co-emissions-per-capita.csv: Our World in Data
https://ourworldindata.org/grapher/life-expectancy-at-birth-vs-co-emissions-per-capita

countries.geojson : GeoJSON Maps
https://geojson-maps.ash.ms/