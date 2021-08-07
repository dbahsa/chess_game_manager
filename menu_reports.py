# -*- coding: utf-8 -*-

#------------------------------------------------
#---------- REPORTS MENU SCRIPT STARTS ----------


if __name__=="__main__":

    def exec_r_menu1():
        """ function to launch players menu within the current file"""

        def reports_menu():
            """ Menu interface """
            # Reports menu: [1]Actors | [2]Players | [3]Tournaments | [4]Rounds | [5]Matches | [6]Go Back | [7]Exit
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
                print('choice 6: go to reports_menu')
                # menu_reports.exec_r_menu2()
            elif user_choice == "7":
                print("Merci d'avoir utilisé notre programme et à bientôt 😉")
                break
            else:
                print(f"😅 Vous avez taper '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 7.\n")

    exec_r_menu1()

else: 
    def exec_r_menu2():

        def reports_menu():
            """ Menu interface """
            # Reports menu: [1]Actors | [2]Players | [3]Tournaments | [4]Rounds | [5]Matches | [6]Go Back | [7]Exit
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
                print('choice 6: go to reports_menu')
                # menu_reports.exec_r_menu2()
            elif user_choice == "7":
                print("Merci d'avoir utilisé notre programme et à bientôt 😉")
                break
            else:
                print(f"😅 Vous avez taper '{user_choice}'.\n🙂 Merci de faire un choix entre 1 et 7.\n")