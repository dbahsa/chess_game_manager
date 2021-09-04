#! /user/bin/env python3
# -*- coding: utf-8 -*-


""" modules & packages """
import json
from dataclasses import dataclass, field
from tinydb import TinyDB
import pandas as pd
import datetime

# import model
import view
# import controller as co


""" START USER/PLAYERS MATCH/ROUNDS SCRIPT /!!!\ """

if __name__=="__main__":
    """Launch program to add/update players, macthes, and rounds"""

    
    
    ## -- Tournament Menu --
    def exec_t_menu1():
        """ function to launch reports menu within the current file"""

        view.tournament_menu()
        while True:
            """ Launching Tournament Menu"""
            
            view.tournament_menu()
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                add_tournament()
                break
            elif user_choice == "2":
                add_players()
                update_tournament_players_info()
                break
            elif user_choice == "3":
                update_tournament_menu()
                break
            elif user_choice == "4":
                update_players_menu()
                break
            elif user_choice == "5":
                exec_p_menu1()
                break
            elif user_choice == "6":
                exec_main_menu1()
                break
            elif user_choice == "7":
                view.byebye()
                break
            else:
                view.error_msg()


    
    ## -- Main Menu --
    def exec_main_menu1():
        """ function to launch main menu within the current file"""

        view.welcome_msg()
        while True:
            """ Launching Main Menu Interface """
            
            view.main_menu()
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                exec_t_menu1()
                break
            elif user_choice == "2":
                exec_p_menu1()
                break
            elif user_choice == "3":
                exec_r_menu1()
                break
            elif user_choice == "4":
                view.byebye()
                break
            else:
                view.error_msg()
    exec_main_menu1()

else:
    pass
