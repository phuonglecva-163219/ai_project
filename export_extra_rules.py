import constant
import json
from collections import deque

rules = [
    # bad to play game
    {"conditions": {"all": [
        {"name": "game",
         "operator": constant.BAD,
         "value": "",
         },
    ]},
        "actions": [
        {"name": "ram",
         "params": {"values": [5], "operator":constant.LESS_THAN},
         },
        {"name": "screen",
         "params": {"values": [5.01], "operator":constant.LESS_THAN},
         },
        {"name": "battery",
         "params": {"values": [3005], "operator":constant.LESS_THAN},
         },
    ],
    },
    # medium to  play game
    {"conditions": {"all": [
        {"name": "game",
         "operator": constant.MEDIUM,
         "value": "",
         },
    ]},
        "actions": [
        {"name": "ram",
         "params": {"values": [5, 10]},
         "operator":constant.BETWEEN
         },
        {"name": "screen",
         "params": {"values": [5.01, 6.51]},
         "operator":constant.BETWEEN
         },
        {"name": "battery",
         "params": {"values": [3005, 4005]},
         "operator":constant.BETWEEN
         }
    ],
    },
    # good to play game
    {"conditions": {"all": [
        {"name": "game",
         "operator": constant.GOOD,
         "value": "",
         },
    ]},
        "actions": [
        {"name": "ram",
         "params": {"values": [10]}, "operator":constant.GREATER_THAN
         },
        {"name": "screen",
         "params": {"values": [6.51]}, "operator":constant.GREATER_THAN
         },
        {"name": "pin",
         "params": {"values": [4005]}, "operator":constant.GREATER_THAN
         }
    ],
    },
    # good for student
    {"conditions": {"all": [
        {"name": "student",
         "operator": constant.GOOD,
         "value": "",
         },
    ]},
        "actions": [
        {"name": "ram",
         "params": {"values": [5, 10]}, "operator":constant.BETWEEN
         },
        {"name": "price",
         "params": {"values": [10.1]}, "operator":constant.LESS_THAN
         },
        {"name": "rom",
         "params": {"values": [32.1, 64.1]}, "operator":constant.BETWEEN
         }
    ],
    },
]
with open("extra-rules.json", "w") as out:
    out.write(json.dumps(rules, indent=2))


# def findRulesFromCondition(condition, rules):
#     name = condition.split(" ")[0]
#     operator = condition.split(" ")[1]
#     value = condition.split(" ")[2]
#     value = value if value == "" else float(value)

#     for rule in rules:
#         rule_conditions = rule.get("conditions").get("all")
#         for condi in rule_conditions:
#             if condi["name"] == name and condi["operator"] == operator and condi["value"] == value:
#                 return rule


# start_condition = "game {} {}".format(constant.BAD, "")
# result = []
# conditions = deque()
# conditions.append(start_condition)

# while len(conditions) > 0:
#     condition = conditions.pop()
#     print(condition)
#     rule = findRulesFromCondition(condition, root)
#     print(rule)
#     actions = rule.get("actions")
#     for action in actions:
#         if action.get("name") == "export_telephones":
#             result.append(action.get("params").get("ids"))
#         else:
#             if len(action["params"]["values"]) == 2:
#                 values = action["params"]["values"]
#                 conditions.append("{} {} {} {} {}".format(
#                     action["name"],
#                     constant.GREATER_THAN,
#                     values[0],
#                     constant.LESS_THAN,
#                     values[1]
#                 ))
#             else:
#                 conditions.append("{} {} {}".format(
#                     action["name"],
#                     action["operator"],
#                     action["params"]["values"][0]
#                 ))
#                 # print(action["name"])
#                 # print(rule)
                
#                 # print(rule)

# def combinationImageList(listId):
#     if len(listId) == 1:
#         return listId
#     else:
#         result = []
#         for i in range(1, len(listId)):
            
# print(result)