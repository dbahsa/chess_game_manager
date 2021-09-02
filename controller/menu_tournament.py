
# -*- coding: utf-8 -*-

#-----------------------------------------------------
#---------- TOURNAMENT MENU SCRIPT STARTS ------------

if __name__=="__main__":

    def exec_t_menu1():
        """ function to launch reports menu within the current file"""

        def tournament_menu():
            """ Menu interface """
            # Tournament menu: [1]Create | [2]Open | [3]Go Back | [4]Exit
            c = "\n---------- 🔥 MENU TOURNOI 🔥 -------------"
            x = "\nEntrer le chiffre:"
            d = "\n[1] pour Créer            [2] pour Ouvrir"
            f = "\n[3] pour Menu Principal   [4] pour Arrêter\n"
            menu = c+x+d+f
            print(menu)

        while True:
            """ Launching Program """
            tournament_menu()
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

    exec_t_menu1()

else:
    def exec_t_menu2():
        """ function to launch reports menu within the current file"""

        def tournament_menu():
            """ Menu interface """
            # Tournament menu: [1]Create | [2]Open | [3]Go Back | [4]Exit
            c = "\n---------- 🔥 MENU TOURNOI 🔥 -------------"
            x = "\nEntrer le chiffre:"
            d = "\n[1] pour Créer            [2] pour Ouvrir"
            f = "\n[3] pour Menu Principal   [4] pour Arrêter\n"
            menu = c+x+d+f
            print(menu)

        while True:
            """ Launching Program """
            tournament_menu()
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