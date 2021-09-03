#! /user/bin/env python3
# -*- coding: utf-8 -*-


import controller


########################### TOURNAMENT VIEWS ########################

"""View Tournament Info"""

## -- View Tournament Info  --
def view_tournament_info():
    """ Function to view tournament info """
    
    print("\n-- Voici les informations actuelles du tournoi --\n")
    h = 1
    for i in controller.json_object['tournaments_db']['1']:
        print(f"{[h]} {i}: {controller.json_object['tournaments_db']['1'][i]}")
        h += 1
# view_tournament_info()


############################# PLAYERS VIEWS #########################

""" View players data from db file /!!!\ """

## -- To view players info  --
def view_players_info():
    """ Function to view tournament info """
    
    print("\n📚 Voici les informations actuelles sur les joueurs\n")
    print(controller.real_db)
# view_players_info()


""" View Ranked Players by Ratings & Scores """

## -- Func - Ranked Players by score and rating
def view_sorted_players_by_score_and_rating():
    """View sorted players by score and rating"""

    print('\n🙂 Classement des joueurs par score et par nombre de points au classement général:\n')
    k=0
    for u in controller.sorted_players_by_score_and_rating:
        print(f"N°{k+1}: {u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']}\t{u[1]['Classement']}\t{u[1]['Score']}")
        k +=1
# view_sorted_players_by_score_and_rating()


## -- Func - Ranked Players by rating, Used ONLY for Round1
def view_sorted_players_by_rating():
    print('\n🙂 Classement des joueurs par nombre de points au classement général:\n')
    k=0
    for u in controller.sorted_players_by_rating:
        print(f"N°{k+1}: {u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']}\t{u[1]['Classement']}")
        k +=1
# view_sorted_players_by_rating()


## -- VIEW ROUND1 MATCHUPS FROM DB -- 
def view_round1_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round1:\n")
    e = 1
    d = list(controller.json_object['tournaments_db']['1']['Tournées']["Round1"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1
# view_round1_matchups()


### -- VIEW ROUND2 MATCHUPS FROM DB -- 
def view_round2_matchups():
    """Function to view Round2 Matchups"""
    
    print("\n💡 Voici les Matches du Round2:\n")
    e = 1
    d = list(controller.json_object['tournaments_db']['1']['Tournées']["Round2"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1
# view_round2_matchups()


## -- VIEW ROUND3 MATCHUPS FROM DB --
def view_round3_matchups():
    """Function to view Round3 Matchups"""
    
    print("\n💡 Voici les Matches du Round3:\n")
    e = 1
    d = list(controller.json_object['tournaments_db']['1']['Tournées']["Round3"]['Matches'].values())
    for k in d:
        print(f"Match{e}: {k[0][1]} ({k[0][0][-1]}) vs. {k[1][1]} ({k[1][0][-1]})")
        e +=1
# view_round3_matchups()


### -- VIEW ROUND4 MATCHUPS FROM DB --
def view_round4_matchups():
    """Function to view Round1 Matchups"""
    
    print("\n💡 Voici les Matches du Round4:\n")
    e = 1
    for x in list(controller.json_object['tournaments_db']['1']['Tournées']["Round4"]['Matches'].values()):
        b = list(x.values())
        print(f"Match n°{e}: {b[0][0]} vs. {b[0][1]}")
        e +=1
# view_round4_matchups()
