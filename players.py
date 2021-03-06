#! /user/bin/env python3
# -*- coding: utf-8 -*-


""" modules & packages """
import json
from dataclasses import dataclass, field
from tinydb import TinyDB
import pandas as pd
import datetime
import pprint

import tournament


""" players variables used in this file script """

total_number_of_players = 8
registered_players = 0
all_players_db = [] 

## -- 'db' allows to generate a DB file, 'data.json', for this app --

db = TinyDB('data.json', indent=4)
tournaments_table = db.table('tournaments_db')
players_table = db.table('players_db')

filename = "data.json"
with open(filename, "r") as f:
    json_object = json.load(f)

## -- 'df' allows to update data in DB file --
df = pd.DataFrame(json_object['players_db'])
## - 'T' (Transpose) to use db indexes as table indexes for a better reading of data
real_db = df.T

## -- PPrint for internal use ONLY
pp = pprint.PrettyPrinter(indent=4)

""" # -- Prog Start Here -- """

## -- Scores are added directly by the user in the DB file
def player_score():
    """ return a list of player scores """
    
    scores =[]
    return scores


## -- Done!
def player_tournament_participation():
    """ Function that adds tournaments in which a player participated in """
    
    tournaments =[]
    return tournaments


## -- Done! --
@dataclass
class Player:
    """Class to generate player instances"""
    
    last_name: str
    first_name: str
    birth_date: str
    gender: str
    rating: int
    scores: list = field(init=False, repr=False, default_factory=player_score)
    tournaments: list = field(init=False, repr=False, default_factory=player_tournament_participation)
    single_player_db: dict = field(init=False, repr=False)

    def __post_init__(self):
        """ Method to help generate player full data"""
        self.single_player_db = {"Nom de famille": self.last_name,
                                "Prénom": self.first_name,
                                "Date de naissance": self.birth_date,
                                "Sexe": self.gender,
                                "Classement": self.rating,
                                "Score": self.scores,
                                "Tournois": self.tournaments}


## --
def add_players():
    """ function to instantiate players"""
    
    print("\nEnregistrement des 8 joueurs...")
    for i in range(1,9):
        print(f"\nEntrer les informations sur le joueur n°{i}")
        p = Player(input("- Nom de famille: "),
                    input("- Prénom: "),
                    input("- Date de naissance telle que jj/mm/aaaa (ex: 18/02/1973): "),
                    input("- Sexe [H/F]: ").upper(),
                    int(input("- Classement: "))
                    )
        all_players_db.append(p.single_player_db)
        print(f"\nJoueur n°{i} enregistré.")
    print("Fin de l'enregistrement des joueurs.\n")


""" Saving players data into db file /!!!\ """

## -- 
def save_players_data():
    """ save players data """
    
    db = TinyDB(filename)
    players_table = db.table('players_db')
    players_table.truncate()
    players_table.insert_multiple(all_players_db)
    ## -- Add players indexes from players_db table
    json_object['tournaments_db']['1']['Joueurs'] = [j for j in json_object['players_db']]
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)


## --
def save_players_indexes_in_tournaments_db():
    '''Function to save players indexes in tournament table in db file'''

    for i in range(len(list(json_object["players_db"]))):
        json_object["tournaments_db"]['1']['Joueurs'].append(list(json_object["players_db"])[i])
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)


""" Update players data from db file /!!!\ """

