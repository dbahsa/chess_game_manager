#! /user/bin/env python3
# -*- coding: utf-8 -*-


""" modules & packages """
import json
from dataclasses import dataclass, asdict, field
import pandas as pd
from tinydb import TinyDB


# tournaments = [tournament1, tournament2, tournament[w]] ; 'w' is the num of tournament
# tournament[w] = ['name', [round1, round2, round3, round4, round[z]]] ; 'z' is the num of rounds in a Tournament

# list of all tournaments
tournaments = []
# db: var containing tournament data file
db = TinyDB('tournament_data.json')

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
    tournaments.append(p.single_tournament_db)
    # print("-------------------------------------")
    print("\n🤓 Bravo! Le tournoi a bien été enregistré.\n")
    # print("Passons à l'étape suivante svp...\n")


def save_tournament_data():
    """ save tournament data """
    # db = TinyDB('tournament_data.json')
    # players table: 'players_db'
    tournaments_table = db.table('tournaments_db')
    tournaments_table.truncate()  # clear up the table first
    tournaments_table.insert_multiple(tournaments)


""" START TOURNAMENT SCRIPT """

if __name__=="__main__":

    add_tournament()
    save_tournament_data()

    x = tournaments[0].items()
    print("Printing items from dict x which come from tournaments list\n")
    for i in x:
        print(f"{i[0]}: {i[1]}")
    print("\n")
