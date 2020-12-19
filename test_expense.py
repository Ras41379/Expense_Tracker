from Expense_Tracker import ExpenseTracker
import builtins
from unittest import mock
import pytest
    
def test_expense_funds(capsys):
    """ Test the funds() method of the ExpenseTracker class and makes
    sure that the user is inputting an integer value"""
    with mock.patch("builtin.input",
                    side_effects = ["one, -1, 1"]):
        x = ExpenseTracker.funds
        assert x == "Amount of funds available 1"
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
        assert (500,100)== 400
        assert (1000,200)== 800
        assert (700,500) == 200

def test_balance_warning(capsys, self):
    captured = capsys.readouterr()
    assert captured.out == (
        f"LOW BALANCE WARNING: You have used 75 percent of your" 
                        f"available funds. Remaining balance: {self.amount}.\n"
        f"WARNING: You have used half of your available funds. " 
                        f"Remaining balance: {self.amount}.\n"
    )

def test_categorize_shopping(capsys, self):
    with mock.patch("builtin.input",
                    side_effects = ["1","Bob", "one", "Bob","3", "0"]):
        captured = capsys.readouterr()
        assert captured.out == (
            "Enter 1 to add a name, 2 for an item, 0 when done:\n "
            "Enter who you are shopping for:\n"
            "Enter 1 to add another name, 2 for an item, 0 when done"
            "Not an integer value\n"
            "Enter who you are shopping for:\n"
            "You entered an invalid number\n"
            "Enter 1 to add a name, 2 for an item, and 0 when done:\n"
        )
    assert ExpenseTracker == self.person
    assert ExpenseTracker == self.item

def test_overdraw_amount(capsys, self):
    if self.amount >0:
         print(f"Amount left in your account: ${self.amount}")
    elif self.amount ==0:
        print("Zero balance")
        print(f"Amount left in your account: ${self.amount}")
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
    

    