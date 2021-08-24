#! /user/bin/env python3
# -*- coding: utf-8 -*-

import json

# |- program:
# |—— controller.py (cls: menu)
# |—— model.py (cls: pl + tournt + db + menu)
# |—— view.py (view func)
# |—— db.json


### --- SAVE DATA INTO A DB FILE --###
## 1st create the data variable, here it's 'temp':
temp = {}
"""temp['players_table'] = {}
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
    