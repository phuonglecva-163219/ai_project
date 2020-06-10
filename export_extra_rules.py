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
         "params": {"values": [5], "operator":constant.LESS_THAN},
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
         },
        {"name": "screen",
         "params": {"values": [5, 10]},
         },
        {"name": "battery",
         "params": {"values": [3005, 4005]},
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
         "params": {"values": [10]}, "operator":constant.GREATER_THAN
         },
        {"name": "pin",
         "params": {"values": [4005]}, "operator":constant.GREATER_THAN
         }
    ],
    },
]

with open("rules_1.json", "r") as input:
    root = json.load(input)

# input_condition = "game good"
# name = input_condition.split(" ")[0]
# operator = input_condition.split(" ")[1]


# def getActionsNext(rules, condition):
#     name = condition.split(" ")[0]
#     operator = condition.split(" ")[1]
#     print(name, operator)
#     for rule in rules:
#         if rule.get("conditions").get("all")[0].get("name") == name and rule.get("conditions").get("all")[0].get("operator") == operator:
#             return rule.get("actions")


# actions = getActionsNext(rules, input_condition)
# listId = []


# print(findRulesFromCondition("ram {} {}".format(constant.LESS_THAN, 5), root))

# # extra_rules = json.dumps(rules)

# for extra in extra_rules:
#     print(extra)
# json_extra_rules = []
# json_extra_rules.append({

# })

# # print(root)
with open("extra-rules.json", "r") as input:
    data = json.load(input)

for i in data:
    root.append(i)
# print(root)

def findRulesFromCondition(condition, rules):
    name = condition.split(" ")[0]
    operator = condition.split(" ")[1]
    value = condition.split(" ")[2]
    value = value if value == "" else float(value)

    for rule in rules:
        rule_conditions = rule.get("conditions").get("all")
        for condi in rule_conditions:
            if condi["name"] == name and condi["operator"] == operator and condi["value"] == value:
                return rule
# print(root)



start_condition = "game {} {}".format(constant.BAD, "")
result = []
conditions = deque()
conditions.append(start_condition)

while len(conditions) > 0:
    condition = conditions.pop()
    print(condition)
    rule = findRulesFromCondition(condition, root)
    print(rule)
    actions = rule.get("actions")
    for action in actions:
        if action.get("name") == "export_telephones":
            result.append(action.get("params").get("ids"))
        else:
            if len(action["params"]["values"]) == 2:
                values = action["params"]["values"]
                conditions.append("{} {} {} {} {}".format(
                    action["name"],
                    constant.GREATER_THAN,
                    values[0],
                    constant.LESS_THAN,
                    values[1]
                ))
            else:
                conditions.append("{} {} {}".format(
                    action["name"],
                    action["operator"],
                    action["params"]["values"][0]
                ))
                # print(action["name"])
                # print(rule)
                
                # print(rule)

print(result)