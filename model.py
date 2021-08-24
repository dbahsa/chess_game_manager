#! /user/bin/env python3
# -*- coding: utf-8 -*-


# |- program:
# |—— controller.py (cls: menu)
# |—— model.py (cls: pl + tournt + db + menu)
# |—— view.py (view func)
# |—— db.json


""" modules & packages """
import json
from dataclasses import dataclass, asdict, field

""" players variables used to launch the script """
tournaments = []
# db = TinyDB('tournament_data.json')

""" # -- Prog Start here -- """

# -- To do! In progress
def add_rounds():
    """ Function to add round instances """
    rounds = []
    # print("================== 🤓 Round1 🏁 Matchups 🥸 ================")
    # for i in rounds[0]:
    #     print(i)
    return rounds

# -- To do!
## -- pl_db_indexes = [x for x in temp["players_db"].keys()]
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
    time_control: str # choices: bullet, blitz, or coup rapide
    description: str
    number_of_turns: int = field(default=4)
    # rounds = item from players.py
    rounds: dict = field(init=False, repr=False, default_factory=add_rounds) # MUST BE A DICT WITH EACH ROUND AS A KEY
    # players_db_indexes = item from players.py
    players_db_indexes: list = field(init=False, repr=False, default_factory=add_players_db_indexes)
    single_tournament_db: dict = field(init=False, repr=False)
    
    def __post_init__(self):
        """ Method to help create a single tournament full data"""
        self.single_tournament_db = {"Nom du tournoi": self.name,
                                    "Lieu": self.location,
                                    "Date": self.date,
                                    "Nombre de tour": self.number_of_turns,
                                    "Tournées": self.rounds,
                                    "Joueurs": self.players_db_indexes,
                                    "Contrôle du temps": self.time_control,
                                    "Description": self.description}
        tournaments.append(self.single_tournament_db)

# -- Done!
def add_tournament():
    """ Function to instantiate tournament"""
    print(f"\n🚀 Veuillez entrer les informations suivantes sur le tournoi: ")
    p = Tournament(input("- Nom: "), 
                    input("- Lieu: "),
                    input("- Date, telle que jj/mm/aaaa (ex: 18/02/2022): "),
                    input("- Quel est votre Contrôle du temps: 'Bullit', 'Blitz'ou 'Coup Rapide'? "),
                    input("- Description: ")
                    )
    # print("-------------------------------------")
    print("\n🤓 Bravo! Le tournoi a bien été enregistré.\n")
    # print("Passons à l'étape suivante svp...\n")


### -- To Do! saving with json
def save_data(self):
    """ Method to help create a single tournament full data"""
    temp = {'players_table':{}, 'tournament_table':{}}
    temp['tournament_table']["Nom du tournoi"] = self.name
    temp['tournament_table']["Lieu"] = self.location
    temp['tournament_table']["Date"] = self.date
    temp['tournament_table']["Nombre de tour"] = self.number_of_turns
    temp['tournament_table']["Tournées"] = self.rounds
    temp['tournament_table']["Joueurs"] = self.players_db_indexes
    temp['tournament_table']["Contrôle du temps"] = self.time_control
    temp['tournament_table']["Description"] = self.description
    print(temp)
    with open('xxx.json', "w") as f:
        temp = json.load(f)


### -- To do! In progress...
def save_tournament_data():
    """ save tournament data """
    # db = TinyDB('tournament_data.json')
    # players table: 'players_db'
    tournaments_table = db.table('tournaments_db')
    tournaments_table.truncate()  # clear up the table first
    tournaments_table.insert_multiple(tournaments)














### ---------- DO NOT WORK ---
# -- To do! In progress
# def add_rounds():
#     """ Function to add round instances """
#     rounds = {}
#     # print("================== 🤓 Round1 🏁 Matchups 🥸 ================")
#     # for i in rounds[0]:
#     #     print(i)
#     return rounds

# # -- To do!
# ## -- pl_db_indexes = [x for x in temp["players_db"].keys()]
# def add_players_db_indexes():
#     """ function to add players indexes from data file"""
#     players_db_indexes = {}
#     return players_db_indexes


# @dataclass
# class Tournament:
#     """ Tournament class allows create instances for the current tournament """

#     name: str
#     location: str
#     date: str
#     time_control: str
#     description: str
#     number_of_turns: int = field(default=4)
#     rounds: dict = field(init=False, repr=False, default_factory=add_rounds)
#     players_db_indexes: list = field(init=False, repr=False, default_factory=add_players_db_indexes)

#     # def __init__(self, name, location, date, time_control, description,
#         #         players_db_indexes=None, number_of_turns=4, rounds=[]):
#         # self.name = name
#         # self.location = location
#         # self.date = date
#         # self.time_control = time_control
#         # self.description = description
#         # self.players_db_indexes = players_db_indexes
#         # self.number_of_turns = number_of_turns
#         # self.rounds = rounds
    



# def add_tournament():
#     """ 'add_tournament' helps to instantiate tournament objects """
    
#     print(f"\n🚀 Veuillez entrer les informations suivantes sur ce tournoi: ")
#     p = Tournament(input("- Nom: "), 
#                     input("- Lieu: "),
#                     input("- Date [jj/mm/aaaa], ex: 18/02/2022: "),
#                     input("- Le Contrôle du temps 'Bullit', 'Blitz'ou 'Coup Rapide'? "),
#                     input("- Description: ")
#                     )
#     # print("-------------------------------------")
#     # print("\nBravo! Le tournoi a bien été enregistré.\n")

# add_tournament()
# class_instance = Tournament()
# class_instance.save_data()

# print("\nBravo! Le tournoi a bien été enregistré.\n")


# """ trial func """
# # def __init__(self, my_stars_home, mode):
#     # self._db = TinyDB(os.path.join(my_stars_home, "mystars.db"))
#     # self._idx = {
#     #     'language': {},
#     #     'keyword': {}
#     # }
#     # self.mode = mode


# class Player:
#     """ Player class allows to create player instances"""
    
#     def __init__(self,
#                 lname,
#                 fname,
#                 birth_date,
#                 gender,
#                 rating,
#                 tournaments,
#                 scores=[],
#                 single_tournament_db={}):
#         self.lname: lname
#         self.fname: fname
#         self.birth_date: birth_date
#         self.gender: gender
#         self.rating: rating
#         self.scores: scores
#         self.tournaments: tournaments
#         self.single_tournament_db: single_tournament_db

#     def __post_init__(self):
#         """ Function used to create and save players instances in db file"""
        
#         temp = {}
#         self.single_player_db = {"Nom de famille": self.last_name,
#                                 "Prénom": self.first_name,
#                                 "Date de naissance": self.birth_date,
#                                 "Sexe": self.gender,
#                                 "Classement": self.rating,
#                                 "Score": self.scores,
#                                 "Tournois": self.tournaments}
        
#         temp['players_table'] = self.single_player_db

#         with open('xxx.json', "w") as f:
#             temp = json.load(f)

# ## To do:
# # - Add players indexes to tournament_table
# # - Add players scores to tournament_table