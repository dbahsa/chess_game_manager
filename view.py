#!/user/bin/env python3
# -*- coding: utf-8 -*-


# |- program:
# |—— controller.py (main + menu)
# |—— model.py (pl + tournt + db + menu)
# |—— view.py (view funcs)
# |—— db.json



# |- 🌼 Next Steps 🌼:
# |—— save tournaments info to db files --#
# |—— instantiate players obj --#
# |—— /!!!\ Put a link of 'players data' from 'players table' inside 'tournament table'
# |—— 
# |—— save players info to players_db table --#
# |—— Save in tournaments_db table, players indexes from players_db
# |—— get "sorted" players info (name+rating+score) from db to instantiate 1st matchups --#
# |—— save 1st matchups to db in tournaments_db table --#
# |—— View Matchups from tournaments_db table --#
# |—— Input Round1 score in players_db table --#
# |—— Save Round1 score in players_db table --#
# |—— View players_db table if Round1 Scores are recorded --#
# |—— Save Round1 score in tournaments_db table 
# |—— View tournaments_db table if Round1 Scores are recorded in there too

# |—— 
# |—— 
# |—— 
# |—— get "sorted" players info based num of scores & rating
# |—— instantiate round2
# |—— save round2
# |—— get round2 to input round2 scores
# |—— save round2 scores
# |—— get 'sorted' players info based num of scores & rating
# |—— instantiate round3
# |—— save round3
# |—— get round3 to input round3 scores
# |—— save round3
# |—— etc
# |—— 
# |—— 
# 🚨 In each step, always show the user its own input, and ask to pursue or to reset

"""
while True:
    try:
        add_score = float(input("Taper le nouveau score du joueur: ").replace(",", "."))
        if add_score in [0, 0.5, 1]:
            print(F"Vous avez saisi: {add_score}")
        else:
            print("Merci de choisir [0], [0.5] ou [1]")
            continue
    except:
        print("Erreur de saisie...")
        # continue
    else:
        break
"""

"""a = range(4)
print(len(a))
i = int(input("saisir un chiffre: "))
if i < len(a):
    print(i+1)"""

list = [1,2,3,4,5,6,7,8]
print(list[0::2])
print(list[1::2])
