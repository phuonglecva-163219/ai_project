import json
import constant

with open("comments.json","r", encoding="utf-8") as input:
    telephones = json.load(input)

def getTelephoneByKey(key, data):
    return [ telephone[key] for (id, telephone) in enumerate(data)]

variables = ["ram", "rom", "screen", "main_camera", "extra_camera", "batery", "price"]

rules = [
# RAM=========================
# if ram < 5
{ "conditions": { "all": [
      { "name": "ram",
        "operator": constant.LESS_THAN,
        "value": 5,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
# if ram > 5 and ram < 10
{ "conditions": { "all": [
      { "name": "ram",
        "operator": constant.GREATER_THAN,
        "value": 5,
      },
      { "name": "ram",
        "operator": constant.LESS_THAN,
        "value": 10,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
# if ram > 10
{ "conditions": { "all": [
      { "name": "ram",
        "operator": constant.GREATER_THAN,
        "value": 10,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},

# Screen ==================================================

# if screen < 5
{ "conditions": { "all": [
      { "name": "screen",
        "operator": constant.LESS_THAN,
        "value": 5.01,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
# if screen > 5 and screen < 10
{ "conditions": { "all": [
      { "name": "screen",
        "operator": constant.GREATER_THAN,
        "value": 5.01,
      },
      { "name": "screen",
        "operator": constant.LESS_THAN,
        "value": 6.51,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
# if screen > 10
{ "conditions": { "all": [
      { "name": "screen",
        "operator": constant.GREATER_THAN,
        "value": 6.51,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
# main_camera ==================================================

# if main_camera < 5
{ "conditions": { "all": [
      { "name": "main_camera",
        "operator": constant.LESS_THAN,
        "value": 40.5,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
# if main_camera > 5 and main_camera < 10
{ "conditions": { "all": [
      { "name": "main_camera",
        "operator": constant.GREATER_THAN,
        "value":40.5,
      },
      { "name": "main_camera",
        "operator": constant.LESS_THAN,
        "value": 80,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
# if main_camera > 10
{ "conditions": { "all": [
      { "name": "main_camera",
        "operator": constant.GREATER_THAN,
        "value": 80,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
# extra_camera ==================================================

# if main_camera < 5
{ "conditions": { "all": [
      { "name": "extra_camera",
        "operator": constant.LESS_THAN,
        "value": 30,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},

# if main_camera > 10
{ "conditions": { "all": [
      { "name": "extra_camera",
        "operator": constant.GREATER_THAN,
        "value": 30,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
# batery ==================================================

# if main_camera < 5
{ "conditions": { "all": [
      { "name": "batery",
        "operator": constant.LESS_THAN,
        "value": 3005,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
{ "conditions": { "all": [
      { "name": "batery",
        "operator": constant.GREATER_THAN,
        "value": 3005,
      },
      { "name": "batery",
        "operator": constant.LESS_THAN,
        "value": 4005,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},

# if main_camera > 10
{ "conditions": { "all": [
      { "name": "batery",
        "operator": constant.GREATER_THAN,
        "value": 4005,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
# price ==================================================

# if main_camera < 5
{ "conditions": { "all": [
      { "name": "price",
        "operator": constant.LESS_THAN,
        "value": 10.1,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
{ "conditions": { "all": [
      { "name": "price",
        "operator": constant.GREATER_THAN,
        "value": 10.1,
      },
      { "name": "price",
        "operator": constant.LESS_THAN,
        "value": 20.1,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
{ "conditions": { "all": [
      { "name": "price",
        "operator": constant.GREATER_THAN,
        "value": 20.1,
      },
      { "name": "price",
        "operator": constant.LESS_THAN,
        "value": 30.1,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},

# if main_camera > 10
{ "conditions": { "all": [
      { "name": "price",
        "operator": constant.GREATER_THAN,
        "value": 30.1,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
# ROM condition:
# if main_camera < 5
{ "conditions": { "all": [
      { "name": "rom",
        "operator": constant.LESS_THAN,
        "value": 32.1,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
{ "conditions": { "all": [
      { "name": "rom",
        "operator": constant.GREATER_THAN,
        "value": 32.1,
      },
      { "name": "rom",
        "operator": constant.LESS_THAN,
        "value": 64.1,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},

# if main_camera > 10
{ "conditions": { "all": [
      { "name": "rom",
        "operator": constant.GREATER_THAN,
        "value": 64.1,
      },
  ]},
  "actions": [
      { "name": "export_telephones",
        "params": {"ids": []},
      },
  ],
},
]


def getRulesByVariable(rules, variable):
    arr = []
    for rule in rules:
        if rule["conditions"]["all"][0]["name"] == variable:
            arr.append(rule)
    return arr


rams = getTelephoneByKey("ram", telephones)
rams = [int(ram.strip().split(" ")[0]) for ram in rams]

screens = getTelephoneByKey("screen", telephones)
screens_new = []
for screen in screens:
    try:
        screens_new.append(float(screen.strip().split('\"')[0]))
    except:
        screens_new.append(
            float(screen.strip().split('\"')[0].split(" ")[1])
        )

cameras = getTelephoneByKey("camera", telephones)

result = []
for (id, camera) in enumerate(cameras):
    camera = str(camera).strip()
   
    if "camera" in camera:
        result.append([24, 12])
    elif len(camera.split(" ")) == 2:
     
        result.append([int(camera.split(" ")[0]), 0])
    else:
    
        extr = camera.split(" ")[5]
        try:
            extr = float(extr)
        except:
            extr = 0
        result.append([
            float(camera.split(" ")[1]),
            extr
        ])

main_camera = [camera[0] for camera in result]
extra_camera = [camera[1] for camera in result]

bateries = getTelephoneByKey("pin", telephones)
bateries = [int(bate.strip().split(" ")[0]) for bate in bateries]
prices = getTelephoneByKey("price", telephones)

roms = getTelephoneByKey("rom", telephones)
roms = [ int(rom.strip().split(" ")[0]) for  rom in roms]
print(roms)
for i in range(len(prices)):
    price = str(prices[i])
    if len(price.split(".")) < 3:
        price = "0.{}".format(price[0])
        prices[i] = float(price)
    else:
        price = "{}.{}".format(price.split(".")[0], price.split(".")[1][0])
        prices[i] = float(price)

list_variable_data = {
   "ram":rams, 
   "screen":screens_new, 
   "main_camera":main_camera, 
   "extra_camera":extra_camera, 
   "batery":bateries, 
   "price":prices,
   "rom":roms
}


new_rules = []
for variable in variables:
    list_rules = getRulesByVariable(rules, variable)
    for rule in list_rules:
        conditions = rule["conditions"]
        actions = rule["actions"]
        
        if len(conditions["all"]) == 1:
            condition = conditions["all"][0]
            data = list_variable_data[variable]
            if condition["operator"] == constant.LESS_THAN:
                actions[0]["params"]["ids"] = [
                    id for (id, val) in enumerate(data)  if  val < condition["value"]
                ]
            if condition["operator"] == constant.GREATER_THAN:
                actions[0]["params"]["ids"] = [
                    id for (id, val) in enumerate(data)  if  val > condition["value"]
                ]
        else:
            low = conditions["all"][0]["value"]
            high = conditions["all"][1]["value"]
            actions[0]["params"]["ids"] = [
                    id for (id, val) in enumerate(data)  if  val > low and  val < high
                ]
    for rule in list_rules:
      new_rules.append(rule)

print(new_rules)

with open("rules_2.json", "w") as output:
    output.write(json.dumps(new_rules, indent=2))