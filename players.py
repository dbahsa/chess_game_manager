#! /user/bin/env python3
# -*- coding: utf-8 -*-

""" modules & packages """
import json
from dataclasses import dataclass, asdict, field
import pandas as pd
from tinydb import TinyDB
# from data import save_players_data2


""" players variables used to launch the script """
total_number_of_players = 8
registered_players = 0
# all_players_db:  exploited by data.py     
all_players_db = [] # ---  /!!!\ MUST BE SORTED BEFORE SAVING IT TO DB FILE ---
# db: var containing tournament data file
db = TinyDB('tournament_data.json')

""" # -- Prog Start here -- """
def player_score():
    """ return a list of player scores after each matchup """
    scores =[]
    return scores

def player_tournament_participation():
    """ to add tournaments in which a player participated in """
    tournaments =[]
    return tournaments

@dataclass
class Player:
    """Class to create player instances"""
    last_name: str
    first_name: str
    birth_date: str
    gender: str
    rating: int
    scores: list = field(init=False, repr=False, default_factory=player_score)
    tournaments: list = field(init=False, repr=False, default_factory=player_tournament_participation)
    single_player_db: dict = field(init=False, repr=False)

    def __post_init__(self):
        """ Method to help create player full data"""
        self.single_player_db = {"Nom de famille": self.last_name,
                                "Prénom": self.first_name,
                                "Date de naissance": self.birth_date,
                                "Sexe": self.gender,
                                "Classement": self.rating,
                                "Score": self.scores,
                                "Tournois": self.tournaments}


## -- /!!!\ create an input func for all class properties such as below (ask_lname, ask_gender...) 


"""
# -- To Do!
def ask_lname():
    lname = input("Entrer le nom de famille: ")
    if lname == "":
        print("Veuillez saisir le nom de famille svp. Merci!")
        return ask_lname() # this allows to ask the user the lname again; this will keep on asking so as long as the user doens't answer the question
    return lname # once lname obtained it can be pushed to function "add_players", where p = Player(last_name = lname...)

player_last_name = ask_lname()

# -- To Do!
def ask_gender():
    player_gender = input("Entrer le sexe, F (femme) ou H (homme): ")
    if player_gender != "m".upper() or player_gender != "f".upper():
        print("Veuillez saisir le sexe en tapant F (femme) ou H (homme). Merci!")
        return ask_gender() # this allows to ask the user the lname again; this will keep on asking so as long as the user doens't answer the question
    return player_gender # once lname obtained it can be pushed to function "add_players", where p = Player(last_name = lname...)
player_gender = ask_gender()
"""


# --  Done! Gotta be reajusted when above functions will updated
def add_players():
    """ function to instantiate players"""
    print("\n🚧 Enregistrement des 8 joueurs 🚧")
    # !!! DO NOT FORGET TO CHANGE THE RANGE BELOW TO REFLECT USER'S REQUIREMENTS OF 8 PLAYERS
    # replace 3 by total_number_of_players -> range(1, total_number_of_players+1)
    for i in range(1,9):
        print(f"\n🔥 Entrer les informations sur le joueur n°{i}")
        p = Player(input("- Nom de famille: "), # replace input with: 'player_last_name' obteined above
                    input("- Prénom: "), # player_fname
                    input("- Date de naissance telle que jj/mm/aaaa (ex: 18/02/1973): "), # player_dob
                    input("- Sexe [H/F]: ").upper(), # player_gender
                    int(input("- Classement: ")) # player_rating
                    )
        all_players_db.append(p.single_player_db)
        # print("-------------------------------------")
    print("\n🤓 Merci. Les 8 joueurs ont bien été enregistrés!")
    print("Passons à l'étape suivante dès à présent...\n")


# -- Done! Gotta be reajusted when above functions will updated
def save_players_data():
    """ save players data """
    # db = TinyDB('tournament_data.json')
    # players table: 'players_db'
    players_table = db.table('players_db')
    players_table.truncate() # clear up the table first
    players_table.insert_multiple(all_players_db)


# -- To Do!
def save_players_indexes_in_tournaments_db():
    pass

""" VAR TO READ DB FILE """
# -- 'filename' created to access & update data file: --
filename = 'tournament_data.json'

with open(filename, "r") as f:
    temp = json.load(f)
