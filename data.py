#! /user/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import json
from tinydb import TinyDB, Query

# from players import players_db
from players import all_players_db

# db: var containing tournament data file
db = TinyDB('tournament_data.json')


""" Saving Data """

def save_players_data():
    """ save players data """

    # db = TinyDB('tournament_data.json')
    #-- in players table (t_players')
    players_table = db.table('t_players')
    players_table.truncate() # clear up the table first
    players_table.insert_multiple(all_players_db)
    #-- in tournament table ('t_tournaments')
    tournaments_table = db.table('t_tournaments')
    tournaments_table.truncate() 
    tournaments_table.insert_multiple([
        {"name":"Swiss Tournament", "Date":"12/08/2021", "city":"Geneva", "Joueurs":players_table.all()},
        {"name":"Paris Tournament", "Date":"12/10/2021", "city":"Paris", "Joueurs":""}])

def save_tournament_data():
    """ save tournament data """

    # db = TinyDB('tournament_data.json')
    #-- in players table (t_players')
    players_table = db.table('t_players')
    players_table.truncate() # clear up the table first
    players_table.insert_multiple(all_players_db)
    #-- in tournament table ('t_tournaments')
    tournaments_table = db.table('t_tournaments')
    tournaments_table.truncate() 
    tournaments_table.insert_multiple([
        {"name":"Swiss Tournament", "Date":"12/08/2021", "city":"Geneva", "Joueurs":players_table.all()},
        {"name":"Paris Tournament", "Date":"12/10/2021", "city":"Paris", "Joueurs":""}])

def save_matches_data():
    """ save macthes data """

    # db = TinyDB('tournament_data.json')
    #-- in players table (t_players')
    players_table = db.table('t_players')
    players_table.truncate() # clear up the table first
    players_table.insert_multiple(all_players_db)
    #-- in tournament table ('t_tournaments')
    tournaments_table = db.table('t_tournaments')
    tournaments_table.truncate() 
    tournaments_table.insert_multiple([
        {"name":"Swiss Tournament", "Date":"12/08/2021", "city":"Geneva", "Joueurs":players_table.all()},
        {"name":"Paris Tournament", "Date":"12/10/2021", "city":"Paris", "Joueurs":""}])


def save_rounds_data():
    """ save rounds data """

    # db = TinyDB('tournament_data.json')
    #-- in players table (t_players')
    players_table = db.table('t_players')
    players_table.truncate() # clear up the table first
    players_table.insert_multiple(all_players_db)
    #-- in tournament table ('t_tournaments')
    tournaments_table = db.table('t_tournaments')
    tournaments_table.truncate() 
    tournaments_table.insert_multiple([
        {"name":"Swiss Tournament", "Date":"12/08/2021", "city":"Geneva", "Joueurs":players_table.all()},
        {"name":"Paris Tournament", "Date":"12/10/2021", "city":"Paris", "Joueurs":""}])


""" Updating Data """

def update_players_data():
    """ save players data """

    # db = TinyDB('tournament_data.json')
    #-- in players table (t_players')
    players_table = db.table('t_players')
    players_table.truncate() # clear up the table first
    players_table.insert_multiple(all_players_db)
    #-- in tournament table ('t_tournaments')
    tournaments_table = db.table('t_tournaments')
    tournaments_table.truncate() 
    tournaments_table.insert_multiple([
        {"name":"Swiss Tournament", "Date":"12/08/2021", "city":"Geneva", "Joueurs":players_table.all()},
        {"name":"Paris Tournament", "Date":"12/10/2021", "city":"Paris", "Joueurs":""}])

def update_tournament_data():
    """ save tournament data """

    # db = TinyDB('tournament_data.json')
    #-- in players table (t_players')
    players_table = db.table('t_players')
    players_table.truncate() # clear up the table first
    players_table.insert_multiple(all_players_db)
    #-- in tournament table ('t_tournaments')
    tournaments_table = db.table('t_tournaments')
    tournaments_table.truncate() 
    tournaments_table.insert_multiple([
        {"name":"Swiss Tournament", "Date":"12/08/2021", "city":"Geneva", "Joueurs":players_table.all()},
        {"name":"Paris Tournament", "Date":"12/10/2021", "city":"Paris", "Joueurs":""}])

