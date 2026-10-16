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
class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"
    
class Sum:
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend


class Converter:
    def reduce(self, source, to_unit):
        return grams(500)

def grams(amount):
    return Quantity(amount, "g")

def ounces(amount):
    return Quantity(amount, "oz")