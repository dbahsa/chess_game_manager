
#------------------------------------------------
#---------- PLAYERS MENU SCRIPT STARTS ----------

if __name__=="__main__":
    
    def exec_p_menu1():

        """ Menu interface """
        # Players menu: [1]Create | [2]Open | [3]Go Back | [4]Exit
        c = "\n---------- 🔥 MENU JOUEURS 🔥 -------------"
        x = "\nEntrer le chiffre:"
        d = "\n[1] pour Créer            [2] pour Ouvrir"
        f = "\n[3] pour Menu Principal   [4] pour Arrêter\n"
        players_menu = c+x+d+f
        print(players_menu)


        ### ---  Processing Players Menu ---

        def input_number(players_menu):
            """ input_number: to avoid input errors so that user chooses what's proposed to him/her  """
            while True:
                try:
                    choice = int(input(players_menu))
                except ValueError:
                    print("😅 Veuillez entrer le bon 'chiffre' correspondant à votre choix, svp. Merci!")
                else:
                    return choice
                    break

        # x gets user_choice
        x = input_number("MENU JOUEURS - Faites votre choix: ")
                
        def all_scripts(user_choice):
            """ Launching players_menu scripts """
            if user_choice == 1:
                print('choice 1: create players')
                # function()
                    
            elif user_choice == 2:
                print('choice 2: see players')
                # function()
                    
            elif user_choice == 3:
                print('choice 3: go back to main_menu')
                # function()
            
            elif user_choice == 4:
                print("quit prog")
                quit()
            
            # gotta find out how to dislay the current menu again when 'user_choice < 1 or user_choice > 4'
            else:
                user_choice < 1 or user_choice > 4 
                print('🤓 Votre choix doit être entre 1 et 4. Merci de relancer le script svp.')

        all_scripts(x)
    exec_p_menu1()

else:
    def exec_p_menu2():

        """ Menu interface """
        # Players menu: [1]Create | [2]Open | [3]Go Back | [4]Exit
        c = "\n---------- 🔥 MENU JOUEURS 🔥 -------------"
        x = "\nEntrer le chiffre:"
        d = "\n[1] pour Créer            [2] pour Ouvrir"
        f = "\n[3] pour Menu Principal   [4] pour Arrêter\n"
        players_menu = c+x+d+f
        print(players_menu)


        ### ---  Processing Players Menu ---

        def input_number(players_menu):
            """ input_number: to avoid input errors so that user chooses what's proposed to him/her  """
            while True:
                try:
                    choice = int(input(players_menu))
                except ValueError:
                    print("😅 Veuillez entrer le bon 'chiffre' correspondant à votre choix, svp. Merci!")
                else:
                    return choice
                    break

        # x gets user_choice
        x = input_number("MENU JOUEURS - Faites votre choix: ")
                
        def all_scripts(user_choice):
            """ Launching players_menu scripts """
            if user_choice == 1:
                print('choice 1: create players')
                # function()
                    
            elif user_choice == 2:
                print('choice 2: see players')
                # function()
                    
            elif user_choice == 3:
                print('choice 3: go back to main_menu')
                # function()
            
            elif user_choice == 4:
                print("quit prog")
                quit()
            
            # gotta find out how to dislay the current menu again when 'user_choice < 1 or user_choice > 4'
            else:
                user_choice < 1 or user_choice > 4 
                print('🤓 Votre choix doit être entre 1 et 4. Merci de relancer le script svp.')

        all_scripts(x)
    