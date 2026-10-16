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
    def __init__(self):
        self.rates = {}

    def add_rate(self, from_unit, to_unit, rate):
        self.rates[(from_unit, to_unit)] = rate

    def rate(self, from_unit, to_unit):
        if from_unit == to_unit:
            return 1
        return self.rates[(from_unit, to_unit)]

    def reduce(self, source, to_unit):
        augend_in_target = source.augend.amount * self.rate(source.augend.unit, to_unit)
        addend_in_target = source.addend.amount * self.rate(source.addend.unit, to_unit)
        return Quantity(augend_in_target + addend_in_target, to_unit)

def grams(amount):
    return Quantity(amount, "g")

def ounces(amount):
    return Quantity(amount, "oz")