#!/user/bin/env python3
# -*- coding: utf-8 -*-


from dataclasses import dataclass, asdict, field
import pandas as pd

from data import save_initial_data


""" players variables used """
total_number_of_players = 8
registered_players = 0
# all_players_db:  exploited by data.py     
all_players_db = []


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


# To start adding Player
add_players()

# To start saving to DB file
save_initial_data()


# print("Voici la liste des joueurs enregistés:")
# for p in all_players_db:
#     print(p)
# print("\n--\n")
# print(all_players_db)

