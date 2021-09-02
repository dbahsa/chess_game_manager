#! /user/bin/env python3
# -*- coding: utf-8 -*-


import os


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

