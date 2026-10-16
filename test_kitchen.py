# test_kitchen.py
"""
Test List:
- [ ] 200 g * 3 = 600 g
- [ ] multiplying a quantity does not modify the original
- [ ] two quantities with the same amount and unit are equal
- [ ] 1 oz is not the same as 1 g
- [ ] 200 g + 300 g = 500 g
- [ ] 200 g + 1 oz, reduced to grams, using a conversion rate
- [ ] (200 g + 1 oz) * 2
"""
#Step A1: The first failing test
from kitchen import Quantity

def test_multiplication():
    flour = Quantity(200)
    assert flour.times(3) == Quantity(600)

#Step A2: Triangulating to the real formula    
# def test_multiplication_by_two():
#     flour = Quantity(200)
#     flour.times(2)
#     assert flour.amount == 400
    
#Step A3: A quantity that does not change under you
def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)
    assert flour.times(3) == Quantity(600)
    assert flour.times(2) == Quantity(400)
    
#Step A4: Equality
def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)
    
#Step A5: A second unit
def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")