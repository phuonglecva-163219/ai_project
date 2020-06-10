import json
from PIL import Image
import constant
import matplotlib.pyplot as plt
import numpy as np

import sys
with open("rules_1.json", "r") as input_rule:
    rules = json.load(input_rule)
with open("comments.json", "r", encoding="utf-8") as input_fact:
    facts = json.load(input_fact)

try:
    img_0 = Image.open("images_1/{}.jpg".format(0))
except IOError:
    print("Unable to load image")
    sys.exit(1)

input_condition = "battery {} {}".format(constant.LESS_THAN, 3005)
input_condition = {
    "name": input_condition.split(" ")[0],
    "operator": input_condition.split(" ")[1],
    "value": int(input_condition.split(" ")[2]),
}

def isEqual(obj1, obj2):
    return obj1["name"] == obj2["name"] and obj1["operator"] == obj2["operator"] and obj1["value"] == obj2["value"]
        
def getNameAndParams(rule):
    name, params = rule.get("actions")[0].get("name"), rule.get("actions")[0].get("params")
    return (name, params)

def getListImage(list_id):
    return [image for (id, image) in enumerate(facts)
                    if id in list_id]
def showListImage(listImage):
    # w, h = 10, 10
    # print(len(listImage))
    rows = len(listImage) // 2
    cols = len(listImage)//rows + 1
    # print(rows, cols)
    fig=plt.figure(figsize=(20, 10))
    plt.axis('off')
    plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')

    for (index, id) in enumerate(listImage):
        # print(index)
        img = Image.open("images_1/{}.jpg".format(id))
        index = index + 1
        ax = fig.add_subplot(rows, cols, index)
        plt.imshow(np.asarray(img))
    plt.show()


def run(condition):
    for rule in rules:
        for condi in rule.get("conditions").get("all"):
            if condi == input_condition:
                list_id = getNameAndParams(rule)[1].get("ids")
                showListImage(list_id)
                return  list_id

run(input_condition)