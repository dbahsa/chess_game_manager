#! /user/bin/env python3
# -*- coding: utf-8 -*-


""" modules & packages """
import json
from tinydb import TinyDB
import pandas as pd


import tournament, players
import view


""" START USER/PLAYERS MATCH/ROUNDS SCRIPT /!!!\ """

if __name__=="__main__":
    """Launch program to add/update players, macthes, and rounds"""

    view.welcome_msg()

    """Update Menus"""

    ## -- Compute next round steps -- 
    def compute_next_round_menu():
        """ function to compute next round steps"""

        while True:
            """ Launching Program """
            
            view.compute_next_round_menu()
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                players.erase_all_scores()
                players.generate_save_round1_matchups()
                view.players_info()
                view.view_round1_matchups()
            elif user_choice in ["a","e","h","m"]:
                launch_games_menu()
            elif user_choice in ["b","f","i","n"]:
                stop_games_menu()
            elif user_choice == "c":
                view.players_info()
                players.update_player_score()
                players.save_round1_matchups()
                players.generate_save_round2_matchups()
            elif user_choice == "v":
                view.players_info()
                players.update_player_score()
                players.save_round2_scores()
                players.generate_save_round3_matchups()
            elif user_choice == "k":
                view.players_info()
                players.update_player_score()
                players.save_round3_scores()
                players.generate_save_round4_matchups()
            elif user_choice == "p":
                view.players_info()
                players.update_player_score()
                players.save_round4_scores()
            elif user_choice == "2":
                view.view_round2_matchups()
            elif user_choice == "3":
                view.view_round3_matchups()
            elif user_choice == "4":
                view.view_round4_matchups()
            elif user_choice == "5":
                break
            else:
                view.error_msg()


    ## -- Ending time Games Menu --
    def stop_games_menu():
        """ function to launch games per round"""

        while True:
            """ End Timer """
            
            view.stop_games_menu()
            user_choice = input("\nPour arrêter quel round svp? Taper votre choix: ")
            if user_choice == "1":
                current_time = players.datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de finir!")
                print("En cas d'erreur, revenir en arrière pour réinitialiser la fin des jeux,", end="")
                print("puis recommencer")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                players.json_object['tournaments_db']['1']['Tournées']["Round1"]['Temps de fin'] = a
                with open(players.filename, "w") as f:
                    json.dump(players.json_object, f, indent=4)
            elif user_choice == "2":
                current_time = players.datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de finir!")
                print("En cas d'erreur, revenir en arrière pour rréinitialiser la fin des jeux,", end="")
                print("puis recommencer")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                players.json_object['tournaments_db']['1']['Tournées']["Round2"]['Temps de fin'] = a
                with open(players.filename, "w") as f:
                    json.dump(players.json_object, f, indent=4)
            elif user_choice == "3":
                current_time = players.datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de finir!")
                print("En cas d'erreur, revenir en arrière pour réinitialiser la fin des jeux,", end="")
                print("puis recommencer")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                players.json_object['tournaments_db']['1']['Tournées']["Round3"]['Temps de fin'] = a
                with open(players.filename, "w") as f:
                    json.dump(players.json_object, f, indent=4)
            elif user_choice == "4":
                current_time = players.datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de finir!")
                print("En cas d'erreur, revenir en arrière pour réinitialiser la fin des jeux,", end="")
                print("puis recommencer")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                players.json_object['tournaments_db']['1']['Tournées']["Round4"]['Temps de fin'] = a
                with open(players.filename, "w") as f:
                    json.dump(players.json_object, f, indent=4)
            elif user_choice == "5":
                break
            else:
                view.error_msg()


    ## -- Launch Game Menu --
    def launch_games_menu():
        """ function to launch games per round"""

        while True:
            """ Launching Games """
            
            view.launch_games_menu()
            user_choice = input("\nPour quel round svp? Taper votre choix: ")
            if user_choice == "1":
                current_time = players.datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de commencer!")
                print("En cas d'erreur, revenir en arrière pour réinitialiser le début des jeux,", end="")
                print("puis recommencer")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                players.json_object['tournaments_db']['1']['Tournées']["Round1"]['Temps de départ'] = a
                with open(players.filename, "w") as f:
                    json.dump(players.json_object, f, indent=4)
            elif user_choice == "2":
                current_time = players.datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de commencer!")
                print("En cas d'erreur, revenir en arrière pour rréinitialiser le début des jeux,", end="")
                print("puis recommencer")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                players.json_object['tournaments_db']['1']['Tournées']["Round2"]['Temps de départ'] = a
                with open(players.filename, "w") as f:
                    json.dump(players.json_object, f, indent=4)
            elif user_choice == "3":
                current_time = players.datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de commencer!")
                print("En cas d'erreur, revenir en arrière pour réinitialiser le début des jeux,", end="")
                print("puis recommencer")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                players.json_object['tournaments_db']['1']['Tournées']["Round3"]['Temps de départ'] = a
                with open(players.filename, "w") as f:
                    json.dump(players.json_object, f, indent=4)
            elif user_choice == "4":
                current_time = players.datetime.datetime.now()
                print(f"Il est {current_time.hour}h:{current_time.minute}, les matches viennent de commencer!")
                print("En cas d'erreur, revenir en arrière pour réinitialiser le début des jeux,", end="")
                print("puis recommencer")
                a= f"{current_time.day}/{current_time.month}/{current_time.year} à {current_time.hour}h:{current_time.minute}"
                players.json_object['tournaments_db']['1']['Tournées']["Round4"]['Temps de départ'] = a
                with open(players.filename, "w") as f:
                    json.dump(players.json_object, f, indent=4)
            elif user_choice == "5":
                break
            else:
                view.error_msg()


    ## -- Reports Menu --
    def latest_reports_menu():
        """ function to view differents reports"""

        while True:
            """ Launching Program """
            
            view.latest_reports_menu()
            user_choice = input("\nTaper votre choix: ")
            if user_choice == "1":
                view.tournament_overview_by_players_by_last_and_first_names()
            elif user_choice == "2":
                view.sorted_players_by_score_and_rating()
            elif user_choice == "3":
                view.tournament_info()
            elif user_choice == "4":
                view.all_rounds_info()
            elif user_choice == "5":
                view.all_matches_info()
            elif user_choice == "6":
                view.byebye()
                break
            else:
                view.error_msg()
    

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
                update_tournament_menu_out()
            elif user_choice == "2":
                update_players_menu()
            elif user_choice == "3":
                update_tournament_menu_out()
            elif user_choice == "4":
                update_players_menu()
            elif user_choice == "5":
                launch_games_menu()
            elif user_choice == "6":
                stop_games_menu()
            elif user_choice == "7":
                compute_next_round_menu()
            elif user_choice == "8":
                update_players_menu()
            elif user_choice == "9":
                latest_reports_menu()
                pass
            elif user_choice == "0":
                break
            else:
                view.error_msg()
    exec_main_menu1()


else:
    pass