## -- Update Player last name in db file -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_lname():
    """ Function to update players last name in db file """

    print("\n🚧 Procédons à l'actualisation des données...")
    while True:
        msg = "veuillez taper son numéro d'index entre [1] et [8], ou taper [0] pour revenir au menu pécédent: "
        print("\n🚨 Pour modifier le 'Nom de famille' d'un joueur, ", end="")
        user_choice = input(msg)
        try:
            if int(user_choice) in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}] pour modifier le 'Nom de famille' de", end="")
                print(f" {real_db.at[user_choice, 'Prénom']} {real_db.at[user_choice, 'Nom de famille']}.")
                txt = f"🚦 Veuillez saisir son nouveau 'Nom de famille', svp: "
                real_db.at[user_choice, 'Nom de famille'] = str(input(txt).capitalize())
                data = real_db.to_json(orient='index', indent=4)
                json_object['players_db'] = json.loads(data)
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                print(f"🎉 Le nouveau 'Nom de famille' de {real_db.at[user_choice, 'Prénom']} est ", end="")
                print(f"{real_db.at[user_choice, 'Nom de famille']}.")
                print()
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- Update Player first name in db file -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_fname():
    """ Function to update players first name in db file """

    print("\n🚧 Procédons à l'actualisation des données...")
    while True:
        msg = "veuillez taper son numéro d'index entre [1] et [8], ou taper [0] pour revenir au menu pécédent: "
        print("\n🚨 Pour modifier le 'Prénom' d'un joueur, ", end="")
        user_choice = input(msg)
        try:
            if int(user_choice) in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}] pour modifier le 'Prénom' de", end="")
                print(f" {real_db.at[user_choice, 'Nom de famille']}.")
                txt = f"🚦 Veuillez saisir son nouveau 'Prénom', svp: "
                real_db.at[user_choice, 'Prénom'] = str(input(txt).capitalize())
                data = real_db.to_json(orient='index', indent=4)
                json_object['players_db'] = json.loads(data)
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                print(f"🎉 Le nouveau 'Prénom' de {real_db.at[user_choice, 'Nom de famille']} est ", end="")
                print(f"{real_db.at[user_choice, 'Prénom']}.")
                print()
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- Update Player gender in db file -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_gender():
    """ Function to update players gender in db file """

    print("\n🚧 Procédons à l'actualisation des données...")
    while True:
        msg = "veuillez taper son numéro d'index entre [1] et [8], ou taper [0] pour revenir au menu pécédent: "
        print("\n🚨 Pour modifier le 'Sexe' d'un joueur, ", end="")
        user_choice = input(msg)
        try:
            if int(user_choice) in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}] pour changer le 'Sexe' de", end="")
                print(f" {real_db.at[user_choice, 'Prénom']} {real_db.at[user_choice, 'Nom de famille']}.")
                txt = f"🚦 Veuillez taper [H] pour homme et [F] pour femme: "
                real_db.at[user_choice, 'Sexe'] = str(input(txt).capitalize())
                data = real_db.to_json(orient='index', indent=4)
                json_object['players_db'] = json.loads(data)
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                print(f"🎉 Le nouveau 'Sexe' de {real_db.at[user_choice, 'Nom de famille']} est ", end="")
                print(f"{real_db.at[user_choice, 'Sexe']}.")
                print()
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- Update Player birth date in db file -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_birth_date():
    """ Function to update players birth date in db file """

    print("\n🚧 Procédons à l'actualisation des données...")
    while True:
        msg = "veuillez taper son numéro d'index entre [1] et [8], ou taper [0] pour revenir au menu pécédent: "
        print("\n🚨 Pour modifier la 'Date de naissance' d'un joueur, ", end="")
        user_choice = input(msg)
        try:
            if int(user_choice) in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}] pour changer la 'Date de naissance' de", end="")
                print(f" {real_db.at[user_choice, 'Prénom']} {real_db.at[user_choice, 'Nom de famille']}.")
                txt = f"🚦 Taper la nouvelle date en respectant le format jj/mm/aaaa (ex: 18/02/1973): "
                real_db.at[user_choice, 'Date de naissance'] = str(input(txt).capitalize())
                data = real_db.to_json(orient='index', indent=4)
                json_object['players_db'] = json.loads(data)
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                print(f"🎉 La nouvelle 'Date de naissance' de {real_db.at[user_choice, 'Nom de famille']}", end="")
                print(f" est {real_db.at[user_choice, 'Date de naissance']}.")
                print()
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- Update Player rating in db file -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_rating():
    """ Function to update players rating in db file """

    print("\n🚧 Procédons à l'actualisation des données...")
    while True:
        msg = "veuillez taper son numéro d'index entre [1] et [8], ou taper [0] pour revenir au menu pécédent: "
        print("\n🚨 Pour modifier le nombre de points d'un joueur au 'Classement' général, ", end="")
        user_choice = input(msg)
        try:
            if int(user_choice) in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}] pour changer le 'Classement' de", end="")
                print(f" {real_db.at[user_choice, 'Prénom']} {real_db.at[user_choice, 'Nom de famille']}.")
                txt = f"🚦 Veuillez taper en chiffre son nouveau nombre de points au 'Classement' général: "
                real_db.at[user_choice, 'Classement'] = str(input(txt))
                data = real_db.to_json(orient='index', indent=4)
                json_object['players_db'] = json.loads(data)
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                print(f"🎉 Le nouveau nombre de points au 'Classement' général de ", end="")
                print(f"{real_db.at[user_choice, 'Nom de famille']} est {real_db.at[user_choice, 'Classement']}.")
                print()
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- Add Player score in db file -- /!!!\ At the end of the script, send the user back to the former menu
def add_player_score():
    """ Function to add players score in db file """
    
    print("\n🚧 Procédons à l'ajout de score...")
    while True:
        msg = "taper son numéro d'index entre [1] et [8], ou taper [0] pour revenir au menu pécédent: "
        print("\n🚨 Pour ajouter le 'Score' d'un joueur, ", end="")
        user_choice = input(msg)
        try:
            if int(user_choice) in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}] pour ajouter un 'Score' à ", end="")
                print(f"{real_db.at[user_choice, 'Prénom']} {real_db.at[user_choice, 'Nom de famille']}.")
                add_score = float(input("🚨 Entrer le nouveau score du joueur: ").replace(",", "."))
                try:
                    if add_score in [0, 0.5, 1]:
                        real_db.at[user_choice, 'Score'].append(add_score)
                        data = real_db.to_json(orient='index', indent=4)
                        json_object['players_db'] = json.loads(data)
                        with open(filename, "w") as f:
                            json.dump(json_object, f, indent=4)
                        print(f"🎉 Vous avez ajouté {real_db.at[user_choice, 'Score']}", end="")
                        print(f" au 'Score' de {real_db.at[user_choice, 'Prénom']}", end="")
                        print(f" {real_db.at[user_choice, 'Nom de famille']}")
                        print()
                    else:
                        print("💥 Merci de saisir 'uniquement' un score de [0], [0.5] ou [1].")
                        continue
                except:
                    print("💥 Erreur de saisie...")
                else:
                    continue
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_score():
    """ Function to update/add players score in db file """
    
    print("\n🚧 Procédons à l'actualisation des données...")
    while True:
        msg = "taper son numéro d'index entre [1] et [8], ou taper [0] pour revenir au menu pécédent: "
        print("\n🚨 Pour actualiser le 'Score' d'un joueur, ", end="")
        user_choice = input(msg)
        try:
            if int(user_choice) in range(1,9):
                print(f"\n💡 Vous avez tapé [{user_choice}] pour actualiser un 'Score' de ", end="")
                print(f"{real_db.at[user_choice, 'Prénom']} {real_db.at[user_choice, 'Nom de famille']}", end="")
                print(" mentionné ci-dessous:\n")
                ## --> if the score list is not empty -> Update Score
                if len(real_db.at[user_choice, 'Score']) > 0:
                    s = 0
                    for x in real_db.at[user_choice, 'Score']:
                        print(f"🏁 A son match n°{s+1}, {real_db.at[user_choice, 'Prénom']} a eu {x} point")
                        s += 1
                    update_msg = "\n🚨 Taper le numéro du match dont le score doit être modifié: "
                    update_score = int(input(update_msg))
                    
                    try:
                        if update_score > 0 and update_score <= len(real_db.at[user_choice, 'Score']):
                            score_ref = real_db.at[user_choice, 'Score'][update_score-1]
                            print(f"💡 Le match n°{update_score} a pour score: {score_ref} \n")
                            msg = f"🚨 Le nouveau score du match n°{update_score} est: "
                            new_score = float(input(msg).replace(",", "."))
                            print(new_score)
                            ## --> validate the right choice of points
                            try:
                                if new_score in [0, 0.5, 1]:
                                    real_db.at[user_choice, 'Score'][update_score-1] = new_score
                                    
                                    data = real_db.to_json(orient='index', indent=4)
                                    json_object['players_db'] = json.loads(data)
                                    with open(filename, "w") as f:
                                        json.dump(json_object, f, indent=4)
                                    
                                    p_fname = real_db.at[user_choice, 'Prénom']
                                    p_lname = real_db.at[user_choice, 'Nom de famille']

                                    print(f"🎉 Félicitations! Le nouveau score de {p_fname} {p_lname}", end="")
                                    print(f" pour le match n°{update_score}", end="")
                                    print(f" est: {real_db.at[user_choice, 'Score']}")
                                    print()
                                else:
                                    print("💡 Merci de saisir 'uniquement' un score de [0], [0.5] ou [1].")
                                    continue
                            except:
                                print("💥 Erreur de saisie...")
                            else:
                                continue
                        else:
                            print(f"💥 Erreur de saisie: {update_score} ")
                            print(f"\n💡 Merci de taper le bon numéro de match comme ci-dessous, svp:\n")
                            if len(real_db.at[user_choice, 'Score']) > 0:
                                s = 0
                                for x in real_db.at[user_choice, 'Score']:
                                    print(f"🏁  Score du match n°{s+1}: {x} point")
                                    s += 1
                    except:
                        print("💥 Erreur de saisie...")
                    else:
                        continue
                ## --> if the score list is empty --> Add Score
                else: 
                    add_score = float(input("\n🚨 Ajouter un score pour ce joueur: ").replace(",", "."))
                    try:
                        if add_score in [0, 0.5, 1]:
                            real_db.at[user_choice, 'Score'].append(add_score)
                            data = real_db.to_json(orient='index', indent=4)
                            json_object['players_db'] = json.loads(data)
                            with open(filename, "w") as f:
                                json.dump(json_object, f, indent=4)
                            print(f"🎉 Vous avez actualisé {real_db.at[user_choice, 'Score']}", end="")
                            print(f" au 'Score' de {real_db.at[user_choice, 'Prénom']}", end="")
                            print(f" {real_db.at[user_choice, 'Nom de famille']}")
                            print()
                        else:
                            print("💥 Merci de saisir 'uniquement' un score de [0], [0.5] ou [1].")
                            continue
                    except:
                        print("💥 Erreur de saisie...")
                    else:
                        continue
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                # print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## --  /!!!\ be very careful with this one!
def erase_all_scores():
    """"Function removes all scores at once.  Better be carfeul with it!"""

    for r in range(8):
        real_db.iat[r,5] = []
        data = real_db.to_json(orient='index', indent=4)
        json_object['players_db'] = json.loads(data)
        with open(filename, "w") as f:
            json.dump(json_object, f, indent=4)
    print("Réinitialisation des scores terminée...")


