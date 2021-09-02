#! /user/bin/env python3
# -*- coding: utf-8 -*-


""" modules & packages """
import json
from dataclasses import dataclass, field
from tinydb import TinyDB, Query
import pandas as pd
import datetime
import pprint


""" players variables used in this file script """

total_number_of_players = 8
registered_players = 0
all_players_db = [] 

## -- 'db' allows to generate a DB file, 'db1.json', for this app --
db = TinyDB('db1.json', indent=4)
tournaments_table = db.table('tournaments_db')
players_table = db.table('players_db')

filename = "db1.json"
with open(filename, "r") as f:
    json_object = json.load(f)

## -- 'df' allows to update data in DB file --
df = pd.DataFrame(json_object['players_db'])
## - 'T' (Transpose) to use db indexes as table indexes for a better reading of data
real_db = df.T


## -- PPrint for internal use ONLY
pp = pprint.PrettyPrinter(indent=4)

""" # -- Prog Start Here -- """

## -- Done! -- Scores are added directly by the user in the DB file
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


## -- Done! --
def add_players():
    """ function to instantiate players"""
    
    print("\nEnregistrement des 8 joueurs...")
    # replace 3 by total_number_of_players -> range(1, total_number_of_players+1)
    for i in range(1,9):
        print(f"\nEntrer les informations sur le joueur n°{i}")
        p = Player(input("- Nom de famille: "),
                    input("- Prénom: "),
                    input("- Date de naissance telle que jj/mm/aaaa (ex: 18/02/1973): "),
                    input("- Sexe [H/F]: ").upper(),
                    int(input("- Classement: "))
                    )
        all_players_db.append(p.single_player_db)
        # print("-------------------------------------")
        print(f"\nJoueur n°{i} enregistré.")
    print("Fin de l'enregistrement des joueurs.\n")
# add_players()


""" Saving players data into db file /!!!\ """

## -- Done! --
def save_players_data():
    """ save players data """
    
    db = TinyDB(filename)
    players_table = db.table('players_db')
    players_table.truncate()
    players_table.insert_multiple(all_players_db)
# save_players_data()


## -- Done!
def save_players_indexes_in_tournaments_db():
    '''Function to save players indexes in tournament table in db file'''

    for i in range(len(list(json_object["players_db"]))):
        json_object["tournaments_db"]['1']['Joueurs'].append(list(json_object["players_db"])[i])
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
# save_players_indexes_in_tournaments_db()


""" View players data from db file /!!!\ """

## -- Done! --
def view_players_info():
    """ Function to view tournament info """
    
    print("\n📚 Voici les informations actuelles sur les joueurs\n")
    print(real_db)
view_players_info()


""" Update players data from db file /!!!\ """

## -- Done! -- Update Player last name in db file -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_lname():
    """ Function to update players last name in db file """

    print("\n🚧 Procédons à l'actualisation des données...")
    view_players_info()
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
                view_players_info()
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            view_players_info()
            print()
# update_player_lname()


## -- Done! -- Update Player first name in db file -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_fname():
    """ Function to update players first name in db file """

    print("\n🚧 Procédons à l'actualisation des données...")
    view_players_info()
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
                view_players_info()
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            view_players_info()
            print()
# update_player_fname()


## -- Done! -- Update Player gender in db file -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_gender():
    """ Function to update players gender in db file """

    print("\n🚧 Procédons à l'actualisation des données...")
    view_players_info()
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
                view_players_info()
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            view_players_info()
            print()
# update_player_gender()


## -- Done! -- Update Player birth date in db file -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_birth_date():
    """ Function to update players birth date in db file """

    print("\n🚧 Procédons à l'actualisation des données...")
    view_players_info()
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
                view_players_info()
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            view_players_info()
            print()
# update_player_birth_date()


## -- Done! -- Update Player rating in db file -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_rating():
    """ Function to update players rating in db file """

    print("\n🚧 Procédons à l'actualisation des données...")
    view_players_info()
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
                view_players_info()
            if int(user_choice) not in range(1,9):
                print(f"💡 Vous avez tapé [{user_choice}].\n")
                print()
            if int(user_choice) == 0:
                ## -- /!!!\ Send the user back to the former menu
                print("🏠 Retour au menu précédent...\n")
                break
        except:
            print(f"\n💥 Erreur de saisie...")
            view_players_info()
            print()
# update_player_rating()


