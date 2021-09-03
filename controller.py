#! /user/bin/env python3
# -*- coding: utf-8 -*-


""" modules & packages """
import json
from dataclasses import dataclass, field
from tinydb import TinyDB
import pandas as pd
import datetime

from model import Player, Tournament


########################### TOURNAMENT VARIABLES & TOOLS ########################

""" tournament variables used to launch the script """
tournaments = []

""" players variables used in this file script """

total_number_of_players = 8
registered_players = 0
all_players_db = [] 

## -- 'db' allows to generate a DB file, './data/data.json', for this app --
db = TinyDB('./data/data.json', indent=4)
tournaments_table = db.table('tournaments_db')
players_table = db.table('players_db')

filename = "./data/data.json"
with open(filename, "r") as f:
    json_object = json.load(f)

## -- 'df' allows to update data in DB file --
df = pd.DataFrame(json_object['players_db'])
## - 'T' (Transpose) to use db indexes as table indexes for a better reading of data
real_db = df.T


########################### TOURNAMENT MANAGEMENT ########################

"""Add/Save Tournament"""

# -- Add Tournament -- /!!!\ ADD AN END DATE WHICH IS ADDED AUTOMATICALLY AT THE END OF THE TOURNAMENT !!!
def add_tournament():
    """ Function to instantiate tournament"""
    
    print(f"\n🚀 Veuillez entrer les informations suivantes sur le tournoi: ")
    p = Tournament(input("- Nom: "), 
                    input("- Lieu: "),
                    input("- Date, telle que jj/mm/aaaa (ex: 18/02/2022): "),
                    input("- Quel est votre Contrôle du temps? 'Bullit', 'Blitz' ou 'Coup Rapide'"),
                    input("- Description: ")
                    )
    print("\n🤓 Bravo! Le tournoi a bien été enregistré.\n")


# -- Save First Tournament Info --
def save_tournament_data():
    """ save tournament data """
    db = TinyDB('../data/data.json')
    tournaments_table = db.table('tournaments_db')
    tournaments_table.truncate()  # clear up the table first
    tournaments_table.insert_multiple(tournaments)


"""Update Tournaments properties"""

# -- Done! -- Update Tournament Name in db file --
def update_tournament_name():
    """ Function to update Tournament Name in db file """

    print(f"\nLe nom actuel du tournoi est: {json_object['tournaments_db']['1']['Nom du tournoi']}\n")
    json_object['tournaments_db']['1'].update({"Nom du tournoi": str(input("Quel est le nouveau nom du tournoi? "))})
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
    print(f"\nLe nouveau nom du tournoi est: {json_object['tournaments_db']['1']['Nom du tournoi']}")
    ## -- Send the user back to the main menu


# -- Done! -- Update Tournament Location in db file --
def update_tournament_location():
    """ Function to update Tournament Location in db file """

    print(f"\nLe nom actuel du lieu où se déroule tournoi est: {json_object['tournaments_db']['1']['Lieu']}\n")
    json_object['tournaments_db']['1'].update({"Lieu": str(input("Quel est le nom du lieu où se déroule tournoi? "))})
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
    print(f"\nNouveau nom du lieu actualisé: {json_object['tournaments_db']['1']['Lieu']}")
    ## -- Send the user back to the main menu


# -- Done! -- Update Tournament Date in db file --
def update_tournament_date():
    """ Function to update Tournament Date in db file """

    print(f"\nLe date actuelle du tournoi est: {json_object['tournaments_db']['1']['Date']}\n")
    json_object['tournaments_db']['1'].update({"Date": str(input("Quelle la vraie date du tournoi (jj/mm/aaaa)? "))})
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
    print(f"\nNouvelle date: {json_object['tournaments_db']['1']['Date']}")
    ## -- Send the user back to the main menu


# -- Done! -- Update Tournament Number of Turns in db file --
def update_tournament_number_of_turns():
    """ Function to update Tournament Number of Turns in db file """

    print(f"\nLe nombre actuel de tours est: {json_object['tournaments_db']['1']['Nombre de tours']}\n")
    json_object['tournaments_db']['1'].update({"Nombre de tours": str(input("Quel est le nombre de tours (en chiffre)? "))})
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
    print(f"\nNouveau Nombre de Tours: {json_object['tournaments_db']['1']['Nombre de tours']}")
    ## -- Send the user back to the main menu