""" Var of Sorted Players Data """

## -- Var - Sorted Players by score and rating
sorted_players_by_score_and_rating = sorted(json_object["players_db"].items(), key=lambda i: (sum(i[1]['Score']), int(i[1]['Classement'])), reverse=True)

## -- Var - Sorted Players by rating
sorted_players_by_rating = sorted(json_object["players_db"].items(), key=lambda i: int(i[1]['Classement']), reverse=True)


""" Var used to generate matchups """

# -- Rounds dict includes all rounds --
rounds = ''

# -- Players matchup reference_rating is used to sort items used to pair up players in a round1 ONLY
players_matchup_reference_rating = []

# -- Players matchup reference_score_and_rating is used to sort items used to pair up players
players_matchup_reference_score_and_rating = []

""" Generate Matches for Round1 """

## -- /!!!\ DO NOT TOUCH IT - LEAVE IT ACTIVE /!!!\
def generate_players_round1_matchup_ref_rating():
    """ Function used to generate 'sorted_players_by_rating' variable """

    # -- Get Player reference for matchups, to be listed in 'players_matchup_reference_rating'
    for u in sorted_players_by_rating:
        w = 'Index n°' + u[0]
        x = u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']
        y = 'Classement: ' + str(u[1]['Classement'])
        a = [w, x, y]
        players_matchup_reference_rating.append(a)