# with open(filename, "w") as f:
#     json.dump(temp, f, indent=4)


""" VAR TO SORT PLAYERS DATA """
# -- Unsorted Players by rating: --
unsorted_players = {}
for s in temp["players_db"].items():
    y = s[0]
    w = list(s[1].values())
    unsorted_players[y] = w

# -- Sorted Players by rating: --
sorted_players_by_rating = sorted(unsorted_players.items(), key=lambda x: x[1][4], reverse = True)

# -- Sorted Players by score and rating: --
sorted_players_by_score_and_rating = sorted(unsorted_players.items(), key=lambda x: (sum(x[1][5]), x[1][4]), reverse = True)

# print("\n--- Players UNSORTED _ranking  & num of points at the end of Round1 --\n")
# players_names_ranking_points = []
# for t in range(len(serialized_players)):
#     player_name_ranking_point = [serialized_players[t]['lname'], serialized_players[t]['points'], serialized_players[t]['ranking']]
#     print(serialized_players[t]['lname'], serialized_players[t]['points'], serialized_players[t]['ranking'])
#     players_names_ranking_points.append(player_name_ranking_point)

# print("\n--- Players SORTED _num of Points & Ranking at the end of Round1 --\n")
# sorted_players_by_points = sorted(unsorted_players.items(), key = lambda x: (x[1], x[2]), reverse = True)
# for s in sorted_players_by_points:
#     print(s)

# -- View Ranked Players Based on their Rating points:
# print("\n         - Classement des joueurs au début du tournoi -")
# print("---------------------------------------------------------------------------")
# n = 0
# for i in sorted_players_by_rating:
#     print(f"N°{n+1} avec l'indexe {i[0]}: '{i[1][1]} {i[1][0]}', '{i[1][4]}' points, avec un score de '{i[1][5]}'")
#     n += 1
# print("---------------------------------------------------------------------------\n")
# -- OUTPUT: 
# -- Classement des joueurs au début du tournoi --
# N°1 avec l'indexe 6: 'Brenn Nzimbi', '9999' points, avec un score de '[]'
# N°2 avec l'indexe 7: 'Alexia Laville', '9998' points, avec un score de '[]'
# N°3 avec l'indexe 4: 'Mary Gendre', '4543' points, avec un score de '[]'
# N°4 avec l'indexe 8: 'Corine Lafarge', '4543' points, avec un score de '[]'
# N°5 avec l'indexe 3: 'John Hamel', '3445' points, avec un score de '[]'
# N°6 avec l'indexe 2: 'Lionel Prudom', '2345' points, avec un score de '[]'
# N°7 avec l'indexe 1: 'Paul Lyons', '1234' points, avec un score de '[]'
# N°8 avec l'indexe 5: 'Sophia Gaillard', '1221' points, avec un score de '[]'


"""Variables used for rounds & matchups instances"""
# -- Rounds list (is a dict) comprises all rounds --
rounds = {}

# -- Done! --
def view_unsorted_players_list():
    """ This function allows to ONLY see unsorted players list """

    # -- PANDAS PLAYERS TABLE
    print("\n                 -  Liste non-triée des joueurs -")
    print("---------------------------------------------------------------------------")
    # -- Unsorted players --
    df = pd.DataFrame.from_dict(temp["players_db"], orient='index')
    print(df)


# -- Done! --
def view_sorted_players_list_by_rating():
    """ This function allows to ONLY see unsorted players list """

    # -- PANDAS Sorted players by rating
    print("\n     - Liste triée des joueurs par points au 'Classement' général -")
    print("---------------------------------------------------------------------------")
    df = pd.DataFrame.from_dict(temp["players_db"], orient='index')
    x = df.sort_values(by=['Classement'], ascending=False)
    print(x)


# -- Done! --
def view_ranked_players_by_rating_only():
    """Function to view players list based on their rating ONLY"""

    print("\n- Classement Général des Joueurs -")
    print("---------------------------------------------------------------------------")
    n = 0
    for i in sorted_players_by_rating:
        # print(f"N°{n+1} avec l'indexe {i[0]}: {i[1][1]} {i[1][0]}, {i[1][4]} points")
        print(f'Membre n°{i[0]}: {i[1][1]} {i[1][0]},  n°{n+1} au classement général avec {i[1][4]} points')
        n += 1
    print("---------------------------------------------------------------------------\n")


