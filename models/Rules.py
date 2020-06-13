from Condition import Condition
from Action import Action
import json

class Rule:
    def __init__(self, conditions, actions):
        self.conditions = conditions
        self.actions = actions

    def export_rule(self):
        return {
            "conditions": {
                "all": self.conditions,
            },
            "actions": self.actions
        }


if __name__ == "__main__":
    actionList = []
    conditionList = []
    # Set conditions:
    conditionList.append(
        Condition("student", "good", "").export()
    )
    # Set Actions:
    actionList.append(
        Action("ram", {
            "values": [5, 10]
        }, "between"
        ).export()
    )
    actionList.append(
        Action("price", {
            "values": [10.1]
        }, "less_than"
        ).export()
    )
    actionList.append(
        Action("rom", {
            "values": [32.1, 64.1]
        }, "between"
        ).export()
    )
    rule = Rule(conditionList, actionList)
    # print(rule.export_rule())
    # with open("demo.json", "w") as jsonOut:
    #     jsonOut.write(json.dumps(rule.export_rule(), indent=2))
    with open("test.json", "r") as input:
        data = json.load(input)
    data.append(rule.export_rule())
    print(data)
    
    with open("test2.json", "w") as output:
        output.write(json.dumps(data,indent=2))