generate_players_round1_matchup_ref_rating()


## -- 
def view_generate_players_round1_matchup_ref_rating_by_index():
    """ Function used to view 'sorted_players_by_rating' variable """

    print("\n🙂 Classement général des joueurs avec n°index:\n")
    for u in sorted_players_by_rating:
        w = 'Index n°' + u[0]
        x = u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']
        y = 'Classement: ' + str(u[1]['Classement'])
        a = [w, x, y]
        print(a)


## -- /!!!\ DO NOT TOUCH IT - LEAVE IT ACTIVE /!!!\
def generate_players_matchup_reference_score_and_rating():
    """ Function used to generate 'sorted_players_by_rating' variable """

    # -- Get Player reference for matchups, to be listed in 'players_matchup_reference_rating'
    for u in sorted_players_by_score_and_rating:
        w = 'Index n°' + u[0]
        x = u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']
        y = 'Classement: ' + str(u[1]['Classement'])
        z = u[1]['Score']
        a = [w, x, y, z]
        players_matchup_reference_score_and_rating.append(a)
generate_players_matchup_reference_score_and_rating()


"""Add Matches Data to Tournament Table"""

## -- /!!!\ LAUNCH ONLY ONCE, ELSE = SERIOUS ISSUE WITH DB !!! 
def add_roundx_in_tournament_table():
    """Function to add new items in tournament table under 'Tournées' key"""
    
    for i in range(int(json_object['tournaments_db']['1']['Nombre de tours'])):
        data = {f'Round{i+1}':{
                    'Temps de départ': '',
                    'Matches': {
                        'Match1': "",
                        'Match2': "",
                        'Match3': "",
                        'Match4': ""
                        },
                    'Temps de fin': ''}
                }
        json_object['tournaments_db']['1']['Tournées'].update(data)
        with open(filename, "w") as f:
            f.seek(0)
            json.dump(json_object, f, indent=4)
# add_roundx_in_tournament_table()

