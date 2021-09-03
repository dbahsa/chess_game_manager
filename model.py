#! /user/bin/env python3
# -*- coding: utf-8 -*-


from dataclasses import dataclass, field

""" Tournament constructors """

def add_rounds():
    """ Function to add round instances """
    
    rounds = {}
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


""" Players constructors """

def player_score():
    """ return a list of player scores """
    
    scores =[]
    return scores


def player_tournament_participation():
    """ Function that adds tournaments in which a player participated in """
    
    tournaments =[]
    return tournaments

## -- Players cls --
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