## -- Done! -- Add Player score in db file -- /!!!\ At the end of the script, send the user back to the former menu
def add_player_score():
    """ Function to add players score in db file """
    
    print("\n🚧 Procédons à l'actualisation des données...")
    view_players_info()
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
                        view_players_info()
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
            view_players_info()
            print()
# add_player_score()


## -- Done! -- /!!!\ At the end of the script, send the user back to the former menu
def update_player_score():
    """ Function to update/add players score in db file """
    
    print("\n🚧 Procédons à l'actualisation des données...")
    view_players_info()
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
                                    view_players_info()
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
                            view_players_info()
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
            view_players_info()
            print()
# update_player_score()


## -- Done! --  /!!!\ be very careful with this one!
def erase_all_scores():
    """"Function removes all scores at once.  Better be carfeul with it!"""

    for r in range(8):
        real_db.iat[r,5] = []
        data = real_db.to_json(orient='index', indent=4)
        json_object['players_db'] = json.loads(data)
        with open(filename, "w") as f:
            json.dump(json_object, f, indent=4)
# erase_all_scores()


""" Var of Sorted Players Data """

## -- Unsorted Players by rating--
    # unsorted_players = {}
    # for s in json_object["players_db"].items():
        # print(s)
        # print(s[0])
        # print(list(s[1].values()))
        # y = s[0]
        # w = list(s[1].values())
        # unsorted_players[y] = w

## -- Done! -- Var - Sorted Players by score and rating
sorted_players_by_score_and_rating = sorted(json_object["players_db"].items(), key=lambda i: (sum(i[1]['Score']), int(i[1]['Classement'])), reverse=True)

## -- Done! -- Var - Sorted Players by rating
sorted_players_by_rating = sorted(json_object["players_db"].items(), key=lambda i: int(i[1]['Classement']), reverse=True)


""" View Ranked Players by Ratings & Scores """

## -- Done! -- Func - Ranked Players by score and rating
def view_sorted_players_by_score_and_rating():
    """View sorted players by score and rating"""

    print('\n🙂 Classement des joueurs par score et par nombre de points au classement général:\n')
    k=0
    for u in sorted_players_by_score_and_rating:
        print(f"N°{k+1}: {u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']}\t{u[1]['Classement']}\t{u[1]['Score']}")
        k +=1
# view_sorted_players_by_score_and_rating()


## -- Done! -- Func - Ranked Players by rating, Used ONLY for Round1
def view_sorted_players_by_rating():
    print('\n🙂 Classement des joueurs par nombre de points au classement général:\n')
    k=0
    for u in sorted_players_by_rating:
        print(f"N°{k+1}: {u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']}\t{u[1]['Classement']}")
        k +=1
# view_sorted_players_by_rating()


""" Var used to generate matchups """

# -- Rounds dict includes all rounds --
rounds = ''

# -- Players matchup reference_rating is used to sort items used to pair up players in a round1 ONLY
players_matchup_reference_rating = []

# -- Players matchup reference_score_and_rating is used to sort items used to pair up players
players_matchup_reference_score_and_rating = []


""" Generate Matches for Round1 """

## -- Done! -- /!!!\ DO NOT TOUCH IT - LEAVE IT ACTIVE /!!!\
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


## -- Done! --
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


## -- Done! --  /!!!\ DO NOT TOUCH IT - LEAVE IT ACTIVE /!!!\
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



## -- Done! -- /!!!\ LAUNCH ONLY ONCE, ELSE = SERIOUS ISSUE WITH DB !!! 
def adding_roundx_in_tournament_table():
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
        # json_object['tournaments_db']['1']['Tournées'].clear()
        json_object['tournaments_db']['1']['Tournées'].update(data)
        with open(filename, "w") as f:
            f.seek(0)
            json.dump(json_object, f, indent=4)
# adding_roundx_in_tournament_table()


## -- Done! --
def add_starting_time():
    """Function to add starting time for each round"""
    
    current_time = datetime.datetime.now()
    a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
    json_object['tournaments_db']['1']['Tournées']["Round1"]['Temps de départ'] = a
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
# add_starting_time()


## -- Done! --
def add_ending_time():
    """Function to add ending time for each round"""

    current_time = datetime.datetime.now()
    a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
    json_object['tournaments_db']['1']['Tournées']["Round1"]['Temps de fin'] = a
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)
# add_ending_time()