## -- /!!!\ LAUNCH ONLY ONCE, ELSE = SERIOUS ISSUE WITH DB !!! 
def clear_roundx_in_tournament_table():
    """Function to add new items in tournament table under 'Tournées' key"""
    
    for i in range(int(json_object['tournaments_db']['1']['Nombre de tours'])):
        data = {f'Round{i+1}':{
                    'Temps de départ': '',
                    'Matches': {
                        'Match1': "",
                        'Match2': "",
                        'Match3': "",
                        'Match4': ""
                        },
                    'Temps de fin': ''}
                }
        json_object['tournaments_db']['1']['Tournées'].clear()
        with open(filename, "w") as f:
            f.seek(0)
            json.dump(json_object, f, indent=4)
# clear_roundx_in_tournament_table()

""" Generate & Save Matchups & Scores """

""" Round 1 """

###### --- 1. GENERATE & SAVE ROUND1 MATCHUPS --- FIRST LAUNCH 'add_roundx_in_tournament_table()'

## -- /!!! \ generate_players_matchup_with_reference_rating() and 
## -- generate_players_matchup_reference_score_and_rating() must REMAIN initiated 
## -- to allow generate_round1_matchups() to work /!!!\ 
def generate_save_round1_matchups():
    """ Function to generate and save round1 matchups based on players ratings only """

    generate_players_round1_matchup_ref_rating()
    # 1. Generate the 1st pairs of players for Round1
    a = players_matchup_reference_rating
    x = slice(0,4)
    y = slice(4,8)
    z = zip(a[x],a[y])

    ## -- Save Round1 matchups & rounds info in tournament_db table
    o = 1
    for g in z:
        json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'][f'Match{o}'] = tuple(g)
        with open(filename, "w") as f:
            json.dump(json_object, f, indent=4)
        o += 1
    ## -- Add players indexes from players_db table
    json_object['tournaments_db']['1']['Joueurs'] = [j for j in json_object['players_db']]
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
generate_save_round1_matchups()


###### --- 2. VIEW ROUND1 MATCHUPS FROM DB --

## -- --- 
def view_round1_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round1:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1


###### --- 3. LAUNCH ROUND1 GAMES - STARTING TIME -- GOOD MENU TRY EXCEPT /!!!!!\

