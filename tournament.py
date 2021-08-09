#!/user/bin/env python3
# -*- coding: utf-8 -*-


import datetime
from dataclasses import dataclass, field


# tournaments = [tournament1, tournament2, tournament[w]] ; 'w' is the num of tournament
# tournament[w] = ['name', [round1, round2, round3, round4, round[z]]] ; 'z' is the num of rounds in a Tournament

# list of all tournaments
tournaments = []

def add_rounds():
    """ function to add round instances """
    rounds = []
    return rounds

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
    number_of_rounds: int = field(default=4)
    rounds: list = field(init=False, repr=False, default_factory=add_rounds)
    players_db_indexes: list = field(init=False, repr=False, default_factory=add_players_db_indexes)
    single_tournament_db: dict = field(init=False, repr=False)
    
    def __post_init__(self):
        """ Method to help create a single tournament full data"""
        self.single_tournament_db = {"Nom du tournoi": self.name,
                                    "Lieu": self.location,
                                    "Date": self.date,
                                    "Nombre de tour": self.number_of_rounds,
                                    "Tournées": self.rounds,
                                    "Joueurs": self.players_db_indexes,
                                    "Contrôle du temps": self.time_control,
                                    "Description": self.description}
        tournaments.append(self.single_tournament_db)

def add_tournament():
    """ Function to instantiate tournament"""
    print(f"\n🚀 Veuillez entrer les informations suivantes sur le tournoi")
    p = Tournament(input("- Nom: "), 
                    input("- Lieu: "),
                    input("- Date, telle que jj/mm/aaaa (ex: 18/02/2022): "),
                    input("- Quel est votre Contrôle du temps: 'Bullit', 'Blitz'ou 'Coup Rapide'? "),
                    input("- Description: ")
                    )
    # print("-------------------------------------")
    print("\n🤓 Bravo! Le tournoi a bien été enregistré.\n")
    # print("Passons à l'étape suivante svp...\n")

add_tournament()

x = tournaments[0].items()
print("Printing items from dict x which come from tournaments list\n")
for i in x:
    print(f"{i[0]}: {i[1]}")
print("\n")

# |- 🌼 Next Steps 🌼:
# |—— save tournaments info to db files
# |—— instantiate players obj
# |—— save players info to db
# |—— get "sorted" players info (name+rating+score) from db to instantiate 1st matchups
# |—— save 1st matchups to db
# |—— get matchups from db to instantiate round1
# |—— save round1
# |—— get round1 to add score
# |—— save round1 score
# |—— get "sorted" players info based num of scores & rating
# |—— instantiate round2
# |—— save round2
# |—— get round2 to input round2 scores
# |—— save round2 scores
# |—— get 'sorted' players info based num of scores & rating
# |—— instantiate round3
# |—— save round3
# |—— get round3 to input round3 scores
# |—— save round3
# |—— etc
# |—— 
# |—— 
# 🚨 In each step, always show the user its own input, and ask to pursue or to reset