# -- Done! --
def view_ranked_players_by_score_and_rating():
    """Function to view players list based on their rating ONLY"""

    print("\n- Joueurs Triés par Score et Classement Général -")
    print("---------------------------------------------------------------------------")
    n = 0
    for i in sorted_players_by_score_and_rating:
        print(f'Membre n°{i[0]}: {i[1][1]} {i[1][0]}  est actuellement n°{n+1} avec un score de {sum(i[1][5])}')
        n += 1
    print("---------------------------------------------------------------------------\n")


""" VAR used to create matchups """
# -- Players matchup reference_rating is used to sort items used to pair up players in a round1 ONLY
players_matchup_reference_rating = []
# -- Players matchup reference_score_and_rating is used to sort items used to pair up players in a round1 ONLY
players_matchup_reference_score_and_rating = []


# -- Done! --
def create_players_matchup_with_reference_rating():
    """ Function used to create 'sorted_players_by_rating' variable """

    # -- Get Player reference for matchups, to be listed in 'players_matchup_reference_rating'
    for i in sorted_players_by_rating:
        a = [i[0], sum(i[1][5])]
        players_matchup_reference_rating.append(a)


# -- Done!  --
def create_players_matchup_reference_score_and_rating():
    """ Function used to create 'sorted_players_by_rating' variable """

    # -- Get Player reference for matchups, to be listed in 'players_matchup_reference_rating'
    for i in sorted_players_by_score_and_rating:
        a = [i[0], sum(i[1][5])]
        players_matchup_reference_score_and_rating.append(a)


# -- Update in progress ... --
def generate_round1_matchups():
    """ Function to create matchups per round """

    # -- Generate the 1st pairs of players in Round 1
    a = players_matchup_reference_rating
    x = slice(0,4)
    y = slice(4,8)
    z = zip(a[x],a[y])

    # -- adding Round1 matchups to tournament rounds instance
    round1_matchups = {}
    
    i=1
    for g in list(z):
        round1_matchups["Match n°str(i)"] = g
        i += 1
    
    rounds["Round1"] = round1_matchups

    # round1_matchups =[]
    # for g in list(z):
    #     round1_matchups.append(g)
    # rounds["Round1"] = round1_matchups


# -- To do!
def generate_next_rounds_matchups():
    pass

# -- Done! --
def view_round1_matchups():
    """ Function to view Round1 matchups """

    # -- The user must know member number in order to enter their scores
    view_ranked_players_by_rating_only()
    print("======= 🏁 Matches Round1 🏁 ======\n")
    for i in range(len(rounds["Round1"])):
        print(f"Match n°{i+1}: {rounds['Round1'][i]}")
    print("\n🚧 Match n°x: ([n° membre, son score], [n° autre membre, son score]) 🚧")
    print("========================================================================\n")


# -- To do!
def view_generate_next_rounds_matchups():
    pass


# -- To do!
def view_next_rounds_matchups():
    pass


# -- Update in progress ... --
def save_rounds_in_db():
    """Function to save rounds instance in tournaments_db in db file """

    # -- Open and save rounds data in tournament table in db file
    with open(filename, "w") as f:
        temp["tournaments_db"]["1"]['Tourn\u00e9es'] = rounds
        json.dump(temp, f)
        # json.dump(temp, f, indent=4)