## -- ADD STARTING TIME ROUND1
def add_starting_time_round1():
    """Function to add starting time for round1"""
    
    print("\n🚧 Êtes-vous prêt à lancer les matches?.")
    while True:
        msg = "\nTaper [1] pour commencer ou taper [0] pour revenir au menu pécédent: "
        user_choice = input(msg)
        try:
            if int(user_choice) == 1:
                current_time = datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de commencer!")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                json_object['tournaments_db']['1']['Tournées']["Round1"]['Temps de départ'] = a
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                continue
            if int(user_choice) != 1:
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- CLEAR STARTING TIME ROUND1
def clear_starting_time_round1():
    """Function to remove starting for round 1"""

    json_object['tournaments_db']['1']['Tournées']["Round1"]['Temps de départ'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 4. STOP ROUND1 GAMES - ENDING TIME -- GOOD MENU TRY EXCEPT /!!!!!\

## --  ADD ENDING TIME ROUND1
def add_ending_time_round1():
    """Function to add ending time for round1"""
    
    print("\n🚧 Souhaitez-vous arrêter les matches?.")
    while True:
        msg = "\nTaper [1] pour arrêter, ou taper [0] pour revenir au menu pécédent: "
        user_choice = input(msg)
        try:
            if int(user_choice) == 1:
                current_time = datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de terminer!")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                json_object['tournaments_db']['1']['Tournées']["Round1"]['Temps de fin'] = a
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
            if int(user_choice) != 1:
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## --  CLEAR ENDING TIME ROUND1
def clear_starting_time_round1():
    """Function to remove starting for round 1"""

    json_object['tournaments_db']['1']['Tournées']["Round1"]['Temps de fin'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 5. ADD & SAVE SCORES ROUND1 IN DB --

def save_round1_matchups():
    """ Function to generate and save round1 matchups based on players ratings only """

    # 1. Generate the 1st pairs of players for Round1
    a = players_matchup_reference_score_and_rating
    x = slice(0,4)
    y = slice(4,8)
    z = zip(a[x],a[y])

    ## -- Save Round1 matchups & rounds info in tournament_db table
    o = 1
    for g in z:
        json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'][f'Match{o}'] = tuple(g)
        ## -- to cleanup: key.clear()
        with open(filename, "w") as f:
            json.dump(json_object, f, indent=4)
        o += 1


""" Round 2 """

###### --- 1. GENERATE & SAVE ROUND2 MATCHUPS ---

## -- /!!! \ generate_players_matchup_with_reference_rating() and 
## -- generate_players_matchup_reference_score_and_rating() must REMAIN initiated 
## -- to allow generate_round1_matchups() to work /!!!\ 
def generate_save_round2_matchups():
    """ Function to generate and save round2 matchups based on players scores and rating from round1 games """

    # 1. Generate pairs of players for Round2
    a = players_matchup_reference_score_and_rating
    b = slice(0,8,2)
    c = slice(1,8,2)
    z = zip(a[b],a[c])
    
    ## -- Save Round2 matchups & rounds info in tournament_db table
    o = 1
    for g in z:
        json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'][f'Match{o}'] = tuple(g)
        with open(filename, "w") as f:
            json.dump(json_object, f, indent=4)
        o += 1
        ## -- Add players indexes from players_db table
    json_object['tournaments_db']['1']['Joueurs'] = [j for j in json_object['players_db']]
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)


###### --- 2. VIEW ROUND2 MATCHUPS FROM DB --

## -- Done ! --- 
def view_round2_matchups():
    """Function to view Round2 Matchups"""
    
    print("\n💡 Voici les Matches du Round2:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1


###### --- 3. LAUNCH ROUND2 GAMES - STARTING TIME --

## --  ADD STARTING TIME ROUND2
def add_starting_time_round2():
    """Function to add starting time for round2"""
    
    print("\n🚧 Êtes-vous prêt à lancer les matches?.")
    while True:
        msg = "\nTaper [1] pour commencer ou taper [0] pour revenir au menu pécédent: "
        user_choice = input(msg)
        try:
            if int(user_choice) == 1:
                current_time = datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de commencer!")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                json_object['tournaments_db']['1']['Tournées']["Round2"]['Temps de départ'] = a
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                continue
            if int(user_choice) != 1:
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## --  CLEAR STARTING TIME ROUND2
def clear_starting_time_round2():
    """Function to remove starting for round 2"""

    json_object['tournaments_db']['1']['Tournées']["Round2"]['Temps de départ'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 4. STOP ROUND2 GAMES - ENDING TIME --

## -- Done! --  ADD ENDING TIME ROUND2
def add_ending_time_round2():
    """Function to add ending time for round2"""
    
    print("\n🚧 Souhaitez-vous arrêter les matches?.")
    while True:
        msg = "\nTaper [1] pour arrêter, ou taper [0] pour revenir au menu pécédent: "
        user_choice = input(msg)
        try:
            if int(user_choice) == 1:
                current_time = datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de terminer!")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                json_object['tournaments_db']['1']['Tournées']["Round2"]['Temps de fin'] = a
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
            if int(user_choice) != 1:
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- Done! --  CLEAR ENDING TIME ROUND2
def clear_starting_time_round2():
    """Function to remove starting for round2"""

    json_object['tournaments_db']['1']['Tournées']["Round2"]['Temps de fin'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 5. ADD & SAVE SCORES ROUND2 IN DB --

def save_round2_scores():
    """ Function to generate and save round2 matchups based on players scores and rating from round2 games """

    # 1. Generate pairs of players for Round2
    a = players_matchup_reference_score_and_rating
    b = slice(0,8,2)
    c = slice(1,8,2)
    z = zip(a[b],a[c])
    
    ## -- Save Round2 matchups & rounds info in tournament_db table
    o = 1
    for g in z:
        json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'][f'Match{o}'] = tuple(g)
        with open(filename, "w") as f:
            json.dump(json_object, f, indent=4)
        o += 1


""" Round 3 """

###### --- 1. GENERATE & SAVE ROUND3 MATCHUPS ---

## -- To Do! -- /!!! \ generate_players_matchup_with_reference_rating() and 
## -- generate_players_matchup_reference_score_and_rating() must be REMAIN initiated
## -- to allow generate_round1_matchups() to work /!!!\ 
## -- Must rework the conditions to avoid players facing each other more than once  /!!!\ 
def generate_save_round3_matchups():
    """ Function to generate and save round3 matchups based on players scores and rating from round3 games """

    ## 1. Generate pairs of players for Round3
    a = players_matchup_reference_score_and_rating
    ## -- 1st player vs 2nd player
    b = slice(0,8,2)
    c = slice(1,8,2)
    z = zip(a[b],a[c])
    ## -- 1st player vs 3rd player
    d = a[0:8:2]
    e = a[1:8:2]
    d.extend(e)
    j = zip(d[b],d[c])
    ## 2. Save Round3 matchups & rounds info in tournament_db table
    o = 1
    for g in z:
        ## -- 1st player vs 2nd player
        q = json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'][f'Match{o}']
        s = json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'][f'Match{o}']
        json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}'] = tuple(g)
        r = json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}']
        if q != r and s != r:
            json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}'] = tuple(g)
            with open(filename, "w") as f:
                json.dump(json_object, f, indent=4)
        else:
            ## -- 1st player vs 3rd player
            h = 1
            for y in j:
                json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{h}'] = tuple(y)
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                h += 1
        o += 1
    ## -- Add players indexes from players_db table
    json_object['tournaments_db']['1']['Joueurs'] = [j for j in json_object['players_db']]
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
        ## -- Take 'em back to main menu.


###### --- 2. VIEW ROUND3 MATCHUPS FROM DB --

## -- Done ! --- 
def view_round3_matchups():
    """Function to view Round3 Matchups"""
    
    print("\n💡 Voici les Matches du Round3:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1


###### --- 3. LAUNCH ROUND3 GAMES - STARTING TIME --

## -- Done! --  ADD STARTING TIME ROUND3
def add_starting_time_round3():
    """Function to add starting time for round3"""
    
    print("\n🚧 Êtes-vous prêt à lancer les matches?.")
    while True:
        msg = "\nTaper [1] pour commencer ou taper [0] pour revenir au menu pécédent: "
        user_choice = input(msg)
        try:
            if int(user_choice) == 1:
                current_time = datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de commencer!")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                json_object['tournaments_db']['1']['Tournées']["Round3"]['Temps de départ'] = a
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                continue
            if int(user_choice) != 1:
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- Done! --  CLEAR STARTING TIME ROUND3
def clear_starting_time_round3():
    """Function to remove starting for round 3"""

    json_object['tournaments_db']['1']['Tournées']["Round3"]['Temps de départ'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 4. STOP ROUND3 GAMES - ENDING TIME --

## -- Done! --  ADD ENDING TIME ROUND3
def add_ending_time_round3():
    """Function to add ending time for round3"""
    
    print("\n🚧 Souhaitez-vous arrêter les matches?.")
    while True:
        msg = "\nTaper [1] pour arrêter, ou taper [0] pour revenir au menu pécédent: "
        user_choice = input(msg)
        try:
            if int(user_choice) == 1:
                current_time = datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de terminer!")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                json_object['tournaments_db']['1']['Tournées']["Round3"]['Temps de fin'] = a
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
            if int(user_choice) != 1:
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- Done! --  CLEAR ENDING TIME ROUND3
def clear_starting_time_round3():
    """Function to remove starting for round3"""

    json_object['tournaments_db']['1']['Tournées']["Round3"]['Temps de fin'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 5. ADD & SAVE SCORES ROUND3 IN DB --

def save_round3_scores():
    """ Function to generate and save round3 matchups based on players scores and rating from round3 games """

    ## 1. Generate pairs of players for Round3
    a = players_matchup_reference_score_and_rating
    ## -- 1st player vs 2nd player
    b = slice(0,8,2)
    c = slice(1,8,2)
    z = zip(a[b],a[c])
    ## -- 1st player vs 3rd player
    d = a[0:8:2]
    e = a[1:8:2]
    d.extend(e)
    j = zip(d[b],d[c])
    ## 2. Save Round3 matchups & rounds info in tournament_db table
    o = 1
    for g in z:
        ## -- 1st player vs 2nd player
        q = json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'][f'Match{o}']
        s = json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'][f'Match{o}']
        json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}'] = tuple(g)
        r = json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}']
        if q != r and s != r:
            json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}'] = tuple(g)
            with open(filename, "w") as f:
                json.dump(json_object, f, indent=4)
        else:
            ## -- 1st player vs 3rd player
            h = 1
            for y in j:
                json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{h}'] = tuple(y)
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                h += 1
        o += 1


""" Round 4 """

###### --- 1. GENERATE & SAVE ROUND4 MATCHUPS ---

## -- Done! -- /!!! \ generate_players_matchup_with_reference_rating() and 
## -- generate_players_matchup_reference_score_and_rating() must REMAIN initiated 
## -- to allow generate_round1_matchups() to work /!!!\ 
## -- Must rework the conditions to avoid players facing each other more than once  /!!!\ 
def generate_save_round4_matchups():
    """ Function to generate and save round3 matchups based on players scores and rating from round4 games """

    ## 1. Generate pairs of players for Round3
    a = players_matchup_reference_score_and_rating
    ## -- 1st player vs 2nd player
    b = slice(0,8,2)
    c = slice(1,8,2)
    z = zip(a[b],a[c])
    ## -- 1st player vs 3rd player
    d = a[0:8:2]
    e = a[1:8:2]
    d.extend(e)
    j = zip(d[b],d[c])
    ## 2. Save Round4 matchups & rounds info in tournament_db table
    o = 1
    for g in z:
        ## -- 1st player vs 2nd player
        q = json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'][f'Match{o}']
        s = json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'][f'Match{o}']
        p = json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}']
        json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'][f'Match{o}'] = tuple(g)
        r = json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'][f'Match{o}']
        if q != r and s != r and p != r :
            json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'][f'Match{o}'] = tuple(g)
            with open(filename, "w") as f:
                json.dump(json_object, f, indent=4)
        else:
            ## -- 1st player vs 3rd player
            h = 1
            for y in j:
                json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'][f'Match{h}'] = tuple(y)
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                h += 1
        o += 1
    ## -- Add players indexes from players_db table
    json_object['tournaments_db']['1']['Joueurs'] = [j for j in json_object['players_db']]
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)