## -- Done! -- /!!! \ generate_players_matchup_with_reference_rating() and 
## -- generate_players_matchup_reference_score_and_rating() must be initiated 
## -- to allow generate_round1_matchups() to work /!!!\ 
def generate_round1_matchups():
    """ Function to generate and save round1 matchups based on players ratings only """

    # 1. Generate the 1st pairs of players for Round1
    a = players_matchup_reference_rating
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
# generate_round1_matchups()


""" /!!!\ Hint - View more details on matches/rounds/players from the tournament table in the db file:
    # i = 1
    # for m in list(z):
    #     print(json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'][f'Match{i}'][0][1])
    #     i += 1
    # print()
"""


## -- Done ! --- 
def view_round1_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round1:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1
view_round1_matchups()


## -- Done! -- /!!! \ generate_players_matchup_with_reference_rating() and 
## -- generate_players_matchup_reference_score_and_rating() must be initiated 
## -- to allow generate_round1_matchups() to work /!!!\ 
def generate_round2_matchups():
    """ Function to generate and save round2 matchups based on players ratings only """

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
# generate_round2_matchups()


## -- Done ! --- 
def view_round2_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round2:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1
view_round2_matchups()


## -- To Do! -- /!!! \ generate_players_matchup_with_reference_rating() and 
## -- generate_players_matchup_reference_score_and_rating() must be initiated 
## -- to allow generate_round1_matchups() to work /!!!\ 
## -- Must rework the conditions to avoid players facing each other more than once  /!!!\ 
def generate_round3_matchups():
    """ Function to generate and save round1 matchups based on players scores and rating """

    """
    ## -- Outcomes Scenarios (w: win, l: loss, t: tie):
        
        ## - Case 1:  4w   |   4l   |   0t
            ## create and sort (by score and rating) a win_list and a loss_list, then win_list.extend(loss_list)
            ## in order to generate next round games:
            ### win_list = ['w1', 'w2', 'w3', 'w4']
            ### loss_list = ['l1', 'l2', 'l3', 'l4']
            ### win_list.extend(loss_list)
            #### a = win_list // 'a' is the var used to create next round matchups
        
        ## - Case 2:  3w   |   3l   |   2t
            ## create and sort (by score and rating) a win_list, loss_list and a tie_list, then win_list.extend(loss_list + tie_list)
            ## in order to generate next round games:
            ### win_list = ['w1', 'w2', 'w3']
            ### loss_list = ['l1', 'l2', 'l3']
            ### tie_list = ['t1', 't2']
            ### win_list.extend(loss_list + tie_list)
            #### a = win_list // 'a' is the var used to create next round matchups
        
        ## - Case 3:  2w   |   2l   |   4t
            ## create and sort (by score and rating) a win_list, loss_list and a tie_list, then win_list.extend(loss_list + tie_list)
            ## in order to generate next round games:
            ### win_list = ['w1', 'w2']
            ### loss_list = ['l1', 'l2']
            ### tie_list = ['t1', 't2', 't3', 't4']
            ### win_list.extend(loss_list + tie_list)
            #### a = win_list // 'a' is the var used to create next round matchups
        
        ## - Case 4:  1w   |   1l   |   6t
            ## create and sort (by score and rating) a win_list, loss_list and a tie_list, then win_list.extend(loss_list + tie_list)
            ## in order to generate next round games:
            ### win_list = ['w1']
            ### loss_list = ['l1']
            ### tie_list = ['t1', 't2', 't3', 't4', 't5', 't6']
            ### win_list.extend(loss_list + tie_list)
            #### a = win_list // 'a' is the var used to create next round matchups
        
        ## - Case 5:  0w   |   0l   |   8t
            ## create and sort (by score and rating) a tie_list = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8']
            ## in order to generate next round games.
            ### a = tie_list // 'a' is the var used to create next round matchups
    
    """
    
    print("\n-- Scenarios Outcomes --\n")
    l = []
    for d in real_db['Score'].values:
        if d[0] == float(1):
            l.append(float(1))
    if len(l) == 4:
        print(f" Il y a en tout {len(l)} wins, c'est un cas1")
    elif len(l) == 3:
        print(f" Il y a en tout {len(l)} wins, c'est un cas2")
    elif len(l) == 2:
        print(f" Il y a en tout {len(l)} wins, c'est un cas3")
    elif len(l) == 1:
        print(f" Il y a en tout {len(l)} wins, c'est un cas4")
    elif len(l) == 0:
        print(f" Il y a en tout {len(l)} wins, c'est un cas5")
    else:
        print("error...")

    """

    # 1. Generate pairs of players for Roundx
    a = players_matchup_reference_score_and_rating
    b = slice(0,8,2)
    c = slice(1,8,2)
    z = zip(a[b],a[c])

    ## -- Save Round3 matchups & rounds info in tournament_db table
    o = 1
    for g in z:
        ##-- cleanup: json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'][f'Match{o}'].clear()
        q = json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'][f'Match{o}']
        s = json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'][f'Match{o}']
        json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}'] = tuple(g)
        r = json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}']
        if q != r and s != r:
            json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}'] = tuple(g)
            with open(filename, "w") as f:
                json.dump(json_object, f, indent=4)
        else:
            
            print("Ces joueurs se sont déjà affrontés dans ce tournoi...")
            print("Même si le programme continue, il faudra changer les scores manuellement...")
            ## -- Take 'em back to the main menu.
        o += 1

    """