# -- Done! -- Update Tournament Rounds in db file 
# --- Automatic Process... Check it when rounds are created --
def update_tournament_rounds():
    """ Function to update Tournament Rounds in db file """

    print(f"\nLes tournées sont: {json_object['tournaments_db']['1']['Tournées']}\n")
    ## -- Append rounds from players_db table
    json_object['tournaments_db']['1']['Tournées'].update(json_object['players_db']['1']['Tournées'])
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
    print(f"\nNouvelles Tournées: {json_object['tournaments_db']['1']['Tournées']}")
    ## -- Send the user back to the main menu


# -- Done! -- Update Tournament Players Indexes in db file
# --- Automatic Process... Check it when player instances are created --
def update_tournament_players_info():
    """ Function to update Tournament Players Indexes in db file """

    print(f"\nLes indices des joueurs sont: {json_object['tournaments_db']['1']['Joueurs']}\n")
    ## -- Append players indexes from players_db table
    json_object['tournaments_db']['1']['Joueurs'].append(json_object['players_db']['1']['Joueurs'])
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
    print(f"\nNouveaux Joueurs: {json_object['tournaments_db']['1']['Joueurs']}")
    ## -- Send the user back to the main menu


# -- Done! -- Update Tournament Time Control in db file --
def update_tournament_time_control():
    """ Function to update Tournament Time Control in db file """

    print(f"\nLe Contrôle du temps actuel est: {json_object['tournaments_db']['1']['Contrôle du temps']}\n")
    json_object['tournaments_db']['1'].update({"Contrôle du temps": str(input("Quel est le Contrôle du temps? "))})
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
    print(f"\nNouveau Contrôle du temps: {json_object['tournaments_db']['1']['Contrôle du temps']}")
    ## -- Send the user back to the main menu


# -- Done! -- Update Tournament Description in db file --
def update_tournament_time_description():
    """ Function to update Tournament Time Control in db file """

    print(f"\nLa description actuelle est: {json_object['tournaments_db']['1']['Description']}\n")
    json_object['tournaments_db']['1'].update({"Description": str(input("Quelle est la description? "))})
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
    print(f"\nNouvelle Description: {json_object['tournaments_db']['1']['Description']}")
    ## -- Send the user back to the main menu


# -- Done! -- Update User Tournalent Input in db file --
def update_tournament_info():
    """Menu to update tournament info"""
    
    while True:
        print("\nVoici les informations actuelles sur le tournoi.")
        print("Taper le chiffre de votre choix pour effectuer une modification:\n")
        h = 1
        for i in json_object['tournaments_db']['1']:
            if h!=5 and h!=6:
                print(f"{[h]} {i}: {json_object['tournaments_db']['1'][i]}")
            h += 1
        print("[0] Menu Principal.")
        
        user_choice = input("\nTaper votre choix: ")
        if user_choice == "1":
            print("\n--------------------------------------------------")
            print(json_object['tournaments_db']['1']['Nom du tournoi'])
            update_tournament_name()
        elif user_choice == "2":
            print("\n--------------------------------------------------")
            print(json_object['tournaments_db']['1']['Lieu'])
            update_tournament_location()
        elif user_choice == "3":
            print("\n--------------------------------------------------")
            print(json_object['tournaments_db']['1']['Date'])
            update_tournament_date()
        if user_choice == "4":
            print("\n--------------------------------------------------")
            print(json_object['tournaments_db']['1']['Nombre de tours'])
            update_tournament_number_of_turns()
        elif user_choice == "5":
            print("\n--------------------------------------------------")
            print(json_object['tournaments_db']['1']['Tournées'])
            update_tournament_rounds()
        elif user_choice == "6":
            print("\n--------------------------------------------------")
            print(json_object['tournaments_db']['1']['Joueurs'])
            update_tournament_players_info()
        elif user_choice == "7":
            print("\n--------------------------------------------------")
            print(json_object['tournaments_db']['1']['Contrôle du temps'])
            update_tournament_time_control()
        elif user_choice == "8":
            print("\n--------------------------------------------------")
            print(json_object['tournaments_db']['1']['Description'])
            update_tournament_time_description()
        elif user_choice == "0":
            print("\n--------------------------------------------------")
            print("Retour au Menu Principal")
            break
        else:
            print("\n==================================================")
            print(f"Vous avez tapé '{user_choice}'.\nChoisissez à nouveau un chiffre sur le menu, svp.\n")

    ## -- DO NOT ERASE THESE -- scripts used to update functions above --
        # with open(filename, "r") as f:
        #     json_object = json.load(f)
        # print(json_object['tournaments_db']['1'])
        # print()
        # print(json_object['tournaments_db']['1']['Nom du tournoi'])
        # print(json_object['tournaments_db']['1']['Lieu'])
        # print(json_object['tournaments_db']['1']['Date'])
        # print(json_object['tournaments_db']['1']['Nombre de tours'])
        # print(json_object['tournaments_db']['1']['Tournées'])
        # print(json_object['tournaments_db']['1']['Joueurs'])
        # print(json_object['tournaments_db']['1']['Contrôle du temps'])
        # print(json_object['tournaments_db']['1']['Description'])
        # print("\n-- Current Tournament Info --\n")
        # for i in json_object['tournaments_db']['1']:
        #     print(f"{i}: {json_object['tournaments_db']['1'][i]}")
        # print("--")


