
#------------------------------------------------
#---------- REPORTS MENU SCRIPT STARTS ----------


if __name__=="__main__":

    def exec_r_menu1():

        """ Menu interface """

        # Reports menu: [1]Actors | [2]Players | [3]Tournaments | [4]Rounds | [5]Matches | [6]Go Back | [7]Exit
        c = "\n-------- 🔥 MENU RAPPORTS 🔥 -------------"
        d = "\nEntrer le chiffre:"
        e = "\n[1] pour Acteurs     [2] pour Joueurs"
        f = "\n[3] pour Tournois    [4] pour Tours"
        g = "\n[5] pour Matches     [6] pour Menu Principal"
        h = "\n[7] pour Arrêter\n"
        reports_menu = c+d+e+f+g+h
        print(reports_menu)

        ### ---  Processing Main Menu ---

        def input_number(reports_menu):
            """ input_number: to avoid input errors so that user chooses what's proposed to him/her  """
            while True:
                try:
                    choice = int(input(reports_menu))    
                except ValueError:
                    print("😅 Veuillez entrer le bon 'chiffre' correspondant à votre choix, svp. Merci!")
                else:
                    return choice
                    break

        # x gets user_choice
        x = input_number("MENU RAPPORTS - Faites votre choix: ")
                
        def all_scripts(user_choice):
            """ Launching Program """
            if user_choice == 1:
                print('choice 1: rapports actors')
                # function()
                    
            elif user_choice == 2:
                print('choice 2: rapports players')
                # function()
                    
            elif user_choice == 3:
                print('choice 3: rapports tournaments')
                # function()
                    
            elif user_choice == 4:
                print('choice 4: rapports rounds')
                # function()
                    
            elif user_choice == 5:
                print('choice 5: rapports matches')
                # function()
            
            elif user_choice == 6:
                print('choice 6: back to main_menu')
                # function()
                            
            elif user_choice == 7:
                print("choice 7: quit prog")
                quit()
            
            # gotta find out how to dislay the current menu again when 'user_choice < 1 or user_choice > 7'
            else:
                user_choice < 1 or user_choice > 7
                print('🤓 Votre choix doit être entre 1 et 7. Merci de relancer le script svp.')

        all_scripts(x)
    exec_r_menu1()

else: 
    def exec_r_menu2():

        """ Menu interface """

        # Reports menu: [1]Actors | [2]Players | [3]Tournaments | [4]Rounds | [5]Matches | [6]Go Back | [7]Exit
        c = "\n-------- 🔥 MENU RAPPORTS 🔥 -------------"
        d = "\nEntrer le chiffre:"
        e = "\n[1] pour Acteurs     [2] pour Joueurs"
        f = "\n[3] pour Tournois    [4] pour Tours"
        g = "\n[5] pour Matches     [6] pour Menu Principal"
        h = "\n[7] pour Arrêter\n"
        reports_menu = c+d+e+f+g+h
        print(reports_menu)

        ### ---  Processing Main Menu ---

        def input_number(reports_menu):
            """ input_number: to avoid input errors so that user chooses what's proposed to him/her  """
            while True:
                try:
                    choice = int(input(reports_menu))    
                except ValueError:
                    print("😅 Veuillez entrer le bon 'chiffre' correspondant à votre choix, svp. Merci!")
                else:
                    return choice
                    break

        # x gets user_choice
        x = input_number("MENU RAPPORTS - Faites votre choix: ")
                
        def all_scripts(user_choice):
            """ Launching Program """
            if user_choice == 1:
                print('choice 1: rapports actors')
                # function()
                    
            elif user_choice == 2:
                print('choice 2: rapports players')
                # function()
                    
            elif user_choice == 3:
                print('choice 3: rapports tournaments')
                # function()
                    
            elif user_choice == 4:
                print('choice 4: rapports rounds')
                # function()
                    
            elif user_choice == 5:
                print('choice 5: rapports matches')
                # function()
            
            elif user_choice == 6:
                print('choice 6: back to main_menu')
                # function()
                            
            elif user_choice == 7:
                print("choice 7: quit prog")
                quit()
            
            # gotta find out how to dislay the current menu again when 'user_choice < 1 or user_choice > 7'
            else:
                user_choice < 1 or user_choice > 7
                print('🤓 Votre choix doit être entre 1 et 7. Merci de relancer le script svp.')

        all_scripts(x)
    