generate_round3_matchups()

print("===")
# pp.pprint(json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'][f'Match1'])
# pp.pprint(json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'][f'Match1'][0][0][-1])
# pp.pprint(json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'][f'Match1'][0][3][0])
print('===')


## -- To Do... In progress
## -- To determine which scenario to choose so as to generate games for the next rounds !!!
def matchup_scenario():
    """Function to determine which scenario to choose so as to generate games for the next round"""
    
    ## May be better to use this in a generate_matches function !!!!
    l = []
    for d in real_db['Score'].values:
        if d[0] == float(1):
            l.append(float(1))
    if len(l) == 4:
        print(f" Il y a en tout {len(l)} wins, c'est un cas1")
    elif len(l) == 3:
        print(f" Il y a en tout {len(l)} wins, c'est un cas2")
    elif len(l) == 2:
        print(f" Il y a en tout {len(l)} wins, c'est un cas3")
    elif len(l) == 1:
        print(f" Il y a en tout {len(l)} wins, c'est un cas4")
    elif len(l) == 0:
        print(f" Il y a en tout {len(l)} wins, c'est un cas5")
    else:
        print("error...")


## -- Done ! --- 
def view_round3_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round3:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1
# view_round3_matchups()



## -- Done! -- /!!! \ generate_players_matchup_with_reference_rating() and 
## -- generate_players_matchup_reference_score_and_rating() must be initiated 
## -- to allow generate_round1_matchups() to work /!!!\ 
## -- Must rework the conditions to avoid players facing each other more than once  /!!!\ 
def generate_round4_matchups():
    """ Function to generate and save round1 matchups based on players ratings only """

    # 1. Generate pairs of players for Roundx
    a = players_matchup_reference_score_and_rating
    b = slice(0,8,2)
    c = slice(1,8,2)
    z = zip(a[b],a[c])
    ## -- Save Round2 matchups & rounds info in tournament_db table
    o = 1
    for g in z:
        ##-- cleanup: json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'][f'Match{o}'].clear()
        q = json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'][f'Match{o}']
        s = json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'][f'Match{o}']
        n = json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'][f'Match{o}']
        json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'][f'Match{o}'] = tuple(g)
        r = json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'][f'Match{o}']
        if q != r and s != r and n != r:
            json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'][f'Match{o}'] = tuple(g)
            with open(filename, "w") as f:
                json.dump(json_object, f, indent=4)
        else:
            print("Ces joueurs se sont déjà affrontés dans ce tournoi...")
            print("Même si le programme continue, il faudra changer les scores manuellement...")
            ## -- Take 'em back to the main menu.
        o += 1
# generate_round4_matchups()


