#! /user/bin/env python3
# -*- coding: utf-8 -*-


""" modules & packages """
import json
from dataclasses import dataclass, field
from tinydb import TinyDB
import pandas as pd
import datetime

from model import tournament, players
import view


""" START USER/PLAYERS MATCH/ROUNDS SCRIPT /!!!\ """

if __name__=="__main__":
    """Launch program to add/update players, macthes, and rounds"""

    view.welcome_msg()

    """Update Menus"""

    ## -- Update Players Menu --
    def update_players_menu():
        """ function to launch players menu within the current file"""

        while True:
            """ Launching Program """
            
            view.players_info()
            view.update_players_menu()
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                players.update_player_lname()
            elif user_choice == "2":
                players.update_player_fname()
            elif user_choice == "3":
                players.update_player_gender()
            elif user_choice == "4":
                players.update_player_birth_date()
            elif user_choice == "5":
                players.update_player_rating()
            elif user_choice == "6":
                players.update_player_score()
            elif user_choice == "7":
                players.erase_all_scores()
            elif user_choice == "8":
                break
            else:
                view.error_msg()


    ## -- Update Tournament Menu --
    def update_tournament_menu_out():
        """ function to launch reports menu within the current file"""

        while True:
            """ Launching Program """
            
            ## w/o menu sys
             
            print("\nVoici les informations actuelles sur le tournoi.")
            print("Taper le chiffre de votre choix pour effectuer une modification:\n")
            h = 1
            for i in tournament.json_object['tournaments_db']['1']:
                if h!=5 and h!=6:
                    print(f"{[h]} {i}: {tournament.json_object['tournaments_db']['1'][i]}")
                h += 1
            print("[0] Menu Principal.")
            
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                print("\n--------------------------------------------------")
                print(tournament.json_object['tournaments_db']['1']['Nom du tournoi'])
                tournament.update_tournament_name()
            elif user_choice == "2":
                print("\n--------------------------------------------------")
                print(tournament.json_object['tournaments_db']['1']['Lieu'])
                tournament.update_tournament_location()
            elif user_choice == "3":
                print("\n--------------------------------------------------")
                print(tournament.json_object['tournaments_db']['1']['Date'])
                tournament.update_tournament_date()
            if user_choice == "4":
                print("\n--------------------------------------------------")
                print(tournament.json_object['tournaments_db']['1']['Nombre de tours'])
                tournament.update_tournament_number_of_turns()
            elif user_choice == "5":
                print("\n--------------------------------------------------")
                print(tournament.json_object['tournaments_db']['1']['Tournées'])
                tournament.update_tournament_rounds()
            elif user_choice == "6":
                print("\n--------------------------------------------------")
                print(tournament.json_object['tournaments_db']['1']['Joueurs'])
                tournament.update_tournament_players_info()
            elif user_choice == "7":
                print("\n--------------------------------------------------")
                print(tournament.json_object['tournaments_db']['1']['Contrôle du temps'])
                tournament.update_tournament_time_control()
            elif user_choice == "8":
                print("\n--------------------------------------------------")
                print(tournament.json_object['tournaments_db']['1']['Description'])
                tournament.update_tournament_description()
            elif user_choice == "0":
                print("\n--------------------------------------------------")
                print("Retour au Menu Principal")
                break
            else:
                print("\n==================================================")
                print(f"Vous avez tapé '{user_choice}'.\nChoisissez à nouveau un chiffre sur le menu, svp.\n")


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
                tournament.update_tournament_info()
            elif user_choice == "4":
                update_players_menu()
            elif user_choice == "5":
                break
            elif user_choice == "6":
                exec_main_menu1()
            else:
                view.error_msg()


    ## -- Main Menu -- /!!!\ Must REMAIN ACTIVE to allow other menus to function properly!!!
    def exec_main_menu1():
        """ function to launch main menu within the current file"""

        while True:
            """ Launching Main Menu Interface """
            
            view.main_menu()
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                tournament.add_tournament()
                tournament.save_tournament_data()
                players.clear_roundx_in_tournament_table()
                players.add_roundx_in_tournament_table()
                tournament.update_tournament_players_info()
            elif user_choice == "2":
                players.add_players()
                players.save_players_data()
                players.save_players_indexes_in_tournaments_db()
            elif user_choice == "3":
                view.all_matches_info()
                # view.view_round1_matchups()
                pass
            elif user_choice == "4":
                players.update_player_score()
                players.generate_players_round1_matchup_ref_rating()
                players.generate_players_matchup_reference_score_and_rating()

            elif user_choice == "5":
                view.players_info()
                view.tournament_overview_by_players_by_last_and_first_names()
                view.sorted_players_by_score_and_rating()
                view.tournament_info()
                view.all_rounds_info()
                view.all_matches_info()
                pass
            elif user_choice == "6":
                update_players_menu()
            elif user_choice == "7":
                # update_tournament_menu_out()
                tournament.update_tournament_info()
            elif user_choice == "8":
                view.byebye()
                break
            else:
                view.error_msg()
    exec_main_menu1()
    

else:
    pass
