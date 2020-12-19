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
def test_subtraction():
    """ Test the subtractions() method of the ExpenseTracker class and 
    makes sure that the ouput is calculated correctly"""
    with mock.patch("builtin.input", side_effect = 
                    [500, "yes", 30, "yes", "fifty", 0, "five",  ]):
        assert subtraction() = 
    assert s (500,100)== 400
    assert s (1000,200)== 800
    assert s (700,500) == 200

def test_balance_warning(capsys):
    assert balance_warning() == expected
    captured = capsys.readouterr()
    assert captured.out == (
        f"LOW BALANCE WARNING: You have used 75 percent of your" 
                          f"available funds. Remaining balance: {self.amount}.\n"
        f"WARNING: You have used half of your available funds. " 
                          f"Remaining balance: {self.amount}.\n"
    )

def test_categorize_shopping():
    with mock.patch("builtin.input",
                    side_effects = ["Bob", "one", "3"]):
        captured = capsys.readouterr()
        assert captured.out == (
            "Bob\n"
            "Not an integer value\n"
            "Enter 1 to add a name, 2 for an item, and 0 when done: \n"
                    )
    
    assert ExpenseTracker == self.person
    assert ExpenseTracker == self.item
  
    # with mock.patch("builtin.input", side_effect = 
    #                 [1, "myself", 2, "clothes", 5, 0, "five" ]): 
    




def test_overdraw_amount(capsys):
    if self.amount >0:
         print(f"Amount left in your account: ${self.amount}")
    elif self.amount ==0:
        print("Zero balance")
        print(f"Amount left in your account: ${self.amount}"))
    elif self.amount<0:
        print("Not enough left in balance")
        print(f"Amount left in your account: ${self.amount}")
    captured = capsys.readouterr()
    assert captured.out == (
        "Not enough left in balance.\n"
        f"Amount left in your account: ${self.amount}.\n"
        f"Don't know who it was bought for at ${self.amount}.\n"
        f"Expense tracker of {self.person[0]} with balance of " 
                  f"${self.amount}.\n"
        f"Expense tracker of {self.person[0]} & {self.person[1]} with" 
                  f" balance of ${self.amount}.\n"
        
    )
    

    