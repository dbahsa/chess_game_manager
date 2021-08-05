import menu_tournament
import menu_players
import menu_reports


#---------------------------------------------
#---------- MAIN MENU SCRIPT STARTS ----------


if __name__=="__main__":

    def exec_main_menu1():

        """ Menu interface """
        # Main menu: [1]Tournament | [2]Players | [3]Reports | [4]Exit
        a = "\n  🚀 GESTIONNAIRE DE TOURNOI D'ECHECS  "
        b = "\n ======================================"
        c = "\n----------- MENU PRINCIPAL -------------"
        x = "\nEntrer le chiffre:"
        d = "\n[1] pour Tournoi       [2] pour Joueurs"
        f = "\n[3] pour Rapports      [4] pour Arrêter\n"
        main_menu = a+b+c+x+d+f
        print(main_menu)

        ### ---  Processing Main Menu ---
        def input_number(main_menu):
            """ input_number: to avoid input errors so that user chooses what's offered to him/her  """
            while True:
                try:
                    choice = int(input(main_menu))
                except ValueError:
                    print("😅 Veuillez entrer le bon 'chiffre' correspondant à votre choix, svp. Merci!")
                else:
                    return choice
                    break

        # x gets user_choice
        x = input_number("MENU PRINCIPAL - Faites votre choix: ")
                
        def all_scripts(user_choice):
            """ Launching Program """
            if user_choice == 1:
                print('choice 1: go to tournament_menu')
                menu_tournament.exec_t_menu2()
                    
            elif user_choice == 2:
                print('choice 2: go to players_menu')
                menu_players.exec_p_menu2()
                    
            elif user_choice == 3:
                print('choice 3: go to reports_menu')
                menu_reports.exec_r_menu2()
            
            elif user_choice == 4:
                print("choice 4: quit prog")
                quit()
            
            # gotta find out how to dislay the current menu again when 'user_choice < 1 or user_choice > 4'
            else:
                user_choice < 1 or user_choice > 4 
                print('🤓 Votre choix doit être entre 1 et 4. Merci de relancer le script svp.')

        all_scripts(x)
    exec_main_menu1()

else:

    def exec_main_menu2():

        """ Menu interface """
        # Main menu: [1]Tournament | [2]Players | [3]Reports | [4]Exit
        a = "\n  🚀 GESTIONNAIRE DE TOURNOI D'ECHECS  "
        b = "\n ======================================"
        c = "\n----------- MENU PRINCIPAL -------------"
        x = "\nEntrer le chiffre:"
        d = "\n[1] pour Tournoi       [2] pour Joueurs"
        f = "\n[3] pour Rapports      [4] pour Arrêter\n"
        main_menu = a+b+c+x+d+f
        print(main_menu)

        ### ---  Processing Main Menu ---
        def input_number(main_menu):
            """ input_number: to avoid input errors so that user chooses what's offered to him/her  """
            while True:
                try:
                    choice = int(input(main_menu))
                except ValueError:
                    print("😅 Veuillez entrer le bon 'chiffre' correspondant à votre choix, svp. Merci!")
                else:
                    return choice
                    break

        # x gets user_choice
        x = input_number("MENU PRINCIPAL - Faites votre choix: ")
                
        def all_scripts(user_choice):
            """ Launching Program """
            if user_choice == 1:
                print('choice 1: go to tournament_menu')
                menu_tournament.exec_t_menu2()
                    
            elif user_choice == 2:
                print('choice 2: go to players_menu')
                menu_players.exec_p_menu2()
                    
            elif user_choice == 3:
                print('choice 3: go to reports_menu')
                menu_reports.exec_r_menu2()
            
            elif user_choice == 4:
                print("choice 4: quit prog")
                quit()
            
            # gotta find out how to dislay the current menu again when 'user_choice < 1 or user_choice > 4'
            else:
                user_choice < 1 or user_choice > 4 
                print('🤓 Votre choix doit être entre 1 et 4. Merci de relancer le script svp.')

        all_scripts(x)