###### --- 2. VIEW ROUND4 MATCHUPS FROM DB --

## -- Done ! --- 
def view_round4_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round4:\n")
    e = 1
    for x in list(json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'].values()):
        b = list(x.values())
        print(f"Match n°{e}: {b[0][0]} vs. {b[0][1]}")
        e +=1


###### --- 3. LAUNCH ROUND4 GAMES - STARTING TIME --

## -- Done! --  ADD STARTING TIME ROUND4
def add_starting_time_round4():
    """Function to add starting time for round4"""
    
    print("\n🚧 Êtes-vous prêt à lancer les matches?.")
    while True:
        msg = "\nTaper [1] pour commencer ou taper [0] pour revenir au menu pécédent: "
        user_choice = input(msg)
        try:
            if int(user_choice) == 1:
                current_time = datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de commencer!")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                json_object['tournaments_db']['1']['Tournées']["Round4"]['Temps de départ'] = a
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                continue
            if int(user_choice) != 1:
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- Done! --  CLEAR STARTING TIME ROUND4
def clear_starting_time_round4():
    """Function to remove starting for round4"""

    json_object['tournaments_db']['1']['Tournées']["Round4"]['Temps de départ'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 4. STOP ROUND4 GAMES - ENDING TIME --

## -- Done! --  ADD ENDING TIME ROUND4
def add_ending_time_round4():
    """Function to add ending time for round4"""
    
    print("\n🚧 Souhaitez-vous arrêter les matches?.")
    while True:
        msg = "\nTaper [1] pour arrêter, ou taper [0] pour revenir au menu pécédent: "
        user_choice = input(msg)
        try:
            if int(user_choice) == 1:
                current_time = datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de terminer!")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                json_object['tournaments_db']['1']['Tournées']["Round4"]['Temps de fin'] = a
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
            if int(user_choice) != 1:
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            print()


## -- Done! --  CLEAR ENDING TIME ROUND4
def clear_starting_time_round4():
    """Function to remove starting for round4"""

    json_object['tournaments_db']['1']['Tournées']["Round4"]['Temps de fin'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 5. ADD & SAVE SCORES ROUND4 IN DB --

def save_round4_scores():
    """ Function to generate and save round4 matchups based on players scores and rating from round4 games """

    ## 1. Generate pairs of players for Round3
    a = players_matchup_reference_score_and_rating
    ## -- 1st player vs 2nd player
    b = slice(0,8,2)
    c = slice(1,8,2)
    z = zip(a[b],a[c])
    ## -- 1st player vs 3rd player
    d = a[0:8:2]
    e = a[1:8:2]
    d.extend(e)
    j = zip(d[b],d[c])
    ## 2. Save Round4 matchups & rounds info in tournament_db table
    o = 1
    for g in z:
        ## -- 1st player vs 2nd player
        q = json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'][f'Match{o}']
        s = json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'][f'Match{o}']
        p = json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}']
        json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'][f'Match{o}'] = tuple(g)
        r = json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'][f'Match{o}']
        if q != r and s != r and p != r :
            json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'][f'Match{o}'] = tuple(g)
            with open(filename, "w") as f:
                json.dump(json_object, f, indent=4)
        else:
            ## -- 1st player vs 3rd player
            h = 1
            for y in j:
                json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'][f'Match{h}'] = tuple(y)
                with open(filename, "w") as f:
                    json.dump(json_object, f, indent=4)
                h += 1
        o += 1


""" START USER/PLAYERS MATCH/ROUNDS SCRIPT /!!!\ """

if __name__=="__main__":
    """Launch program to add/update players, macthes, and rounds"""

    print("\n===================== 👀 ===================\n")

else:
    pass