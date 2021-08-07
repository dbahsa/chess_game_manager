# -*- coding: utf-8 -*-

import menu_tournament
import menu_players
import menu_reports


#---------------------------------------------
#---------- MAIN MENU SCRIPT STARTS ----------


if __name__=="__main__":

    def exec_main_menu1():
        """ function to launch main menu within the current file"""

        def main_menu():
            """ Main Menu interface """
            # Main menu: [1]Tournament | [2]Players | [3]Reports | [4]Exit
            a = "\n 🏁 GESTIONNAIRE DE TOURNOI D'ECHECS 🏁"
            b = "\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            c = "\n~~~~~~~~~~ 🏠 MENU PRINCIPAL ~~~~~~~~~~~~"
            x = "\n Entrer le chiffre:"
            d = "\n [1] pour Tournoi       [2] pour Joueurs"
            f = "\n [3] pour Rapports      [4] pour Arrêter"
            g = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            menu = a+b+c+x+d+f+g
            print(menu)
                
        while True:
            """ Launching Program """
            main_menu()
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
            elif user_choice == "4":
                print("Merci d'avoir utilisé notre programme et à bientôt 😉")
                break
            else:
                print(f"😅 Vous avez taper '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 4.\n")
                
    exec_main_menu1()

else:
    def exec_main_menu2():
        """ function to launch main menu within the current file"""

        def main_menu():
            """ Main Menu interface """
            # Main menu: [1]Tournament | [2]Players | [3]Reports | [4]Exit
            a = "\n 🏁 GESTIONNAIRE DE TOURNOI D'ECHECS 🏁"
            b = "\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            c = "\n~~~~~~~~~~ 🏠 MENU PRINCIPAL ~~~~~~~~~~~~"
            x = "\n Entrer le chiffre:"
            d = "\n [1] pour Tournoi       [2] pour Joueurs"
            f = "\n [3] pour Rapports      [4] pour Arrêter"
            g = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            menu = a+b+c+x+d+f+g
            print(menu)
                
        while True:
            """ Launching Program """
            main_menu()
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
            elif user_choice == "4":
                print("Merci d'avoir utilisé notre programme et à bientôt 😉")
                break
            else:
                print(f"😅 Vous avez taper '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 4.\n")
