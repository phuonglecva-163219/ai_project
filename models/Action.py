class Action:
    def __init__(self, name, params, operator=None):
        self.name = name
        self.params = params
        self.operator = operator

    def export(self):
        result = {
            "name": self.name,
            "params": self.params
        }
        if self.operator is not None:
            result["operator"] = self.operator

        return result

if __name__ == "__main__":
    action = Action("ream", "ids")
    print(action.export())