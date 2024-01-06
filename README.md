## **French Version** 
(an English Version is given at the end)

# Guide d'utilisateur
Instructions pour le déploiement et l'utilisation de votre dashboard.

# Rapport d'Analyse
Principales conclusions extraites des données avec graphiques et explications.

This

# Guide de developpeur

---

## **English Version**

# User Guide
Instructions pour le déploiement et l'utilisation de votre dashboard.

# Analisis Report
Principales conclusions extraites des données avec graphiques et explications.

This

# Developper Guide

The code is composed of three modules: main.py, graphiques.py, and interactif.py.

The file main.py creates the Dashboard. First, it imports the Dash components, and the modules graphiques.py and interactif.py. Then, it initializes the application. It constructs the app and includes the graphics. To add a graphic, you have to call it in the constructor. Next, main.py calls the update module to enable interactivity with the user. Finally, it runs the app.

The module graphiques.py allows defining different graphics. First, it imports json, pandas, and plotly_express components. Then, it defines secondary functions that help create graphic functions. Next, it defines graphic functions: a histogram (histogramme()), a map (carte()), and an elementary graphic (graphele()).

Finally, the file interactif.py is used to define interactivity between the user and a graphic. It imports dash.dependencies, plotly_express, and graphiques.py. It defines the dynamic component and contents function to make the interactivity between the user and a previously configured dynamic graphic (configured in graphiques.py and main.py).