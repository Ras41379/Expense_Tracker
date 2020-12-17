from Expense_Tracker import subtraction as s
import pytest


def test_expense_init():
    """ Test the __init__() method of the ExpenseTracker class."""
    tracker= Tracker()
    assert tracker.balance == 0
    assert tracker.deduction == 0
    
def test_expense_funds():
    """ Test the funds() method of the ExpenseTracker class and makes
    sure that the user is inputting an integer value"""
    while True:
        try: 
            userInput= int(input(message))
        except ValueError:
            print("Not an integer! Please input an int value")
            continue
        else:
            continue
def test_subtractions():
    """ Test the subtractions() method of the ExpenseTracker class and 
    makes sure that the ouput is calculated correctly"""
    assert s.subtract(500,100)== 400
    assert s.subtract(1000,200)== 800
    assert s.subtract(700,500) == 200
    