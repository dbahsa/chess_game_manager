#! /user/bin/env python3
# -*- coding: utf-8 -*-

""" modules & packages """
import json
from dataclasses import dataclass, asdict, field
import pandas as pd
from tinydb import TinyDB
# from data import save_players_data2


""" players variables used to launch the script """
total_number_of_players = 8
registered_players = 0
# all_players_db:  exploited by data.py     
all_players_db = []
# db: var containing tournament data file
db = TinyDB('tournament_data.json')

""" # -- Prog Start here -- """
def player_score():
    """ return a list of player scores after each matchup """
    scores =[]
    return scores

def player_tournament_participation():
    """ to add tournaments in which a player participated in """
    tournaments =[]
    return tournaments

@dataclass
class Player:
    """Class to create player instances"""
    last_name: str
    first_name: str
    birth_date: str
    gender: str
    rating: int
    scores: list = field(init=False, repr=False, default_factory=player_score)
    tournaments: list = field(init=False, repr=False, default_factory=player_tournament_participation)
    single_player_db: dict = field(init=False, repr=False)

    def __post_init__(self):
        """ Method to help create player full data"""
        self.single_player_db = {"Nom de famille": self.last_name,
                                "Prénom": self.first_name,
                                "Date de naissance": self.birth_date,
                                "Sexe": self.gender,
                                "Classement": self.rating,
                                "Score": self.scores,
                                "Tournois": self.tournaments}


def add_players():
    """ function to instantiate players"""
    print("\n🚧 Enregistrement des 8 joueurs 🚧")
    # !!! DO NOT FORGET TO CHANGE THE RANGE BELOW TO REFLECT USER'S REQUIREMENTS OF 8 PLAYERS
    # replace 3 by total_number_of_players -> range(1, total_number_of_players+1)
    for i in range(1,3):
        print(f"\n🔥 Entrer les informations sur le joueur n°{i}")
        p = Player(input("- Nom de famille: "), 
                    input("- Prénom: "),
                    input("- Date de naissance telle que jj/mm/aaaa (ex: 18/02/1973): "),
                    input("- Sexe [H/F]: ").upper(),
                    int(input("- Classement: "))
                    )
        all_players_db.append(p.single_player_db)
        # print("-------------------------------------")
    print("\n🤓 Merci. Les 8 joueurs ont bien été enregistrés!")
    print("Passons à l'étape suivante dès à présent...\n")


def save_players_data():
    """ save players data """
    # db = TinyDB('tournament_data.json')
    # players table: 'players_db'
    players_table = db.table('players_db')
    players_table.truncate() # clear up the table first
    players_table.insert_multiple(all_players_db)


""" variables to help execute the script """
# 'filename' created to access & update data file:
filename = 'tournament_data.json'

with open(filename, "r") as f:
    temp = json.load(f)
# with open(filename, "w") as f:
#     json.dump(temp, f, indent=4)


def view_current_players_standings():
    """ This function allow to see sorted & unsorted players standings """
    print("\n  -- Tableau des joueurs --")
    print("-----------------------------")
    # unsorted players data
    df = pd.DataFrame.from_dict(temp["players_db"], orient='index')
    print(df)
    print("\n  - Tri des joueurs par points au 'Classement' général -")
    print("---------------------------------------------------------")
    # # sorting players data by rating
    x = df.sort_values(by=['Classement'], ascending=False)
    print(x)
    print("\n")







""" START UI """

if __name__=="__main__":

    # Add & Save Players to DB file
    # add_players()
    # save_players_data()
    # view_current_players_standings()

    # To start saving to DB file
    # save_initial_data()

    # print(all_players_db)

    # to get the names of tables in db:
    # for s in temp.keys():
    #     print(s[0:])

    # print(temp["players_db"].items())

    # to get indexes from t_players table separately:
    # for s in temp["players_db"].items():
    #     print(s[0])
    # or in temp list:
    # print(list(temp.items())[0][1].keys())

    # Get player's record:
    print("\n--- before udate -- ")
    print(temp["players_db"]["1"]['Nom de famille'])
    print(temp["players_db"]["2"]['Nom de famille'])
    
    # Open file to update them
    with open(filename, "r") as f:
        temp = json.load(f) 
        temp["players_db"]["1"]['Nom de famille'] = "Licorne"
        temp["players_db"]["2"]['Nom de famille'] = "Vinci"

    # save update
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)
    
    # print data updated 
    print("\n--- after update -- ")
    print(temp["players_db"]["1"]['Nom de famille'])
    print(temp["players_db"]["2"]['Nom de famille'])


    print("\n---")
    print(temp["players_db"].items())
    print("---\n")
    for s in temp["players_db"].items():
        # print(s[1].values())
        print(s)
        print(s[1].keys())
        print(list(s[1].keys()))
        print(s[1]['Nom de famille']) # to update scores, i must change "s[1]['Nom de famille']" from dict "temp["players_db"].items()"
    print("\n")
    # print(temp["players_db"].items()[1]['Nom de famille'])
    
    # -- wtih pandas: BEST TABLE VIEW --- #
    # print("\n")
    # # df = pd.DataFrame.from_dict(temp["players_db"], orient='index')
    # print(df)
    # print("\n")

    # print("\n  -- Tableau des joueurs --")
    # print("-----------------------------")
    # # unsorted players data
    # df = pd.DataFrame.from_dict(temp["players_db"], orient='index')
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

