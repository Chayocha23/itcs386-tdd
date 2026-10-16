# Step A1: The first failing test (Green)
# kitchen.py
class Quantity:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount = 600
