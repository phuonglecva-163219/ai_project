
class Condition:
    def __init__(self, name, operator, value):
        self.name = name
        self.operator = operator
        self.value = value
    
    def export(self):
        return {
            "name":self.name,
            "operator":self.operator,
            "value":self.value,
        }

if __name__ == "__main__":
    condition = Condition("ram", "less_than", 5)
    print(condition.export())