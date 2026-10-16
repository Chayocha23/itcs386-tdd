import pytest
from bank import BankAccount, InsufficientFunds

#Step 0.5: Fixtures for fresh test data 
@pytest.fixture
def account():
    return BankAccount("alice", balance=100)

# --- 3 Sample Tests from the Lab ---
def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150

def test_withdraw_more_than_balance_is_refused(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(500)
    assert account.balance == 100

def test_each_test_gets_a_fresh_account(account):
    assert account.balance == 100

# ---3 tests that the requirements specify to add ---
# 1. A deposit of 0 is refused with ValueError
def test_deposit_zero_is_refused(account):
    with pytest.raises(ValueError, match="deposit must be positive"):
        account.deposit(0)

# 2. Withdrawing the whole balance leaves exactly 0
def test_withdraw_whole_balance(account):
    account.withdraw(100)
    assert account.balance == 0

# 3. Two withdrawals in a row both reduce the balance
def test_two_withdrawals_in_a_row(account):
    account.withdraw(30)
    account.withdraw(20)
    assert account.balance == 50
    
#Step 0.6: Comparing decimals
def test_interest(account):
    account.add_interest(0.10)
    assert account.balance == pytest.approx(110)