########################### PLAYERS MANAGEMENT ########################

## -- Done! --
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

## -- Done! --
def save_players_data():
    """ save players data """
    
    db = TinyDB(filename)
    players_table = db.table('players_db')
    players_table.truncate()
    players_table.insert_multiple(all_players_db)


## -- Done!
def save_players_indexes_in_tournaments_db():
    '''Function to save players indexes in tournament table in db file'''

    for i in range(len(list(json_object["players_db"]))):
        json_object["tournaments_db"]['1']['Joueurs'].append(list(json_object["players_db"])[i])
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)


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


## -- Done! --  /!!!\ be very careful with this one!
def erase_all_scores():
    """"Function removes all scores at once.  Better be carfeul with it!"""

    for r in range(8):
        real_db.iat[r,5] = []
        data = real_db.to_json(orient='index', indent=4)
        json_object['players_db'] = json.loads(data)
        with open(filename, "w") as f:
            json.dump(json_object, f, indent=4)


""" Var of Sorted Players Data """

## -- Done! -- Var - Sorted Players by score and rating
sorted_players_by_score_and_rating = sorted(json_object["players_db"].items(), key=lambda i: (sum(i[1]['Score']), int(i[1]['Classement'])), reverse=True)

## -- Done! -- Var - Sorted Players by rating
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


## -- Done! -- /!!!\ LAUNCH ONLY ONCE, ELSE = SERIOUS ISSUE WITH DB !!! 
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


""" Generate & Save Matchups & Scores """

""" Round 1 """

###### --- 1. GENERATE & SAVE ROUND1 MATCHUPS --- FIRST LAUNCH 'add_roundx_in_tournament_table()'

## -- Done! -- /!!! \ generate_players_matchup_with_reference_rating() and 
## --- generate_players_matchup_reference_score_and_rating() must REMAIN initiated 
## ---- to allow generate_round1_matchups() to work /!!!\ --
def generate_save_round1_matchups():
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
        with open(filename, "w") as f:
            json.dump(json_object, f, indent=4)
        o += 1


###### --- 2. VIEW ROUND1 MATCHUPS FROM DB --
'''
def view_round1_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round1:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1
'''

###### --- 3. LAUNCH ROUND1 GAMES - STARTING TIME -- GOOD MENU TRY EXCEPT /!!!!!\

## -- ADD STARTING TIME ROUND1 --
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


