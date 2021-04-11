import json

dictcards={
    0:{
    "name":"Randy Ortan",
    "Age":40,
    "Sex":"M",
    "Strength":872.05,
    "Speed":870.85,
    "Damage":873.02,
    "Respect":869.40,
    "img":"res\\images\\cards\\wrestlers\\ro.png",
    "stackimg":"res\\images\\cards\\stackwrestlers\\stackro.png"
       },
    1:{
    "name":"John Cena",
    "Age":43,
    "Sex":"M",
    "Strength":883.95,
    "Speed":873.26,
    "Damage":865.32,
    "Respect":877.46,
    "img":"res\\images\\cards\\wrestlers\\jc.png",
    "stackimg":"res\\images\\cards\\stackwrestlers\\stackjc.png"
       },
    2:{
    "name":"Great Khali",
    "Age":47,
    "Sex":"M",
    "Strength":876.54,
    "Speed":843.26,
    "Damage":883.56,
    "Respect":866.96,
    "img":"res\\images\\cards\\wrestlers\\gk.png",
    "stackimg":"res\\images\\cards\\stackwrestlers\\stackgk.png"
       },
    3:{
    "name":"Roman reigns",
    "Age":35,
    "Sex":"M",
    "Strength":874.53,
    "Speed":873.50,
    "Damage":870.91,
    "Respect":871.94,
    "img":"res\\images\\cards\\wrestlers\\rr.png",
    "stackimg":"res\\images\\cards\\stackwrestlers\\stackrr.png"
       },
    4:{
    "name":"Batista",
    "Age":51,
    "Sex":"M",
    "Strength":879.49,
    "Speed":878.84,
    "Damage":877.75,
    "Respect":877.94,
    "img":"res\\images\\cards\\wrestlers\\bt.png",
    "stackimg":"res\\images\\cards\\stackwrestlers\\stackbt.png"
       },
    5:{
    "name":"Reymisterio",
    "Age":45,
    "Sex":"M",
    "Strength":867.45,
    "Speed":869.04,
    "Damage":873.42,
    "Respect":871.76,
    "img":"res\\images\\cards\\wrestlers\\rm.png",
    "stackimg":"res\\images\\cards\\stackwrestlers\\stackrm.png"
       },
    6:{
    "name":"Hulk hogan",
    "Age":66,
    "Sex":"M",
    "Strength":857.39,
    "Speed":874.68,
    "Damage":823.79,
    "Respect":863.85,
    "img":"res\\images\\cards\\wrestlers\\hh.png",
    "stackimg":"res\\images\\cards\\stackwrestlers\\stackhh.png",
       },
    7:{
    "name":"Undertaker",
    "Age":55,
    "Sex":"M",
    "Strength":874.83,
    "Speed":875.74,
    "Damage":869.83,
    "Respect":870.49,
    "img":"res\\images\\cards\\wrestlers\\ut.png",
    "stackimg":"res\\images\\cards\\stackwrestlers\\stackut.png",
       },

    

    }

with open('WrestlerData.json','w') as f:
    j=json.dumps(dictcards)
    f.write(j)
    f.close()
