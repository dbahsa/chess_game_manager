#! /user/bin/env python3
# -*- coding: utf-8 -*-


""" modules & packages """
import json
from dataclasses import dataclass, field
from tinydb import TinyDB


""" tournament variables used to launch the script """
tournaments = []
db = TinyDB('db1.json')

filename = "db1.json"
with open(filename, "r") as f:
    json_object = json.load(f)

""" # -- Prog Start Here -- """

# -- Done! -- 
def add_rounds():
    """ Function to add round instances """
    
    rounds = {}
    return rounds


# -- Done!
def add_players_db_indexes():
    """ function to add players indexes from data file"""
    players_db_indexes = []
    return players_db_indexes


@dataclass
class Tournament:
    """ This class helps create instances for the current tournament """
    
    name: str
    location: str
    date: str
    time_control: str
    description: str
    number_of_turns: int = field(default=4)
    rounds: dict = field(init=False, repr=False, default_factory=add_rounds)
    players_db_indexes: list = field(init=False, repr=False, default_factory=add_players_db_indexes)
    single_tournament_db: dict = field(init=False, repr=False)
    
    def __post_init__(self):
        """ Method to help create a single tournament full data"""
        self.single_tournament_db = {"Nom du tournoi": self.name,
                                    "Lieu": self.location,
                                    "Date": self.date,
                                    "Nombre de tours": self.number_of_turns,
                                    "Tournées": self.rounds,
                                    "Joueurs": self.players_db_indexes,
                                    "Contrôle du temps": self.time_control,
                                    "Description": self.description}
        tournaments.append(self.single_tournament_db)


# -- Done! -- Add Tournament -- /!!!\ ADD AN END DATE WHICH IS ADDED AUTOMATICALLY AT THE END OF THE TOURNAMENT !!!
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
# add_tournament()

# -- Done! -- Save First Tournament Info --
def save_tournament_data():
    """ save tournament data """
    db = TinyDB('db1.json')
    tournaments_table = db.table('tournaments_db')
    tournaments_table.truncate()  # clear up the table first
    tournaments_table.insert_multiple(tournaments)

# -- Done! -- View Tournament Info  --
def view_tournament_info():
    """ Function to view tournament info """
    
    print("\n-- Voici les informations actuelles du tournoi --\n")
    ## -- Not Numbered List
    # for i in json_object['tournaments_db']['1']:
    #     print(f"{i}: {json_object['tournaments_db']['1'][i]}")
    ## -- Numbered List
    h = 1
    for i in json_object['tournaments_db']['1']:
        print(f"{[h]} {i}: {json_object['tournaments_db']['1'][i]}")
        h += 1


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


# -- Done! -- Update Tournament Rounds in db file -- Automatic Process... Check it when rounds are created
def update_tournament_rounds():
    """ Function to update Tournament Rounds in db file """

    print(f"\nLes tournées sont: {json_object['tournaments_db']['1']['Tournées']}\n")
    ## -- Append rounds from players_db table
    json_object['tournaments_db']['1']['Tournées'].update(json_object['players_db']['1']['Tournées'])
    with open(filename, "w") as f:
        json.dump(json_object, f, indent=4)
    print(f"\nNouvelles Tournées: {json_object['tournaments_db']['1']['Tournées']}")
    ## -- Send the user back to the main menu


# -- Done! -- Update Tournament Players Indexes in db file -- Automatic Process... Check it when player instances are created
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


""" START TOURNAMENT CREATION SCRIPT """

if __name__=="__main__":

    ## -- RESPECT THESE STEPS -- ##

    ## -- Instanttiating tournament ojbects & saving them to db file --
    # add_tournament()
    ## -- TinyDB used to handle this task.
    # save_tournament_data()
    ## -- json module used to handle 'update' tasks because I couldn't find an alternative to the deprecated 'write_back' function.
    # view_tournament_info()
    
    ## -- Update Tournament Data in DB file -- To be Updated once players.py is done /!!!\
    # update_tournament_info()

    print("\n===================== 👀 ===================\n")
