#! /user/bin/env python3
# -*- coding: utf-8 -*-


import os

from model import players

## -- Done! -- Func - Ranked Players by score and rating
def view_sorted_players_by_score_and_rating():
    """View sorted players by score and rating"""

    print('\n🙂 Classement des joueurs par score et par nombre de points au classement général:\n')
    k=0
    for u in players.sorted_players_by_score_and_rating:
        print(f"N°{k+1}: {u[1]['Prénom'][0] + ' ' + u [1]['Nom de famille']}\t{u[1]['Classement']}\t{u[1]['Score']}")
        k +=1
view_sorted_players_by_score_and_rating()


# |- program:
# |—— controller.py (cls: menu)
# |—— model.py (cls: challengers + tournt + db + menu)
# |—— view.py (view func)
# |—— db.json


""" I. LAUNCHING PROGRAM: First create data and mvc folders, and __init__.py file."""

## -- Create Data & MVC Folders -- 
def create_data_and_mvc_folders():
    """Function to create data nd mvc folder"""

    dir = os.path.join("./data/")
    if not os.path.exists(dir):
        os.mkdir(dir)

    dir = os.path.join("./model/")
    if not os.path.exists(dir):
        os.mkdir(dir)

    dir = os.path.join("./view/")
    if not os.path.exists(dir):
        os.mkdir(dir)

    dir = os.path.join("./controller/")
    if not os.path.exists(dir):
        os.mkdir(dir)


## -- Add __init__.py in Data and MVC folders -- 
def add__init__file():
    """Function to add __init__.py in Data and MVC folders"""
    
    filename = "__init__.py"

    f = open("./data/"+filename, "w")
    f.close()

    g = open("./model/"+filename, "w")
    g.close()

    h = open("./view/"+filename, "w")
    h.close()

    i = open("./controller/"+filename, "w")
    i.close()


"""II.  Call Main Menu"""

