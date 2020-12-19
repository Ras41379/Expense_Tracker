from Expense_Tracker import ExpenseTracker
import builtins
from unittest import mock
import pytest
    
def test_expense_funds(capsys):
    """ Test the funds() method of the ExpenseTracker class and makes
    sure that the user is inputting an integer value"""
    with mock.patch("builtins.input",
                    side_effect = ["one, -1, 1"]):
        x = ExpenseTracker()
        assert x.funds() == 1
        captured = capsys.readouterr()
        assert captured.out == (
            "please enter int value.\n"
            "Enter a number greater than 0.\n"
        )
def test_subtraction(capsys):
    """ Test the subtractions() method of the ExpenseTracker class and 
    makes sure that the ouput is calculated correctly"""
    with mock.patch("builtins.input", side_effect = 
                    ["500", "yes", "30", "yes", "fifty", "no"]):
        ET = ExpenseTracker()
        assert ET.subtraction() == (-530.0,[500.0, 30.0])
        captured = capsys.readouterr()
        assert captured.out == (
            "You didn't enter a number for the amount spent!\n"
            'Invalid response: Please type yes or no\n' 
            'Your updated balance is $-530.0\n'
        )
        

def test_balance_warning(capsys):
    ET = ExpenseTracker()
    assert ET.balance_warning()
    captured = capsys.readouterr()
    assert captured.out == (
        f"LOW BALANCE WARNING: You have used 75 percent of your" 
                        f"available funds. Remaining balance: {self.amount}.\n"
        f"WARNING: You have used half of your available funds. " 
                        f"Remaining balance: {self.amount}.\n"
    )

def test_categorize_shopping(capsys):
    with mock.patch("builtins.input",
                    side_effect = ["1","Bob","3", "0"]):
        ET = ExpenseTracker()
        assert ET.categorize_shopping() == "Bob", []
        captured = capsys.readouterr()
        assert captured.out == (
            "Enter 1 to add a name, 2 for an item, 0 when done:\n"
            "Enter who you are shopping for:\n"
            "Enter 1 to add another name, 2 for an item, 0 when done:\n"
            "Invalid number: Please enter 1 for a person, 2 for an item, 0 when" 
            " done:\n"
        )
    

def test_overdraw_amount(capsys):
    ET = ExpenseTracker()
    assert ET.overdraw_amount() == None 
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
    

    