## -- CLEAR STARTING TIME ROUND1 --
def clear_starting_time_round1():
    """Function to remove starting for round 1"""

    json_object['tournaments_db']['1']['Tournées']["Round1"]['Temps de départ'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 4. STOP ROUND1 GAMES - ENDING TIME -- GOOD MENU TRY EXCEPT /!!!!!\

## -- ADD ENDING TIME ROUND1 --
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


## -- CLEAR ENDING TIME ROUND1 --
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

## -- /!!! \ First, generate_players_matchup_with_reference_rating() and 
## --- generate_players_matchup_reference_score_and_rating() must REMAIN initiated 
## ---- to allow generate_round1_matchups() to work /!!!\ --
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


###### --- 2. VIEW ROUND2 MATCHUPS FROM DB --
'''
def view_round2_matchups():
    """Function to view Round2 Matchups"""
    
    print("\n💡 Voici les Matches du Round2:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1
'''

###### --- 3. LAUNCH ROUND2 GAMES - STARTING TIME --

## -- ADD STARTING TIME ROUND2 --
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


## -- CLEAR STARTING TIME ROUND2 --
def clear_starting_time_round2():
    """Function to remove starting for round 2"""

    json_object['tournaments_db']['1']['Tournées']["Round2"]['Temps de départ'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 4. STOP ROUND2 GAMES - ENDING TIME --

## -- ADD ENDING TIME ROUND2 --
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


## -- CLEAR ENDING TIME ROUND2 --
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

## -- /!!! \ First, generate_players_matchup_with_reference_rating() and 
## --- generate_players_matchup_reference_score_and_rating() must be REMAIN initiated
## ---- to allow generate_round1_matchups() to work /!!!\ 
## ----- Must rework the conditions to avoid players facing each other more than once  /!!!\ 
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
        ## -- Take 'em back to main menu.


###### --- 2. VIEW ROUND3 MATCHUPS FROM DB --
'''
def view_round3_matchups():
    """Function to view Round3 Matchups"""
    
    print("\n💡 Voici les Matches du Round3:\n")
    e = 1
    d = list(json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1
'''

###### --- 3. LAUNCH ROUND3 GAMES - STARTING TIME --

## -- ADD STARTING TIME ROUND3 --
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


## -- CLEAR STARTING TIME ROUND3 --
def clear_starting_time_round3():
    """Function to remove starting for round 3"""

    json_object['tournaments_db']['1']['Tournées']["Round3"]['Temps de départ'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 4. STOP ROUND3 GAMES - ENDING TIME --

## -- ADD ENDING TIME ROUND3 --
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


## -- CLEAR ENDING TIME ROUND3 --
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

## -- /!!! \ First, generate_players_matchup_with_reference_rating() and 
## --- generate_players_matchup_reference_score_and_rating() must REMAIN initiated 
## ---- to allow generate_round1_matchups() to work /!!!\ 
## ----- Must rework the conditions to avoid players facing each other more than once  /!!!\ --
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


###### --- 2. VIEW ROUND4 MATCHUPS FROM DB --
'''
def view_round4_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round4:\n")
    e = 1
    for x in list(json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'].values()):
        b = list(x.values())
        print(f"Match n°{e}: {b[0][0]} vs. {b[0][1]}")
        e +=1
'''

###### --- 3. LAUNCH ROUND4 GAMES - STARTING TIME --

## -- ADD STARTING TIME ROUND4 --
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


## -- CLEAR STARTING TIME ROUND4 --
def clear_starting_time_round4():
    """Function to remove starting for round4"""

    json_object['tournaments_db']['1']['Tournées']["Round4"]['Temps de départ'] = ""
    with open(filename, "w") as f:
        # f.seek(0)
        json.dump(json_object, f, indent=4)


###### --- 4. STOP ROUND4 GAMES - ENDING TIME --

## -- ADD ENDING TIME ROUND4 --
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


## -- CLEAR ENDING TIME ROUND4 --
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


########################### MENUS MANAGEMENT ########################

## -- Main Menu --
def exec_main_menu1():
    """ function to launch main menu within the current file"""

    def main_menu():
        """ Main Menu interface """
        # Main menu: [1]Tournament | [2]Players | [3]Reports | [4]Exit
        a = "\n 🏁 GESTIONNAIRE DE TOURNOI D'ECHECS 🏁"
        b = "\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        c = "\n~~~~~~~~~~ 🏠 MENU PRINCIPAL ~~~~~~~~~~~~"
        x = "\n Entrer le chiffre:"
        d = "\n [1] pour Tournoi       [2] pour Joueurs"
        f = "\n [3] pour Rapports      [4] pour Arrêter"
        g = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        menu = a+b+c+x+d+f+g
        print(menu)
            
    while True:
        """ Launching Program """
        main_menu()
        user_choice = input("\nTaper votre choix: ")
        if user_choice == "1":
            print('choice 1: go to tournament_menu')
            # menu_tournament.exec_t_menu2()
        elif user_choice == "2":
            print('choice 2: go to players_menu')
            # menu_players.exec_p_menu2()
        elif user_choice == "3":
            print('choice 3: go to reports_menu')
            # menu_reports.exec_r_menu2()
        elif user_choice == "4":
            print("Merci d'avoir utilisé notre programme et à bientôt 😉")
            break
        else:
            print(f"😅 Vous avez taper '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 4.\n")
# exec_main_menu1()


## -- Players Menu --
def exec_p_menu1():
    """ function to launch players menu within the current file"""

    def players_menu():
        """ Menu interface """
        # Players menu: [1]Create | [2]Open | [3]Go Back | [4]Exit
        c = "\n---------- 🔥 MENU JOUEURS 🔥 -------------"
        x = "\nEntrer le chiffre:"
        d = "\n[1] pour Créer            [2] pour Ouvrir"
        f = "\n[3] pour Menu Principal   [4] pour Arrêter\n"
        menu = c+x+d+f
        print(menu)

    while True:
        """ Launching Program """
        players_menu()
        user_choice = input("\nTaper votre choix: ")
        if user_choice == "1":
            print('choice 1: go to tournament_menu')
            # menu_tournament.exec_t_menu2()
        elif user_choice == "2":
            print('choice 2: go to players_menu')
            # menu_players.exec_p_menu2()
        elif user_choice == "3":
            print('choice 3: go to reports_menu')
            # menu_reports.exec_r_menu2()
        elif user_choice == "4":
            print("Merci d'avoir utilisé notre programme et à bientôt 😉")
            break
        else:
            print(f"😅 Vous avez taper '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 4.\n")
# exec_p_menu1()


## -- Reports Menu --
def exec_r_menu1():
    """ function to launch reports menu within the current file"""

    def reports_menu():
        """ Menu interface """
        # Reports menu: [1]Actors | [2]Players | [3]Tournaments | [4]Rounds | [5]Matches | [6]Go Back | [7]Exit
        c = "\n---------- 🔥 MENU RAPPORTS 🔥 -------------"
        d = "\nEntrer le chiffre:"
        e = "\n[1] pour Acteurs     [2] pour Joueurs"
        f = "\n[3] pour Tournois    [4] pour Tours"
        g = "\n[5] pour Matches     [6] pour Menu Principal"
        h = "\n[7] pour Arrêter\n"
        menu = c+d+e+f+g+h
        print(menu)

    while True:
        """ Launching Program """
        reports_menu()
        user_choice = input("\nTaper votre choix: ")
        if user_choice == "1":
            print('choice 1: go to tournament_menu')
            # menu_tournament.exec_t_menu2()
        elif user_choice == "2":
            print('choice 2: go to players_menu')
            # menu_players.exec_p_menu2()
        elif user_choice == "3":
            print('choice 3: go to reports_menu')
            # menu_reports.exec_r_menu2()
        if user_choice == "4":
            print('choice 4: go to tournament_menu')
            # menu_tournament.exec_t_menu2()
        elif user_choice == "5":
            print('choice 5: go to players_menu')
            # menu_players.exec_p_menu2()
        elif user_choice == "6":
            print('choice 6: go to reports_menu')
            # menu_reports.exec_r_menu2()
        elif user_choice == "7":
            print("Merci d'avoir utilisé notre programme et à bientôt 😉")
            break
        else:
            print(f"😅 Vous avez taper '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 7.\n")
# exec_r_menu1()


## -- Tournament Menu --
def exec_t_menu1():
    """ function to launch reports menu within the current file"""

    def tournament_menu():
        """ Menu interface """
        # Tournament menu: [1]Create | [2]Open | [3]Go Back | [4]Exit
        c = "\n---------- 🔥 MENU TOURNOI 🔥 -------------"
        x = "\nEntrer le chiffre:"
        d = "\n[1] pour Créer            [2] pour Ouvrir"
        f = "\n[3] pour Menu Principal   [4] pour Arrêter\n"
        menu = c+x+d+f
        print(menu)

    while True:
        """ Launching Program """
        tournament_menu()
        user_choice = input("\nTaper votre choix: ")
        if user_choice == "1":
            print('choice 1: go to tournament_menu')
            # menu_tournament.exec_t_menu2()
        elif user_choice == "2":
            print('choice 2: go to players_menu')
            # menu_players.exec_p_menu2()
        elif user_choice == "3":
            print('choice 3: go to reports_menu')
            # menu_reports.exec_r_menu2()
        elif user_choice == "4":
            print("Merci d'avoir utilisé notre programme et à bientôt 😉")
            break
        else:
            print(f"😅 Vous avez taper '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 4.\n")
# exec_t_menu1()


############ START USER/PLAYERS MATCH/ROUNDS SCRIPT /!!!\ ###############


""" START USER/PLAYERS MATCH/ROUNDS SCRIPT /!!!\ """

if __name__=="__main__":
    """Launch program to add/update players, macthes, and rounds"""

    # -- Add & Save Players to DB file --
    # add_players()
    # save_players_data()
    
    # -- generate/View Round1 Matchups & Save them to db file --
    # view_unsorted_players_list()
    # view_sorted_players_list_by_rating()
    # view_ranked_players_by_rating_only()
    # view_ranked_players_by_score_and_rating()

    # -- The next functions MUST be initiated in order to save data in db file --
    # generate_players_matchup_with_reference_rating()
    # generate_players_matchup_reference_score_and_rating()
    # generate_matchups()
    # view_round1_matchups()
    # save_rounds_in_db()
    # view_rounds_in_db()
    # view_ranked_players_by_score_and_rating()

    # -- UPDATE SCORE --
    # -- creating a function to collect score from the user
    # -- Save Round1 data in tournaments_db -- 

    print("\n===================== 👀 ===================\n")

else:
    # view_unsorted_players_list()


    # -- 'generate_matchups' must be on so that rounds instance can be used in tournament.py:
    # generate_matchups()
    
    # view_round1_matchups()
    pass