def update_matches_data():
    """ save macthes data """

    # db = TinyDB('tournament_data.json')
    #-- in players table (t_players')
    players_table = db.table('t_players')
    players_table.truncate() # clear up the table first
    players_table.insert_multiple(all_players_db)
    #-- in tournament table ('t_tournaments')
    tournaments_table = db.table('t_tournaments')
    tournaments_table.truncate() 
    tournaments_table.insert_multiple([
        {"name":"Swiss Tournament", "Date":"12/08/2021", "city":"Geneva", "Joueurs":players_table.all()},
        {"name":"Paris Tournament", "Date":"12/10/2021", "city":"Paris", "Joueurs":""}])


def update_rounds_data():
    """ save rounds data """

    # db = TinyDB('tournament_data.json')
    #-- in players table (t_players')
    players_table = db.table('t_players')
    players_table.truncate() # clear up the table first
    players_table.insert_multiple(all_players_db)
    #-- in tournament table ('t_tournaments')
    tournaments_table = db.table('t_tournaments')
    tournaments_table.truncate() 
    tournaments_table.insert_multiple([
        {"name":"Swiss Tournament", "Date":"12/08/2021", "city":"Geneva", "Joueurs":players_table.all()},
        {"name":"Paris Tournament", "Date":"12/10/2021", "city":"Paris", "Joueurs":""}])



""" Retrieving Data for Processing Purposes """

""" Viewing Reports """

def view_current_data():
    """ to view current data - use db file """
    df = pd.DataFrame(all_players_db)
    print(df)

def sort_data_by_rating():
    """ to sort current data by rating - use db file """
    pass

def sorted_players_by_score():
    """ to view sorted players by score only - use db file """
    pass

def sorted_players_by_score_and_ranking():
    """ to view sorted players by score and ranking - use db file """
    pass
    # # sorting data
    # print("\n-- Voici les informations que vous venez de saisir sur les joueurs: --\n")
    # # # x=df.sort_values(by=['ranking'], ascending=False)
    # print(df)


""" 1) Serialization of players data """
# serialized_players = []

# for x in players_db:
#     # # Serialization of player object:
#     serialized_player = {
#         "Last Name": x.pl_lname,
#         "First Name": x.pl_fname,
#         "Birth Date": x.birth_date,
#         "Gender": x.gender,
#         "Rating": x.pl_rating,
#         "Score": x.pl_score,
#         "Tournaments": x.tournaments
#         }
#     serialized_players.append(serialized_player)

# # # Deserialization of player object:
# pl_lname = serialized_player['Last Name']
# pl_fname = serialized_player['First Name']
# birth_date = serialized_player['Birth Date']
# gender = serialized_player['Gender']
# pl_rating = serialized_player['Rating']
# score = serialized_player['Score']
# tournaments = serialized_player['Tournaments']

# player = {
#   pl_lname: serialized_player['Last Name'],
#   pl_fname: serialized_player['First Name'],
#   birth_date: serialized_player['Birth Date'],
#   gender: serialized_player['Gender'],
#   pl_rating: serialized_player['Rating'],
#   score: serialized_player['Score'],
#   tournaments: serialized_player['Tournaments']
# }

# View serialized players db
# print("-- Serialized DB --")
# for i in serialized_players:
#     print(i)

""" 2) Save tournament data in json file """


#=== SAVING DATA TO FILE
# db = TinyDB('chess_tournament_db.json')

# #-- T players
# players_table = db.table('t_players')
# players_table.truncate() # clear up the table first
# players_table.insert_multiple(xx)

# #-- T Tournament
# tournaments_table = db.table('t_tournaments')
# tournaments_table.truncate() 
# tournaments_table.insert_multiple([
#     {"name":"Swiss Tournament", "Date":"12/08/2021", "city":"Geneva", "Joueurs":players_table.all()},
#     {"name":"Paris Tournament", "Date":"12/10/2021", "city":"Paris", "Joueurs":""}])

#=== Viewing DB from file

# To better view the db.json file
filename = 'chess_tournament_db.json'
with open(filename, "r") as f:
    temp = json.load(f)
print(temp['t_players']['1']["Last Name"])
print(temp)

# with open(filename, "w") as f:
    # json.dump(temp, f, indent=4)

""" to get ids from table
https://tinydb.readthedocs.io/en/stable/usage.html?highlight=doc_id#using-document-ids
"""

# === Print info from DB file

# print("\n-- DB Tableau des joueurs --\n")
# print(players_table.all())
# #print("\n-- DB Tableau des tournois --\n")
#print(tournaments_table.all())
#print("\n-- Liste des tableaux dans le fichier json --\n")
#print(db.tables())

# deserializing db
# serialized_players = players_table.all()
# # print(serialized_players[0])
# print(serialized_players[0]['Last Name'])


""" 3) Update players data on-demand """
