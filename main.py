#! /user/bin/env python3
# -*- coding: utf-8 -*-


""" modules & packages """
import json
from dataclasses import dataclass, field
from tinydb import TinyDB
import pandas as pd
import datetime

from model import tournament, players
# import model
import view
# import controller as co


""" START USER/PLAYERS MATCH/ROUNDS SCRIPT /!!!\ """

if __name__=="__main__":
    """Launch program to add/update players, macthes, and rounds"""

    view.welcome_msg()




    """Update Menus"""

    ## -- Update Players Menu --
    def update_players_menu():
        """ function to launch players menu within the current file"""

        def update_players_menu():
            """ Menu interface """
            
            a = "\n------------------ 🔥 ACTUALISATION DES JOUEURS 🔥 --------------------"
            b = "\nTaper [1] pour le nom\t[2] pour le prénom\t[3] pour le sexe"
            c = "\n      [4] pour modifier la date de naissance"
            d = "\n      [5] pour modifier le nombre de point au classement général"
            e = "\n      [6] pour ajouter ou modifier un score"
            f = "\n      [7] pour effacer tous les scores 🚨"
            g = "\n      [8] pour le 'MENU JOUEUR'\t[9] pour le 'MENU PRINCIPAL'\n"
            menu = a+b+c+d+e+f+g
            print(menu)

        while True:
            """ Launching Program """
            
            update_players_menu()
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                update_player_lname()
                break
            elif user_choice == "2":
                update_player_fname()
                break
            elif user_choice == "3":
                update_player_gender()
                break
            elif user_choice == "4":
                update_player_birth_date()
                break
            elif user_choice == "5":
                update_player_rating()
                break
            elif user_choice == "6":
                update_player_score()
                break
            elif user_choice == "7":
                erase_all_scores()
                break
            elif user_choice == "8":
                exec_p_menu1()
                break
            elif user_choice == "9":
                exec_main_menu1()
                break
            else:
                print(f"😅 Vous avez saisi '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 9.\n")
    # update_players_menu()


    ## -- Update Tournament Menu --
    def update_tournament_menu_out():
        """ function to launch reports menu within the current file"""

        while True:
            """ Launching Program """
            
            view.update_tournament_menu_in()
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                tournament.update_tournament_name()
                
            elif user_choice == "2":
                tournament.update_tournament_location()
               
            elif user_choice == "3":
                tournament.update_tournament_date()
                
            elif user_choice == "4":
                print("🚨 Merci de nous joindre pour modifier le nombre de tours, qui par défaut est égal à 4")
            elif user_choice == "5":
                tournament.update_tournament_time_control()
                
            elif user_choice == "6":
                tournament.update_tournament_description()
                
            elif user_choice == "7":
                exec_p_menu1()
            
            elif user_choice == "8":
                exec_main_menu1()
            
            else:
                print(f"😅 Vous avez tapé '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 8.\n")
    # update_tournament_menu_out()


    """ Starting Menus """

    ## -- Reports Menu --
    def exec_r_menu1():
        """ function to launch reports menu within the current file"""

        def reports_menu():
            """ Menu interface """
            
            c = "\n---------- 🔥 MENU RAPPORTS 🔥 -------------"
            d = "\nEntrer le chiffre:"
            e = "\n[1] pour Acteurs     [2] pour Joueurs"
            f = "\n[3] pour Tournois    [4] pour Tours"
            g = "\n[5] pour Matches     [6] pour Menu Principal"
            h = "\n[7] pour Arrêter\n"
            menu = c+d+e+f+g+h
            print(menu)

        while True:
            """ Launching Program """
            reports_menu()
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                print('choice 1: go to tournament_menu')
                # menu_tournament.exec_t_menu2()
            elif user_choice == "2":
                print('choice 2: go to players_menu')
                # menu_players.exec_p_menu2()
            elif user_choice == "3":
                print('choice 3: go to reports_menu')
                # menu_reports.exec_r_menu2()
            if user_choice == "4":
                print('choice 4: go to tournament_menu')
                # menu_tournament.exec_t_menu2()
            elif user_choice == "5":
                print('choice 5: go to players_menu')
                # menu_players.exec_p_menu2()
            elif user_choice == "6":
                exec_main_menu1()
                break
            elif user_choice == "7":
                print("Merci d'avoir utilisé notre programme et à bientôt 😉")
                break
            else:
                print(f"😅 Vous avez entré '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 7.\n")
    # exec_r_menu1()


    ## -- Players Menu --
    def exec_p_menu1():
        """ function to launch players menu within the current file"""

        def players_menu():
            """ Menu interface """
            # Players menu: [1]Create | [2]Open | [3]Go Back | [4]Exit
            c = "\n------------ 🔥 MENU JOUEURS 🔥 ---------------"
            x = "\nTaper le chiffre:"
            d = "\n[1] pour Créer            [2] pour Actualiser"
            f = "\n[3] pour Menu Principal   [4] pour Arrêter\n"
            menu = c+x+d+f
            print(menu)

        while True:
            """ Launching Program """
            players_menu()
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                print('Créer un joueur')
                # menu_tournament.exec_t_menu2()
            elif user_choice == "2":
                print("Accéder à l'actualisation des joueurs......")
                # menu_players.exec_p_menu2()
            elif user_choice == "3":
                exec_main_menu1()
                break
            elif user_choice == "4":
                print("Merci d'avoir utilisé notre programme et à bientôt 😉")
                break
            else:
                print(f"😅 Vous avez tapé '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 4.\n")
    # exec_p_menu1()


    
    ## -- Tournament Menu --
    def exec_t_menu1():
        """ function to launch reports menu within the current file"""

        while True:
            """ Launching Tournament Menu"""
            
            view.tournament_menu()
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                tournament.add_tournament()
                tournament.save_tournament_data()
                tournament.update_tournament_players_info()
            elif user_choice == "2":
                players.add_players()
                players.save_players_data()
            elif user_choice == "3":
                update_tournament_menu_out()
            elif user_choice == "4":
                players.update_players_menu()
            elif user_choice == "5":
                exec_p_menu1()
            elif user_choice == "6":
                exec_main_menu1()
            elif user_choice == "7":
                view.byebye()
                break
            else:
                view.error_msg()
    # exec_t_menu1()


    ## -- Main Menu -- /!!!\ Must stay active to allow other menu to function properly!!!
    def exec_main_menu1():
        """ function to launch main menu within the current file"""

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
