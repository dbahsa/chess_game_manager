#! /user/bin/env python3
# -*- coding: utf-8 -*-


import json
from tinydb import TinyDB
import pandas as pd
import pprint

## -- PPrint for internal use ONLY
pp = pprint.PrettyPrinter(indent=4)

import tournament, players


### PRINTOUTS FROM DB ONLY !!!! ### 

########################### TOURNAMENT VARIABLES & TOOLS ########################

## -- 'db' allows to generate a DB file, 'data.json', for this app --

db = TinyDB('data.json', indent=4)
tournaments_table = db.table('tournaments_db')
players_table = db.table('players_db')

filename = "data.json"
with open(filename, "r") as f:
    json_object = json.load(f)



########################### TOURNAMENT VIEWS ########################


"""Players infos"""

## -- View Tournament data with players ranked by indexes (tous les acteurs) -- ok ok!!!
def players_info():
    """ Function to view tournament info """
    
    print("\n📚 Voici les informations actuelles sur les joueurs\n")
    print(players.real_db)
    print()



## -- View Tournament data with players ranked by last and first names -- ok ok !!!
def tournament_overview_by_players_by_last_and_first_names():
    """View sorted players sorted by last and first names"""

    print('\n📚 Classement des joueurs par ordre alphabétique:\n')
    print(players.real_db.sort_values(["Nom de famille", "Prénom"], ascending = (True)))
    print()


## -- Func - Ranked Players by score and rating -- ok ok!!!
def sorted_players_by_score_and_rating():
    """View sorted players by score and rating"""

    print('\n📚 Classement des joueurs par score et par nombre de points au classement général:\n')
    k=0
    for u in players.sorted_players_by_score_and_rating:
        print(f"N°{k+1}: {u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']}\t{u[1]['Classement']}\t{u[1]['Score']}")
        k +=1


## -- Func - Ranked Players by rating, Used ONLY for Round1 __ OK OK !!
def sorted_players_by_rating():
    print('\n📚 Classement des joueurs par nombre de points au classement général:\n')
    k=0
    for u in players.sorted_players_by_rating:
        print(f"N°{k+1}: {u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']}\t{u[1]['Classement']}")
        k +=1


"""Tournament Infos"""

## -- View Tournament Info  -- OK OK !!!
def tournament_info():
    """ Function to view tournament info """
    
    print("\n📚 Voici les informations de l'actuel tournoi: \n")
    h = 1
    for i in json_object['tournaments_db']['1']:
        print(f"{[h]} {i}: {json_object['tournaments_db']['1'][i]}")
        h += 1


## -- View All Rounds Info  -- OK OK !!!
def all_rounds_info():
    """ Function to view all rounds info """
    
    print("\n📚 Voici les informations de tous les tours de l'actuel tournoi: \n")
    h = 1
    for i in json_object['tournaments_db']['1']['Tournées']:
        df = pd.DataFrame(json_object['tournaments_db']['1']['Tournées'][i])
        print(f"💥 {i}: {df}")
        print()
        h += 1


## -- View All Matches Info  -- OK OK !!!
def all_matches_info():
    """ Function to view all rounds info """
    
    print("\n📚 Voici les informations de tous les matches de l'actuel tournoi: \n")
    k = []
    p =[]
    for i in players.json_object['tournaments_db']['1']['Tournées']:
        l = players.json_object['tournaments_db']['1']['Tournées'][f'{i}']['Matches']
        p.append(i)
        k.append(l)
    df = pd.DataFrame(k, index=p)
    print(df)
    print()



#############################   MATCHES VIEWS #########################


## --  ok ok!!!
def view_generate_players_round1_matchup_ref_rating_by_index():
    """ Function used to view 'sorted_players_by_rating' variable """

    print("\n🙂 Classement général des joueurs avec n°index:\n")
    for u in players.sorted_players_by_rating:
        w = 'Index n°' + u[0]
        x = u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']
        y = 'Classement: ' + str(u[1]['Classement'])
        a = [w, x, y]
        print(a)


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


## -- View Main Menu -- OK OK !!!
def main_menu():
    """ Main Menu interface """
    
    a = "\n       🏁 GESTIONNAIRE DE TOURNOI D'ECHECS 🏁"
    b = "\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    c = "\n~~~~~~~~~~~~~~~~~ 🏠 MENU PRINCIPAL ~~~~~~~~~~~~~~~~~"
    x = "\n\n  ☰ Faites votre choix en tapant:\n"
    d = "\n [1] Créer un tournoi       [2] Ajouter les joueurs"
    f = "\n [3] Modifier un tournoi    [4] Actualiser infos joueurs"
    g = "\n [5] Activer les matches    [6] Arrêter les matches"
    h = "\n [7] Générer les tours      [8] Entrer les résulats"
    i = "\n [9] Consulter les rapports [0] Menu principal"
    j = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    menu = a+b+c+x+d+f+g+h+i+j
    print()
    print(menu)


## -- Launch Games Menu --
def launch_games_menu():
    """ Menu interface """
    
    a = "\n-----------🔥 COMMENCEMENT DE ROUND 🔥 -----------"
    b = "\nTaper [1] pour Round 1      [3] pour Round 3"
    c = "\n      [2] pour Round 2      [4] pour Round 4"
    g = "\n      [5] pour revenir au 'MENU PRINCIPAL'"
    menu = a+b+c+g
    print(menu)


