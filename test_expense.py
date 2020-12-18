from Expense_Tracker import ExpenseTracker
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
        x=funds(self)
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
    
    
    
def test_categorize_shopping():
    """ Will test the categorize_shopping method of the ExpenseTracker class
    & ensure that the user is entering proper credentials for who/what to 
    shop for.
    """
    while True:
        try:
            num = ()
            if not 0 <= num <= 2:
                print("You entered an invalid number. Try again. ")
                continue
        except ValueError:
            print("Not a proper int value")
    
    assert ExpenseTracker == self.person
    assert ExpenseTracker == self.item
   
    
    