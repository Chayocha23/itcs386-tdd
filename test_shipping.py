import pytest
from shipping import shipping_fee

#Step 0.8: Bug hunt checkpoint
# Rule 1: The weight must be more than 0 kg. Otherwise raise ValueError.
def test_rule_1_zero_weight_raises_error():
    with pytest.raises(ValueError, match="weight must be more than 0 kg"):
        shipping_fee(0)

def test_rule_1_negative_weight_raises_error():
    with pytest.raises(ValueError, match="weight must be more than 0 kg"):
        shipping_fee(-1)

# Tests for Rules 2, 3, and 4
@pytest.mark.parametrize("weight, expected_fee", [
    (0.5, 40),  # Rule 2: up to 1 kg
    (1.0, 40),  # Rule 2: boundary at exactly 1 kg (breaks Rule 2 in buggy code)
    (1.5, 60),  # Rule 3: more than 1 kg and up to 5 kg
    (5.0, 60),  # Rule 3: boundary at exactly 5 kg
    (5.2, 70),  # Rule 4: started kilogram above 5 kg (breaks Rule 4 in buggy code)
    (6.0, 70),  # Rule 4: exactly 1 kg above 5 kg
    (6.1, 80),  # Rule 4: started 2nd kilogram above 5 kg
])
def test_shipping_fee_rules(weight, expected_fee):
    assert shipping_fee(weight) == expected_fee