## -- Stop Games Menu --
def stop_games_menu():
    """ Menu interface """
    
    a = "\n--------- 🔥 FIN DE ROUND 🔥 -----------"
    b = "\nTaper [1] pour Round 1      [3] pour Round 3"
    c = "\n      [2] pour Round 2      [4] pour Round 4"
    g = "\n      [5] pour revenir au 'MENU PRINCIPAL'"
    menu = a+b+c+g
    print(menu)


## -- View Tournament Menu --
def tournament_menu():
    """ Menu interface """
    
    a = "\n---------------- 🔥 MENU TOURNOI 🔥 ---------------"
    b = "\nTaper [1] pour créer un nouveau tournoi"
    c = "\n      [2] pour ajouter huit joueurs"
    d = "\n      [3] pour modifier les données du tournoi"
    e = "\n      [4] pour modifier les données des joueurs"
    g = "\n      [5] pour revenir en arrière"
    h = "\n      [6] pour revenir au 'MENU PRINCIPAL'"
    menu = a+b+c+d+e+g+h
    print(menu)


## -- View Reports Menu --
def latest_reports_menu():
    """ Menu interface """
    
    c = "\n------------ 🔥 MENU RAPPORTS 🔥 ---------------"
    x = "\n ☰ Pour voir les rapports ci-après, taper:\n"
    d = "\n[1] LES JOUEURS PAR NOM       [2] LES JOUEURS PAR POINTS"
    f = "\n[3] LES TOURNOIS              [4] LES TOURS PAR TOURNOI"
    g = "\n[5] LES MATCHES PAR TOURS     [6] revenir au menu principal"
    menu = c+x+d+f+g
    print(menu)


## -- View Update Tournament Menu
def update_tournament_menu_in():
    """ Menu interface """
    
    a = "\n----------- 🔥 PRISE EN MAIN DU TOURNOI 🔥 -------------"
    b = "\nTaper [1] pour le nom\t[2] pour le lieu\t[3] pour la date"
    c = "\n      [4] pour modifier le nombre de tours"
    d = "\n      [5] pour modifier le contrôle du temps"
    e = "\n      [6] pour modifier la description du tournoi"
    f = "\n      [7] pour revenir au 'MENU PRINCIPAL'\n"
    menu = a+b+c+d+e+f
    print(menu)


## -- view Update Players Menu
def update_players_menu():
    """ Menu interface """
    
    a = "\n------------------ 🔥 GESTION DES JOUEURS 🔥 --------------------"
    b = "\nTaper [1] pour le nom\t[2] pour le prénom\t[3] pour le sexe"
    c = "\n      [4] pour modifier la date de naissance"
    d = "\n      [5] pour modifier le nombre de point au classement général"
    e = "\n      [6] pour ajouter ou modifier un score"
    f = "\n      [7] pour effacer tous les scores 🚨"
    g = "\n      [8] pour revenir au 'MENU PRINCIPAL'\n"
    menu = a+b+c+d+e+f+g
    print(menu)


## -- view how rounds are generated
def compute_next_round_menu():
    """ Roundx Menu """
    
    a = "\n------------------------------------------- 🔥 GESTION DES ROUNDS 🔥 --------------------------------------"
    b = "\n💡 Pour obtenir les matches de chaque round, il est crucial d'avoir bien saisir dès le départ le \n"
    c = "classement des joueurs en s'assurant qu'ils n'ont aucun point à leur compteur de score au début du tournoi.\n"
    d = "\nVoici les étapes à suivre par round.  Taper pour:\n"
    e = "💥 Round1                    💥 Round2                  💥 Round3                  💥 Round4\n"
    f = "[1] Réinitialiser Scores  │ [2] Voir Matches Round2  │ [3] Voir Matches Round3  │ [4] Voir Matches Round4\n"
    g = "    Voir Classement       │                          │                          │\n"
    h = "    Voir Matches Round1   │                          │                          │\n"
    i = "[a] Lancer Round1         │ [e] Lancer Round2        │ [h] Lancer Round3        │ [m] Lancer Round4\n"
    j = "[b] Arrêter Round1        │ [f] Arrêter Round2       │ [i] Arrêter Round3       │ [n] Arrêter Round4\n"
    k = "[c] Saisir Scores Round1  │ [v] Saisir Scores Round2 │ [k] Saisir Scores Round3 │ [p] Saisir Scores Round4\n"
    l = "\n[5] Revenir au menu principal\n"
    menu = a+b+c+d+e+f+g+h+i+j+k+l
    print(menu)


""" Small User Interactive Messages """

## -- Welcome Message--
def welcome_msg():
    print("\n\t\tBonjour et bienvenu!")


## -- Goodbye msg --
def byebye():
    print("\n🥸  Merci d'avoir utilisé ce programme, et à bientôt 👍🤓\n")


## -- Error msg --
def error_msg():
    print(f"😅 Mauvaise saisie...\nMerci d'essayer à nouveau.\n")

## -- Contact us msg --
def contact_us_quick_msg():
    print("🚨 Merci de nous joindre pour modifier le nombre de tours, qui par défaut est égal à 4")
