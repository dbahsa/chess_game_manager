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
    pass

def add_players_db_indexes():
    """ function to add players indexes from data file"""
    pass

def add_end_date_time():
    """ function to add date & time at the end of the tournament """
    pass

@dataclass
class Tournament:
    """ This class helps create instances for the current tournament """
    name: str
    location: str
    start_date: str # automatic input
    time_control: str # choices: bullet, blitz, or coup rapide
    description: str
    number_of_rounds: int = field(default=4)
    rounds: list = field(init=False, repr=False, default_factory=add_rounds)
    players_db_indexes: list = field(init=False, repr=False, default_factory=add_players_db_indexes)
    end_date: str = field(init=False, repr=False, default_factory=add_end_date_time)



