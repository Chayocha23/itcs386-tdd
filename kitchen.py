# Step A1: The first failing test
# kitchen.py
## Before Editing (Red)
# class Quantity:
#     def __init__(self, amount):
#         self.amount = amount

#     def times(self, multiplier):
#         self.amount = 600

## After Editing (Green)
# kitchen.py
# kitchen.py
class Quantity:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Quantity(self.amount * multiplier)