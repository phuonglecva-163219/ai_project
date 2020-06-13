import json
from PIL import Image
import constant
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
# input = "{} {} {}"
#  run(input) return listImageId. /images_1/id.jpg
#
import sys
# with open("rules_2.json", "r") as input_rule:
#     root = json.load(input_rule)
# with open("extra-rules.json", "r") as extra_input:
#     extra_rules = json.load(extra_input)
with open("data.json", "r", encoding="utf-8") as input_fact:
    facts = json.load(input_fact)
with open("test.json", "r") as rule_input:
    root = json.load(rule_input)
# for rule in extra_rules:
#     root.append(rule)
# with open("test.json", "w") as out:
#     out.write(json.dumps(root, indent=2))

input_condition = "battery {} {}".format(constant.LESS_THAN, 3005)
input_condition = {
    "name": input_condition.split(" ")[0],
    "operator": input_condition.split(" ")[1],
    "value": int(input_condition.split(" ")[2]),
}


def isEqual(obj1, obj2):
    return obj1["name"] == obj2["name"] and obj1["operator"] == obj2["operator"] and obj1["value"] == obj2["value"]


def getNameAndParams(rule):
    name, params = rule.get("actions")[0].get(
        "name"), rule.get("actions")[0].get("params")
    return (name, params)


def getListImage(list_id):
    return [image for (id, image) in enumerate(facts)
            if id in list_id]


def showListImage(listImage):
    rows = len(listImage) // 2
    cols = len(listImage)//rows + 1
    fig = plt.figure(figsize=(20, 10))
    plt.axis('off')
    plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off',
                    labelleft='off', labeltop='off', labelright='off', labelbottom='off')

    for (index, id) in enumerate(listImage):
        img = Image.open("images_1/{}.jpg".format(id))
        index = index + 1
        ax = fig.add_subplot(rows, cols, index)
        plt.imshow(np.asarray(img))
    plt.show()


def getListConditions(rule):
    return rule.get("conditions").get("all")


def getListActions(rule):
    return rule.get("actions")


def findRulesFromCondition(condition, rules):
    for rule in rules:
        if getListConditions(rule) == condition:
            return rule

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

# print(result)
# init_condition = "{} {} {}".format("ram", constant.LESS_THAN, 5)
# init_rule = findRulesFromCondition(init_condition, root)
# print(init_rule)


# init_condition = "{} {} {} {} {}".format(
#     "ram",
#     constant.GREATER_THAN,
#     5,
#     constant.LESS_THAN,
#     10
# )


def tranform2conditions(conditionStr):
    listParams = conditionStr.split(" ")
    result = []
    if len(listParams) == 3:

        value = listParams[2] if listParams[2] == "" else float(listParams[2])
        result.append({
            "name": listParams[0],
            "operator": listParams[1],
            "value": value
        })
    else:
        result.append({
            "name": listParams[0],
            "operator": listParams[1],
            "value": float(listParams[2])
        })
        result.append({
            "name": listParams[0],
            "operator": listParams[3],
            "value": float(listParams[4])
        })
    return result


conditionInput = "game good "
conditions = tranform2conditions(conditionInput)
# print(conditions)
# listCondition = [{
#     "name": "game",
#     "operator": constant.GOOD,
#     "value": "",
# }]
# print(root)

# print(findRulesFromCondition(conditions,root))


def run(init_condition):
    stack = deque()
    start_condition = tranform2conditions(init_condition)
    start_rule = findRulesFromCondition(start_condition, root)
    stack.append(start_rule)
    result = []
    while len(stack) > 0:
        currRule = stack.pop()
        currActions = getListActions(currRule)
        # currActions = currRule.get("actions")
        if len(currActions) > 1:
            for action in currActions:
                if action.get("operator") == constant.BETWEEN:
                    cond = tranform2conditions("{} {} {} {} {}".format(
                        action.get("name"),
                        constant.GREATER_THAN,
                        action.get("params").get("values")[0],
                        constant.LESS_THAN,
                        action.get("params").get("values")[1]
                    ))
                    stack.append(findRulesFromCondition(cond, root))
                else:
                    cond = tranform2conditions("{} {} {}".format(
                        action.get("name"),
                        action.get("operator"),
                        action.get("params").get("values")[0]
                    ))
                    stack.append(findRulesFromCondition(cond, root))
        elif currActions[0].get("name") == "export_telephones":
            result.append(currActions[0].get("params").get("ids"))
    list_inter = set.intersection(*[set(x) for x in result])
    return list(list_inter)


listId = run("ram {} {}".format(
    constant.LESS_THAN,
    5
))
# listImage = [tele for (index, tele) in enumerate(facts) if index in listId]
# print(listImage)


def runAll(listCondition):
    listResult = []
    for condition in listCondition:
        listResult.append(
            run(condition)
        )
    list_inter = set.intersection(*[set(x) for x in listResult])
    return list(list_inter)


# conditions = ["ram {} {}".format(
#     constant.LESS_THAN, 5), "rom {} {}".format(constant.GREATER_THAN, 64.1)]
# print(listImg)

# condition = ["ram {} {}".format(constant.LESS_THAN, 5)]
# listImg = runAll(condition)
# print(listImg)

def getData(index):
    with open("data.json", "r", encoding="utf-8") as input_fact:
        facts = json.load(input_fact)
    return facts[index]

listCondition = ["game good "]
listId = runAll(listCondition)
print(listId)