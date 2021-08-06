import json
from tinydb import TinyDB, Query
# from players import players_db
from players import pl_ref


class Data:
    players: dict
    tournaments: dict


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

db = TinyDB('tournament_db.json')

# #-- T players
players_table = db.table('t_players')
players_table.truncate() # clear up the table first
players_table.insert_multiple(pl_ref)

# #-- T Tournament
tournaments_table = db.table('t_tournaments')
tournaments_table.truncate() 
tournaments_table.insert_multiple([
    {"name":"Swiss Tournament", "Date":"12/08/2021", "city":"Geneva", "Joueurs":players_table.all()},
    {"name":"Paris Tournament", "Date":"12/10/2021", "city":"Paris", "Joueurs":""}])

# To better view the db.json file
filename = 'chess_tournament_db.json'
with open(filename, "r") as f:
    temp = json.load(f)
print(temp['t_players']['1']["Last Name"])

with open(filename, "w") as f:
    json.dump(temp, f, indent=4)

""" to get ids from table
https://tinydb.readthedocs.io/en/stable/usage.html?highlight=doc_id#using-document-ids
"""

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