# -- Done! --
def view_rounds_in_db():
    """ Function to view Round1 data from db file """

    # -- 'r' collects round data from db file so that we could print it as needed
    # -- We stay focused on 'r = temp["tournaments_db"]["1"]["Tourn\u00e9es"]'
    # -- because it concerns the current tournament 
    r = temp["tournaments_db"]["1"]["Tourn\u00e9es"]

    for i in range(5):
        if i == 0:
            try:
                print(f"🏁 Les matches du Round{i+1} 🏁")
                q = 1
                for h in r['Round'+str(i+1)]:
                    # print(h)
                    print(f"Match n°{q}: {h}")
                    q +=1
                print("\n🚧 Match n°x: ([n° membre, son score], [n° autre membre, son score]) 🚧")
                print("-------------------------------------------------------------------------")
                # -- The user must know member number in order to enter their scores
                view_ranked_players_by_score_and_rating()
                view_ranked_players_by_rating_only()
            except:
                print(f"Round{i+1} is not ready yet.")
            # try:
            #     print(f"\n--- Round{i+2} Matchups From DB File --")
            #     for h in r[i]['Round'+str(i+2)]:
            #         print(h)
            # except:
            #     # print(f"Round{i+2} is not available yet.")
            # try:
            #     print(f"\n--- Round{i+3} Matchups From DB File --")
            #     for h in r[i]['Round'+str(i+3)]:
            #         print(h)
            # except:
            #     # print(f"Round{i+3} is not available yet.")
            # try:
            #     print(f"\n--- Round{i+4} Matchups From DB File --")
            #     for h in r[i]['Round'+str(i+4)]:
            #         print(h)
            # except:
            #     # print(f"Round{i+4} is not available yet.")


# -- Update in progress ... see below on trial in __main__ --
def input_scores():
    pass


# -- To Do! --
def update_rounds_from_db():
    pass


# -- To do! --
def view_input_scores():
    pass


# -- To do! --
def save_scores_to_db():
    pass




""" START USER/PLAYERS SCRIPT """

