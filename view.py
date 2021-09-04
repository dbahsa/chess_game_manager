#! /user/bin/env python3
# -*- coding: utf-8 -*-


import json
from tinydb import TinyDB
import pandas as pd

import model
# import controller


### PRINTOUTS FROM DB ONLY !!!! ### 

########################### TOURNAMENT VARIABLES & TOOLS ########################

## -- 'db' allows to generate a DB file, 'data.json', for this app --
db = TinyDB('data.json', indent=4)
tournaments_table = db.table('tournaments_db')
players_table = db.table('players_db')

filename = "data.json"
with open(filename, "r") as f:
    json_object = json.load(f)

## -- 'df' allows to update data in DB file --
df = pd.DataFrame(json_object['players_db'])
real_db = df.T


########################### TOURNAMENT VIEWS ########################

"""View Tournament Info"""

## -- View Tournament Info  -- OK OK
def view_tournament_info():
    """ Function to view tournament info """
    
    print("\n-- Voici les informations actuelles du tournoi --\n")
    h = 1
    for i in json_object['tournaments_db']['1']:
        print(f"{[h]} {i}: {json_object['tournaments_db']['1'][i]}")
        h += 1

############################# PLAYERS VIEWS #########################

""" View players data from db file /!!!\ """

## -- To view players info  -- ok OK !!!
def view_players_info():
    """ Function to view tournament info """
    
    print("\n📚 Voici les informations actuelles sur les joueurs\n")
    print(real_db)


""" View Ranked Players by Ratings & Scores """

## -- Func - Ranked Players by score and rating /!!\ BACK IN CONTROLLER !!!
def view_sorted_players_by_score_and_rating():
    """View sorted players by score and rating"""

    print('\n🙂 Classement des joueurs par score et par nombre de points au classement général:\n')
    k=0
    for u in sorted_players_by_score_and_rating:
        print(f"N°{k+1}: {u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']}\t{u[1]['Classement']}\t{u[1]['Score']}")
        k +=1


## -- Func - Ranked Players by rating, Used ONLY for Round1 /!!\ BACK IN CONTROLLER !!!
def view_sorted_players_by_rating():
    print('\n🙂 Classement des joueurs par nombre de points au classement général:\n')
    k=0
    for u in sorted_players_by_rating:
        print(f"N°{k+1}: {u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']}\t{u[1]['Classement']}")
        k +=1


## --  /!!\ BACK IN CONTROLLER !!!
def view_generate_players_round1_matchup_ref_rating_by_index():
    """ Function used to view 'sorted_players_by_rating' variable """

    print("\n🙂 Classement général des joueurs avec n°index:\n")
    for u in sorted_players_by_rating:
        w = 'Index n°' + u[0]
        x = u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']
        y = 'Classement: ' + str(u[1]['Classement'])
        a = [w, x, y]
        print(a)
# view_generate_players_round1_matchup_ref_rating_by_index()


## -- VIEW ROUND1 MATCHUPS FROM DB --  /!!\ BACK IN CONTROLLER !!!
def view_round1_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round1:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1


### -- VIEW ROUND2 MATCHUPS FROM DB --  /!!\ BACK IN CONTROLLER !!!
def view_round2_matchups():
    """Function to view Round2 Matchups"""
    
    print("\n💡 Voici les Matches du Round2:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1


## -- VIEW ROUND3 MATCHUPS FROM DB --  /!!\ BACK IN CONTROLLER !!!
def view_round3_matchups():
    """Function to view Round3 Matchups"""
    
    print("\n💡 Voici les Matches du Round3:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1


### -- VIEW ROUND4 MATCHUPS FROM DB --  /!!\ BACK IN CONTROLLER !!!
def view_round4_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round4:\n")
    e = 1
    for x in list(json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'].values()):
        b = list(x.values())
        print(f"Match n°{e}: {b[0][0]} vs. {b[0][1]}")
        e +=1


############################# MENU VIEWS #########################


## -- View Main Menu --
def main_menu():
    """ Main Menu interface """
    
    a = "\n 🏁 GESTIONNAIRE DE TOURNOI D'ECHECS 🏁"
    b = "\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    c = "\n~~~~~~~~~~ 🏠 MENU PRINCIPAL ~~~~~~~~~~~"
    x = "\n\n   ☰ Pour choisir votre menu, taper:\n"
    d = "\n [1] pour Tournoi       [2] pour Joueurs"
    f = "\n [3] pour Rapports      [4] pour Arrêter"
    g = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    menu = a+b+c+x+d+f+g
    print()
    print(menu)

## -- View Tournament Menu --
def tournament_menu():
    """ Menu interface """
    
    a = "\n---------------- 🔥 MENU TOURNOI 🔥 ---------------"
    b = "\nTaper [1] pour créer un nouveau tournoi"
    c = "\n      [2] pour ajouter huit joueurs"
    d = "\n      [3] pour modifier les données du tournoi"
    e = "\n      [4] pour modifier les données des joueurs"
    g = "\n      [5] pour arrêter le programme"
    h = "\n      [6] pour revenir au 'MENU PRINCIPAL'"
    menu = a+b+c+d+e+g+h
    print(menu)


## -- View Starting Players Menu --
def players_menu():
    """ Menu interface """
    # Players menu: [1]Create | [2]Open | [3]Go Back | [4]Exit
    c = "\n------------ 🔥 MENU JOUEURS 🔥 ---------------"
    x = "\nTaper le chiffre:"
    d = "\n[1] pour Créer            [2] pour Actualiser"
    f = "\n[3] pour Menu Principal   [4] pour Arrêter\n"
    menu = c+x+d+f
    print(menu)


## -- View Update Tournament Menu
def update_tournament_menu_in():
    """ Menu interface """
    
    a = "\n------------------ 🔥 ACTUALISATION DU TOURNOI 🔥 -------------------"
    b = "\nTaper [1] pour le nom\t[2] pour le lieu\t[3] pour la date"
    c = "\n      [4] pour modifier le nombre de tours"
    d = "\n      [5] pour modifier le contrôle du temps"
    e = "\n      [6] pour modifier la description du tournoi"
    f = "\n      [7] pour arrêter \t[8] pour le 'MENU PRINCIPAL'\n"
    menu = a+b+c+d+e+f
    print(menu)


## -- view Update Players Menu
def update_players_menu():
    """ Menu interface """
    
    a = "\n------------------ 🔥 ACTUALISATION DES JOUEURS 🔥 --------------------"
    b = "\nTaper [1] pour le nom\t[2] pour le prénom\t[3] pour le sexe"
    c = "\n      [4] pour modifier la date de naissance"
    d = "\n      [5] pour modifier le nombre de point au classement général"
    e = "\n      [6] pour ajouter ou modifier un score"
    f = "\n      [7] pour effacer tous les scores 🚨"
    g = "\n      [8] pour arrêter \t[9] pour le 'MENU PRINCIPAL'\n"
    menu = a+b+c+d+e+f+g
    print(menu)


## -- Welcome Message--
def welcome_msg():
    print("\nBonjour et bienvenu!")


## -- Goodbye msg --
def byebye():
    print("\n🥸  Merci d'avoir utilisé ce programme, et à bientôt 👍🤓\n")


## -- Error msg --
def error_msg():
    print(f"😅 Mauvaise saisie...\nMerci d'essayer à nouveau.\n")

## -- Contact us msg --
def contact_us_quick_msg():
    print("🚨 Merci de nous joindre pour modifier le nombre de tours, qui par défaut est égal à 4")
