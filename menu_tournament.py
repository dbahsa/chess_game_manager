
#-----------------------------------------------------
#---------- TOURNAMENT MENU SCRIPT STARTS ------------

if __name__=="__main__":

    def exec_t_menu1():

        """ Menu interface """
        # Tournament menu: [1]Create | [2]Open | [3]Go Back | [4]Exit
        c = "\n---------- 🔥 MENU TOURNOI 🔥 -------------"
        x = "\nEntrer le chiffre:"
        d = "\n[1] pour Créer            [2] pour Ouvrir"
        f = "\n[3] pour Menu Principal   [4] pour Arrêter\n"
        tournament_menu = c+x+d+f
        print(tournament_menu)

        ### ---  Processing Tournament Menu ---

        def input_number(tournament_menu):
            """ input_number: to avoid input errors so that user chooses what's proposed to him/her  """
            while True:
                try:
                    choice = int(input(tournament_menu))    
                except ValueError:
                    print("😅 Veuillez entrer le bon 'chiffre' correspondant à votre choix, svp. Merci!")
                else:
                    return choice
                    break

        # x gets user_choice
        x = input_number("MENU TOURNOI - Faites votre choix: ")
                
        def all_scripts(user_choice):
            """ Launching tournament_menu scripts """
            if user_choice == 1:
                print('choice 1: create a tournament')
                # function()
                    
            elif user_choice == 2:
                print('choice 2: see tournament db')
                # function()
                    
            elif user_choice == 3:
                print('choice 3: go back to main_menu')
                # function()
            
            elif user_choice == 4:
                print("choice 4: quit")
                quit()
            
            # gotta find out how to dislay the current menu again when 'user_choice < 1 or user_choice > 4'
            else:
                user_choice < 1 or user_choice > 4 
                print('🤓 Votre choix doit être entre 1 et 4. Merci de relancer le script svp.')

        all_scripts(x)
    exec_t_menu1()

else:
    def exec_t_menu2():

        """ Menu interface """
        # Tournament menu: [1]Create | [2]Open | [3]Go Back | [4]Exit
        c = "\n---------- 🔥 MENU TOURNOI 🔥 -------------"
        x = "\nEntrer le chiffre:"
        d = "\n[1] pour Créer            [2] pour Ouvrir"
        f = "\n[3] pour Menu Principal   [4] pour Arrêter\n"
        tournament_menu = c+x+d+f
        print(tournament_menu)

        ### ---  Processing Tournament Menu ---

        def input_number(tournament_menu):
            """ input_number: to avoid input errors so that user chooses what's proposed to him/her  """
            while True:
                try:
                    choice = int(input(tournament_menu))    
                except ValueError:
                    print("😅 Veuillez entrer le bon 'chiffre' correspondant à votre choix, svp. Merci!")
                else:
                    return choice
                    break

        # x gets user_choice
        x = input_number("MENU TOURNOI - Faites votre choix: ")
                
        def all_scripts(user_choice):
            """ Launching tournament_menu scripts """
            if user_choice == 1:
                print('choice 1: create a tournament')
                # function()
                    
            elif user_choice == 2:
                print('choice 2: see tournament db')
                # function()
                    
            elif user_choice == 3:
                print('choice 3: go back to main_menu')
                # function()
            
            elif user_choice == 4:
                print("choice 4: quit")
                quit()
            
            # gotta find out how to dislay the current menu again when 'user_choice < 1 or user_choice > 4'
            else:
                user_choice < 1 or user_choice > 4 
                print('🤓 Votre choix doit être entre 1 et 4. Merci de relancer le script svp.')

        all_scripts(x)
