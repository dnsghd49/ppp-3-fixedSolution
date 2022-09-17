class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"

# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2
        return print(self.max_speed)

# Define another class that inherits Podracer and call this one SebulbasPod.
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"
        return other.condition


modelS = AnakinsPod(140, "perfect", 100000)
plaid = SebulbasPod(200, "perfect", 130000)

print(modelS.max_speed)
print(modelS.price)
print(modelS.condition)

modelS.boost()

print(plaid.flame_jet(plaid))
