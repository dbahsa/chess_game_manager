#!/user/bin/env python3
# -*- coding: utf-8 -*-


from dataclasses import dataclass, asdict, field

""" players variables used """
players_number = 8
registered_players = 0
# all_players_data:  exploited by data.py     
all_players_data = []


""" # -- Prog Start here -- """
def player_score():
    """ return a list of player scores after each matchup """
    scores =[]
    return scores

def player_t_in():
    """ to add tournaments in which a player participated in """
    tournaments =[]
    return tournaments

@dataclass
class Player:
    """Class to create player instances"""
    last_name: str
    first_name: str
    gender: str
    rating: int
    scores: list = field(init=False, repr=False, default_factory=player_score)
    tournaments: list = field(init=False, repr=False, default_factory=player_t_in)
    single_pl_info: dict = field(init=False, repr=False)

    def __post_init__(self):
        """ Method to help create player full data"""
        self.single_pl_info = {"Last Name": self.last_name,
                                "First Name": self.first_name,
                                "Genre": self.gender,
                                "Classement Général": self.rating,
                                "Score": self.scores,
                                "Tournois": self.tournaments}


def add_players():
    """ function to instantiate players"""
    print("\n🚀 Bonjour! Procédons à l'enregistrement des 8 joueurs")
    # !!! DO NOT FORGET TO CHANGE THE RANGE BELOW TO REFLECT USER'S REQUIREMENTS OF 8 PLAYERS
    # replace 3 by players_number -> range(1, players_number+1)sz
    for i in range(1,3):
        print(f"\n🔥 Entrer les informations sur le joueur n°{i}")
        p = Player(input("- Nom de famille: "), 
                    input("- Prénom: "),
                    input("- Genre : "),
                    input("- Nombre de Points au Classement Général: ")
                    )
        all_players_data.append(p.single_pl_info)
        # print("-------------------------------------")
    print("\n🤓 Merci. Les 8 joueurs ont bien été enregistrés!")
    print("Passons à l'étape suivante dès à présent...\n")


add_players()
for p in all_players_data:
    print(p)
# print(all_players_data)

   
'''
        # def all_scripts(user_choice):
        #     """ Launching Program """
        #     if user_choice == 1:
        #         print('choice 1: go to tournament_menu')
        #         menu_tournament.exec_t_menu2()
                    
        #     elif user_choice == 2:
        #         print('choice 2: go to players_menu')
        #         menu_players.exec_p_menu2()
                    
        #     elif user_choice == 3:
        #         print('choice 3: go to reports_menu')
        #         menu_reports.exec_r_menu2()
            
        #     elif user_choice == 4:
        #         print("choice 4: quit prog")
        #         quit()
            
        #     # gotta find out how to dislay the current menu again when 'user_choice < 1 or user_choice > 4'
        #     else:
        #         user_choice < 1 or user_choice > 4 
        #         print('🤓 Votre choix doit être entre 1 et 4. Merci de relancer le script svp.')
                

        # all_scripts(x)

'''