if __name__=="__main__":
    """Launch program to add/update players, macthes, and rounds"""

    # -- Done!
    # -- Add & Save Players to DB file --
    # add_players()
    # save_players_data()
    
    # -- Done!
    # -- Create/View Round1 Matchups & Save them to db file --
    # view_unsorted_players_list()
    # view_sorted_players_list_by_rating()
    # view_ranked_players_by_rating_only()

    # -- Done!
    # -- The next functions MUST be initiated in order to save data in db file --
    create_players_matchup_with_reference_rating()
    create_players_matchup_reference_score_and_rating()
    # generate_round1_matchups()
    # view_round1_matchups()
    # save_rounds_in_db()
    # view_rounds_in_db()

    # view_ranked_players_by_score_and_rating()

    # -- To be done!
    # -- UPDATE SCORE --

    # print(temp["players_db"].keys())
    # print(temp["players_db"]["1"]['Sexe'])
    # print(range(len(temp["players_db"].keys())))
    # for a in range(len(temp["players_db"].keys())):
    #     print(a+1)

    # -- creating a function to collect score from the user
    def ask_player_index():
        print("Pour entrer un score")
        ask_index = input("Veuillez taper le numéro du membre, svp: ")
        try: 
            if int(ask_index)>0 or int(ask_index)<=range(len(temp["players_db"].keys())): 
                # print(f'Vous allez taper le score de {temp["players_db"][str(ask_index)]["Nom de famille"]}')
                ask_score = float(input(f'Taper le score de {temp["players_db"][str(ask_index)]["Nom de famille"]}: '))
                # print(f'Le nouveau score de {temp["players_db"][str(ask_index)]["Nom de famille"]} est: {ask_score}')
                with open(filename, "w") as f:
                    temp["players_db"][str(ask_index)]["Score"].append(ask_score) # /!!!\ MUST FIND A WAY TO LINK 'ask_score' TO TOURNAMENT TABLE
                    # -- A corriger: temp["tournaments_db"]["1"]['Tourn\u00e9es']["Round1"].append(ask_score)
                    json.dump(temp, f, indent=4)
            else:
                print("Mauvaise saisie...")
                return ask_player_index()
        except:
            print("Mauvaise saisie...")
            return ask_player_index()

    # ask_player_index()
    # print("\n--- En résumé ---")
    # print(f'Scores de {temp["players_db"]["1"]["Nom de famille"]}: {temp["players_db"]["1"]["Score"]}')
    # print(f'Score Final de {temp["players_db"]["1"]["Nom de famille"]} dans ce tournoi: {sum(temp["players_db"]["1"]["Score"])}')

    # -- Save Rounds data to tournaments_db
    
    # -- Generate the 1st pairs of players in Round 1
    # a = players_matchup_reference_rating
    a = players_matchup_reference_score_and_rating
    x = slice(0,4)
    y = slice(4,8)
    z = zip(a[x],a[y])

    # -- adding Round1 matchups to tournament rounds instance
    round1_matchups = {}
    i = 1
    for m in list(z):
        round1_matchups[f"Match n°{int(i)}"] = m
        i += 1
    
    for d in round1_matchups.items():
        print(d[1])
    
    print("---")
    for o in players_matchup_reference_score_and_rating:
        print(o)

    print("---")
    for h in sorted_players_by_score_and_rating:
        print(h)

    # print(round1_matchups)
    # rounds["Round1"] = round1_matchups


    # -- Open and save rounds data in tournament table in db file
    # with open(filename, "w") as f:
    #     temp["tournaments_db"]["1"]['Tourn\u00e9es'] = rounds
    #     json.dump(temp, f)
        # json.dump(temp, f, indent=4)

    """
    p_score = temp["players_db"]["i"]["Score"] , 'i' is a player's index in the table

    def ask_player_index():
        ask_index = int(input("Taper le score du membre n°: "))
        
        if (ask_index+1) in range(len(temp["players_db"].keys())):
            ask_score = int(input(f"Quel est le score du membre n°{ask_index}: "))
            print(temp["players_db"]["(ask_index)"]["Score"])
            # temp["players_db"]["(ask_index)"]["Score"] = ask_score

    """


    """ 
    We wanna get players db 'round1_matchups[i]' to update them:
    🏁 Les matches du Round1 🏁
    Match n°1: [['6', 0], ['3', 0]]
    Match n°2: [['7', 0], ['2', 0]]
    Match n°3: [['4', 0], ['1', 0]]
    Match n°4: [['8', 0], ['5', 0]]
    🚧 Match n°x: ([n° membre, son score], [n° autre membre, son score]) 🚧
    -------------------------------------------------------------------------
    - Joueurs Triés par Score et Classement Général-
    Membre n°6: Brenn Nzimbi  est actuellement n°1 avec un score de 0
    Membre n°7: Alexia Laville  est actuellement n°2 avec un score de 0
    Membre n°4: Mary Gendre  est actuellement n°3 avec un score de 0
    Membre n°8: Corine Lafarge  est actuellement n°4 avec un score de 0
    Membre n°3: John Hamel  est actuellement n°5 avec un score de 0
    Membre n°2: Lionel Prudom  est actuellement n°6 avec un score de 0
    Membre n°1: Paul Lyons  est actuellement n°7 avec un score de 0
    Membre n°5: Sophia Gaillard  est actuellement n°8 avec un score de 0
    """

    """ /!!!\ Updates must be done in players_db table and seen in tournaments_db table in db file """
    # -- To update scores, DO NOT USE use the following var:
    # -- r = temp["tournaments_db"]["1"]["Tourn\u00e9es"]["Round"+str(i)].... [player score]; use this to view score only
    # -- INSTEAD use the following var:
    
    # -- p_score = temp["players_db"]["i"]["Score"] , 'i' is a player's index in the table

    # -- I gotta show up player index in matchups to allow user to allocate proper point to a specific player
    # -- And user input then shall be automatically seen in tournament_db table too
    # -- ex: Input Macth n°1 player1_name score: ...> player with 1st rating ...> use 'sorted_players_by_rating' to know pl ranking
    # -- ex: Input Macth n°1 player5_name score: ...> player with 5th rating ...> 
    # -- ex: Input Macth n°2 player2_name score: ...> player with 2nd rating ...> 
    # -- ex: Input Macth n°2 player6_name score: ...> player with 6th rating ...> 
    # -- ex: Input Macth n°3 player3_name score: ...> player with 3rd rating ...> 
    # -- ex: Input Macth n°3 player7_name score: ...> player with 7th rating ...> 
    # -- ex: Input Macth n°4 player4_name score: ...> player with 4th rating ...> 
    # -- ex: Input Macth n°4 player8_name score: ...> player with 8th rating ...> 
    
    # print("\n================== 🤓 Round1 🏁 Matchups 🥸 ================\n")
    # for i in range(len(rounds["Round1"])):
    #     print(f"Match n°{i+1}: {rounds['Round1'][i]}")

    """ /!!!\ 'all_players_db' must be sorted before saving it to db file"""
    # print(all_players_db) # -- all_players_db msut be sorted before saving it to db file
    
    # t= sorted_players_by_rating
    # d = slice(0,4)
    # e = slice(4,8)
    
    # c = t[d]
    # print(c)
    # print(c[0])
    # print(c[0][0]) # player name
    # print(c[0][1]) # player rating
    # print(c[0][2]) # player score
    # print(c[0][3]) # player index
    # print(t[d][0][3]) # player index

    """ Here's a solution """
    # -- t[d][0][3] must be used as in index in 'players_db["player index"]["Score"]'
    # -- Thus: players_db[str(t[d][0][3])]["Score"]
    # -- Then, the user shall input: 'players_db[str(t[d][0][3])]["Score"]: '


    # Unique match format = (["playerX_reference, playerX_scores"], ["playerY_reference, playerY_scores"])
    # which is: round1_matchups[i]

    # -- To start saving to DB file
    # save_initial_data()

    # print(all_players_db)

    # -- to get the names of tables in db:
    # for s in temp.keys():
    #     print(s[0:])

    # print(temp["players_db"].items())

    # -- to get indexes from t_players table separately:
    # for s in temp["players_db"].items():
    #     print(s[0])
    # or in temp list:
    # print(list(temp.items())[0][1].keys())


    # =======================
    """ -- UPDATING DB -- """

    # -- Get player's record:
    # print("\n--- before udate -- ")
    # print(temp["players_db"]["1"]['Nom de famille'])
    # print(temp["players_db"]["2"]['Nom de famille'])
    
    # # -- Open file to update them
    # with open(filename, "r") as f:
    #     temp = json.load(f) 
    #     temp["players_db"]["1"]['Nom de famille'] = "Renard"
    #     temp["players_db"]["2"]['Nom de famille'] = "Poisson"

    # # -- save update
    # with open(filename, "w") as f:
    #     json.dump(temp, f, indent=4)
    
    # -- print data updated 
    # print("\n--- after update -- ")
    # print(temp["players_db"]["1"]['Nom de famille'])
    # print(temp["players_db"]["2"]['Nom de famille'])

    # print("\n---")
    # print(temp["players_db"].items())
    # print("---\n")
    # for s in temp["players_db"].items():
    #     # print(s[1].values())
    #     print(s)
    #     print(s[1].keys())
    #     print(list(s[1].keys()))
    #     print(s[1]['Nom de famille']) # to update scores, i must change "s[1]['Nom de famille']" from dict "temp["players_db"].items()"
    # print("\n")
    # print(temp["players_db"].items()[1]['Nom de famille'])


    # =====================================
    # -- wtih pandas: BEST TABLE VIEW --- #
    # print("\n")
    # # df = pd.DataFrame.from_dict(temp["players_db"], orient='index')
    # print(df)
    # print("\n")

    # print("\n  -- Tableau des joueurs --")
    # print("-----------------------------")
    # # unsorted players data
    # df = pd.DataFrame.from_dict(temp["players_db"], orient='index')
    # print(df)
    # print("\n  - Tri des joueurs par points au 'Classement' général -")
    # print("---------------------------------------------------------")
    # # # sorting players data by rating
    # x = df.sort_values(by=['Classement'], ascending=False)
    # print(x)
    # print("\n")

    # # sorting data
    # print("\n-- Sorting Data by RATING--\n")
    # # x = df.sort_values(by=['Classement'], ascending=False)
    # print(x)
    # print("\n")

    # to sort players:
    # def pl_by_name(p):
    #     return p

    # def pl_by_rating(p):
    #     return p.rating

    # def pl_by_score(p):
    #     return sum(p.scores)

    # players_by_name = sorted(all_players_db, key=pl_by_name)
    # print(players_by_name)

    # from operator import attrgetter
    # s_players = sorted(all_players_db, key=attrgetter("Nom de famille"))


    # print("Voici la liste des joueurs enregistés:\n")
    # for p in all_players_db:
    #     print(p)
    # print("\n--\n")
    # print(all_players_db)

    # -- End of program - Goodbye message.
    # print("---------------------------------------------------------------------------")
    print("\n     ===================== 🌼🌼🌼 ===================")
    print("        Fin du programme 👀...  Merci et à bientôt!\n")

else:
    # view_unsorted_players_list()


    # -- 'generate_round1_matchups' must be on so that rounds instance can be used in tournament.py:
    generate_round1_matchups()
    
    # view_round1_matchups()