## -- Done ! --- 
def view_round4_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round4:\n")
    e = 1
    for x in list(json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'].values()):
        b = list(x.values())
        print(f"Match n°{e}: {b[0][0]} vs. {b[0][1]}")
        e +=1
# view_round4_matchups()



"""Use this to verify if players have already played againts each other:

    ## -- To create 28 Unique GAMES with 7 Rounds, 4 games/round

    challengers=['p1','p2','p3','p4','p5','p6','p7','p8']
    # challengers = sorted_challengers_by_rankings
    matches=[]
    challenger1=0
    while challenger1<len(challengers):
        challenger2=challenger1+1    # start
        while challenger2<len(challengers):
            matches.append((challengers[challenger1],challengers[challenger2]))
            challenger2+=1
        challenger1+=1

    print("\n--- ___ ---")
    print(f"\nThere is a total of '{len(matches)}' matches:\n")
    for m in matches:
        print(m)

"""



"""Hint on different var used in this program
    #### --- PROJECTS VAR ---
    # player = [lname, fname, date_of_birth, gender, rating, player_id, [player_scores]]
    # match = (["playerX_id, playerX_scores"], ["playerY_id, playerY_scores"]) 
    # round1 = ['round_name', start_date_hour, [match1, match2, match3, match4], end_date_hour]


    ## -- round[z] = ['name', start_date_hour, [match1, match2, match3, match4], end_date_hour]
    ## - "name" = json_object['tournaments_db']['1']['Tournées']["Round1"]
    ## - "start_date_hour" = json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches']
    ## - "[match1, match2, match3, match4]" = json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches']
    ## - "end_date_hour" = json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches']

    ## -- Print tournament table...
    print()
    pp.pprint(json_object['tournaments_db']['1']['Tournées'])
"""

""" START USER/PLAYERS MATCH/ROUNDS SCRIPT /!!!\ """

if __name__=="__main__":
    """Launch program to add/update players, macthes, and rounds"""

    # -- Done!
    # -- Add & Save Players to DB file --
    # add_players()
    # save_players_data()
    
    # -- Done!
    # -- generate/View Round1 Matchups & Save them to db file --
    # view_unsorted_players_list()
    # view_sorted_players_list_by_rating()
    # view_ranked_players_by_rating_only()
    # view_ranked_players_by_score_and_rating()

    # -- Done!
    # -- The next functions MUST be initiated in order to save data in db file --
    # generate_players_matchup_with_reference_rating()
    # generate_players_matchup_reference_score_and_rating()
    # generate_matchups()
    # view_round1_matchups()
    # save_rounds_in_db()
    # view_rounds_in_db()

    # view_ranked_players_by_score_and_rating()

    # -- To be done!
    # -- UPDATE SCORE --

    # print(json_object["players_db"].keys())
    # print(json_object["players_db"]["1"]['Sexe'])
    # print(range(len(json_object["players_db"].keys())))
    # for a in range(len(json_object["players_db"].keys())):
    #     print(a+1)

    # -- creating a function to collect score from the user
    def ask_player_index():
        print("Pour entrer un score")
        ask_index = input("Veuillez taper le numéro du membre, svp: ")
        try: 
            if int(ask_index)>0 or int(ask_index)<=range(len(json_object["players_db"].keys())): 
                ask_score = float(input(f'Taper le score de {json_object["players_db"][str(ask_index)]["Nom de famille"]}: '))
                with open('tournament_data.json', "w") as f:
                    # Being corrected... we should not append but make an addition to a ditc instead --> line 447
                    json_object["players_db"][str(ask_index)]["Score"].append(ask_score)
                    json.dump(json_object, f, indent=4)
            else:
                print("Mauvaise saisie...")
                return ask_player_index()
        except:
            print("Mauvaise saisie...")
            return ask_player_index()

    # ask_player_index()
    # print("\n--- En résumé ---")
    # print(f'Scores de {json_object["players_db"]["1"]["Nom de famille"]}: {json_object["players_db"]["1"]["Score"]}')
    # print(f'Score Final de {json_object["players_db"]["1"]["Nom de famille"]} dans ce tournoi: {sum(json_object["players_db"]["1"]["Score"])}')

    # -- Save Round1 data in tournaments_db -- 
    # 1. Generate the 1st pairs of players in Round 1
    # a = players_matchup_reference_score_and_rating
    # x = slice(0,4)
    # y = slice(4,8)
    # z = zip(a[x],a[y])
    
    # 2. Add Round1 matchups to tournament rounds instance
    # round1_matchups = {}
    # i = 1
    # for m in list(z):
    #     round1_matchups[f"Match n°{int(i)}"] = m
    #     i += 1
    # rounds["Round1"] = round1_matchups
    
    # 3. Open and save rounds data in tournament_db table
    # with open('tournament_data.json', "w") as f:
    #     json_object["tournaments_db"]["1"]['Tourn\u00e9es']= rounds
    #     json.dump(json_object, f, indent=4)

    # print("\---")
    # print(rounds)
    # print("\---")
    # print(rounds.items())
    # print("\---")
    # print(rounds.keys())
    # print("\---")
    # print(rounds.values())



    """
    for k in json_object["tournaments_db"]["1"]['Tourn\u00e9es'].items():
        print(k)
        print("---")
        print(k[0])
        print("---")
        print(k[1]['Match n°1'])
        print("---")
        print(k[1]['Match n°1'][0])
        print("---")
        print(k[1]['Match n°1'][0][1])

    # -- OUTPUT:
    
    ('Round1', {'Match n°1': [['1', 4.0], ['8', 0]], 'Match n°2': [['7', 1.0], ['3', 0]], 'Match n°3': [['6', 0], ['2', 0]], 'Match n°4': [['4', 0], ['5', 0]]})
    ---
    Round1
    ---
    [['1', 4.0], ['8', 0]]
    ---
    ['1', 4.0]
    ---
    4.0
    """


    """
    p_score = json_object["players_db"]["i"]["Score"] , 'i' is a player's index in the table

    def ask_player_index():
        ask_index = int(input("Taper le score du membre n°: "))
        
        if (ask_index+1) in range(len(json_object["players_db"].keys())):
            ask_score = int(input(f"Quel est le score du membre n°{ask_index}: "))
            print(json_object["players_db"]["(ask_index)"]["Score"])
            # json_object["players_db"]["(ask_index)"]["Score"] = ask_score

    """


    """ 
    We wanna get players db 'round1_matchups[i]' to update them:
    🏁 Les matches du Round1 🏁
    Match n°1: [['6', 0], ['3', 0]]
    Match n°2: [['7', 0], ['2', 0]]
    Match n°3: [['4', 0], ['1', 0]]
    Match n°4: [['8', 0], ['5', 0]]
    🚧 Match n°x: ([n° membre, son score], [n° autre membre, son score]) 🚧
    -------------------------------------------------------------------------
    - Joueurs Triés par Score et Classement Général-
    Membre n°6: Brenn Nzimbi  est actuellement n°1 avec un score de 0
    Membre n°7: Alexia Laville  est actuellement n°2 avec un score de 0
    Membre n°4: Mary Gendre  est actuellement n°3 avec un score de 0
    Membre n°8: Corine Lafarge  est actuellement n°4 avec un score de 0
    Membre n°3: John Hamel  est actuellement n°5 avec un score de 0
    Membre n°2: Lionel Prudom  est actuellement n°6 avec un score de 0
    Membre n°1: Paul Lyons  est actuellement n°7 avec un score de 0
    Membre n°5: Sophia Gaillard  est actuellement n°8 avec un score de 0
    """

    """ /!!!\ Updates must be done in players_db table and seen in tournaments_db table in db file """
    # -- To update scores, DO NOT USE use the following var:
    # -- r = json_object["tournaments_db"]["1"]["Tourn\u00e9es"]["Round"+str(i)].... [player score]; use this to view score only
    # -- INSTEAD use the following var:
    
    # -- p_score = json_object["players_db"]["i"]["Score"] , 'i' is a player's index in the table

    # -- I gotta show up player index in matchups to allow user to allocate proper point to a specific player
    # -- And user input then shall be automatically seen in tournament_db table too
    # -- ex: Input Macth n°1 player1_name score: ...> player with 1st rating ...> use 'sorted_players_by_rating' to know pl ranking
    # -- ex: Input Macth n°1 player5_name score: ...> player with 5th rating ...> 
    # -- ex: Input Macth n°2 player2_name score: ...> player with 2nd rating ...> 
    # -- ex: Input Macth n°2 player6_name score: ...> player with 6th rating ...> 
    # -- ex: Input Macth n°3 player3_name score: ...> player with 3rd rating ...> 
    # -- ex: Input Macth n°3 player7_name score: ...> player with 7th rating ...> 
    # -- ex: Input Macth n°4 player4_name score: ...> player with 4th rating ...> 
    # -- ex: Input Macth n°4 player8_name score: ...> player with 8th rating ...> 
    
    # print("\n================== 🤓 Round1 🏁 Matchups 🥸 ================\n")
    # for i in range(len(rounds["Round1"])):
    #     print(f"Match n°{i+1}: {rounds['Round1'][i]}")

    """ /!!!\ 'all_players_db' must be sorted before saving it to db file"""
    # print(all_players_db) # -- all_players_db msut be sorted before saving it to db file
    
    # t= sorted_players_by_rating
    # d = slice(0,4)
    # e = slice(4,8)
    
    # c = t[d]
    # print(c)
    # print(c[0])
    # print(c[0][0]) # player name
    # print(c[0][1]) # player rating
    # print(c[0][2]) # player score
    # print(c[0][3]) # player index
    # print(t[d][0][3]) # player index

    """ Here's a solution """
    # -- t[d][0][3] must be used as in index in 'players_db["player index"]["Score"]'
    # -- Thus: players_db[str(t[d][0][3])]["Score"]
    # -- Then, the user shall input: 'players_db[str(t[d][0][3])]["Score"]: '


    # Unique match format = (["playerX_reference, playerX_scores"], ["playerY_reference, playerY_scores"])
    # which is: round1_matchups[i]

    # -- To start saving to DB file
    # save_initial_data()

    # print(all_players_db)

    # -- to get the names of tables in db:
    # for s in json_object.keys():
    #     print(s[0:])

    # print(json_object["players_db"].items())

    # -- to get indexes from t_players table separately:
    # for s in json_object["players_db"].items():
    #     print(s[0])
    # or in json_object list:
    # print(list(json_object.items())[0][1].keys())


    # =======================
    """ -- UPDATING DB -- """

    # -- Get player's record:
    # print("\n--- before udate -- ")
    # print(json_object["players_db"]["1"]['Nom de famille'])
    # print(json_object["players_db"]["2"]['Nom de famille'])
    
    # # -- Open file to update them
    # with open('tournament_data.json', "r") as f:
    #     json_object = json.load(f) 
    #     json_object["players_db"]["1"]['Nom de famille'] = "Renard"
    #     json_object["players_db"]["2"]['Nom de famille'] = "Poisson"

    # # -- save update
    # with open('tournament_data.json', "w") as f:
    #     json.dump(json_object, f, indent=4)
    
    # -- print data updated 
    # print("\n--- after update -- ")
    # print(json_object["players_db"]["1"]['Nom de famille'])
    # print(json_object["players_db"]["2"]['Nom de famille'])

    # print("\n---")
    # print(json_object["players_db"].items())
    # print("---\n")
    # for s in json_object["players_db"].items():
    #     # print(s[1].values())
    #     print(s)
    #     print(s[1].keys())
    #     print(list(s[1].keys()))
    #     print(s[1]['Nom de famille']) # to update scores, i must change "s[1]['Nom de famille']" from dict "json_object["players_db"].items()"
    # print("\n")
    # print(json_object["players_db"].items()[1]['Nom de famille'])


    # =====================================
    # -- wtih pandas: BEST TABLE VIEW --- #
    # print("\n")
    # # df = pd.DataFrame.from_dict(json_object["players_db"], orient='index')
    # print(df)
    # print("\n")

    # print("\n  -- Tableau des joueurs --")
    # print("-----------------------------")
    # # unsorted players data
    # df = pd.DataFrame.from_dict(json_object["players_db"], orient='index')
    # print(df)
    # print("\n  - Tri des joueurs par points au 'Classement' général -")
    # print("---------------------------------------------------------")
    # # # sorting players data by rating
    # x = df.sort_values(by=['Classement'], ascending=False)
    # print(x)
    # print("\n")

    # # sorting data
    # print("\n-- Sorting Data by RATING--\n")
    # # x = df.sort_values(by=['Classement'], ascending=False)
    # print(x)
    # print("\n")

    # to sort players:
    # def pl_by_name(p):
    #     return p

    # def pl_by_rating(p):
    #     return p.rating

    # def pl_by_score(p):
    #     return sum(p.scores)

    # players_by_name = sorted(all_players_db, key=pl_by_name)
    # print(players_by_name)

    # from operator import attrgetter
    # s_players = sorted(all_players_db, key=attrgetter("Nom de famille"))


    # print("Voici la liste des joueurs enregistés:\n")
    # for p in all_players_db:
    #     print(p)
    # print("\n--\n")
    # print(all_players_db)

    # -- End of program - Goodbye message.
    # print("---------------------------------------------------------------------------")
    print("\n===================== 👀 ===================\n")

else:
    # view_unsorted_players_list()


    # -- 'generate_matchups' must be on so that rounds instance can be used in tournament.py:
    # generate_matchups()
    
    # view_round1_matchups()
    pass