from Expense_Tracker import funds, balance_warning
import builtins
from unittest import mock
import pytest



def test_expense_init():
    """ Test the __init__() method of the ExpenseTracker class."""
    tracker = Tracker()
    assert tracker.balance == 0
    assert tracker.deduction == 0
    
def test_expense_funds(capsys):
    """ Test the funds() method of the ExpenseTracker class and makes
    sure that the user is inputting an integer value"""
    with mock.patch("builtin.input",
                    side_effects = ["one, -1, 1"]):
        x=funds()
        assert x== "Amount of funds available 1"
        captured = capsys.readouterr()
        assert captured.out == (
            "please enter int value.\n"
            "Enter a number greater than 0.\n"
        )
def test_subtractions():
    """ Test the subtractions() method of the ExpenseTracker class and 
    makes sure that the ouput is calculated correctly"""
    assert s (500,100)== 400
    assert s (1000,200)== 800
    assert s (700,500) == 200

def test_balance_warning(expected):
    assert balance_warning() == expected

def test_overdraw_amount():
    if self.amount >0:
         print(f"Amount left in your account: ${self.amount}")
    elif self.amount =0:
        print("Zero balance")
        print(f"Amount left in your account: ${self.amount}"))
    elif self.amount<0:
        print("Not enough left in balance")
        print(f"Amount left in your account: ${self.amount}")
    
    