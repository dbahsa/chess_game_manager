#! /user/bin/env python3
# -*- coding: utf-8 -*-

import json

# |- program:
# |—— controller.py (cls: menu)
# |—— model.py (cls: challengers + tournt + db + menu)
# |—— view.py (view func)
# |—— db.json

'''
### --- SAVE DATA INTO A DB FILE --###
## 1st create the data variable, here it's 'temp':
temp = {}
"""temp['challengers_table'] = {}
temp['tournaments_table'] = {}"""

## 2nd. create a json file: ONE WAY
json_string = json.dumps(temp, indent=4)
with open('t_db.json', 'w') as f:
    f.write(json_string)

## 2nd.bis. create a json file: ANOTHER WAY /!\
with open('t_db.json', "w") as f:
    json.dump(temp, f, indent=4)


### --- READ DATA FROM A DB FILE --###
## 1. open the json file: ONE WAY  /!\
with open('t_db.json', 'r') as f:
    json_object = json.loads(f.read())

## 1.bis open the json file: ANOTHER WAY
with open('t_db.json', "r") as f:
    json_object = json.load(f)
'''

"""
## -- Possible Matchups -- To check if challengers have already played against each another !!! --
## 1. Create a function to be initiated once all players have been created... or it can be done before... 'px' is a player index, 'x' is its number

challengers=['p1','p2','p3','p4','p5','p6','p7','p8']
# challengers = sorted_challengers_by_rankings
matches=[]
challenger1=0
while challenger1<len(challengers):
    challenger2=challenger1+1    # start
    while challenger2<len(challengers):
        matches.append((challengers[challenger1],challengers[challenger2]))
        challenger2+=1
    challenger1+=1

print("\n--- ___ ---")
print(f"\nThere is a total of '{len(matches)}' matches:\n")
for m in matches:
    print(m)

print()
"""

import itertools

## to find different unique games in tournament
challengers=['p1','p2','p3','p4','p5','p6','p7','p8']

c = itertools.combinations(challengers, 2)
# p = itertools.permutations(challengers, 2)

num_max_games = []

# print()
for s in c:
    num_max_games.append(s)
    print(s)
print("---")


a = challengers
b = slice(0,8,2)
x = slice(1,8,2)
z = zip(a[b],a[x])

a1 = challengers
x1 = slice(0,4)
y1 = slice(4,8)
w = zip(a1[x1],a1[y1])

m1=[]
for r in z:
    m1.append(r)
    print(r)
print()
print(m1)
print("---")

m2=[]
for j in w:
    m2.append(j)
    print(j)
print()
print(m2)
print("---")


## to check if the game is already in the 28 games list:
for item in num_max_games:
    if item not in m1 and item not in m2:
        print(item)

# for item in num_max_games:
#     if item != ('p1', 'p2'):
#         print(item)


