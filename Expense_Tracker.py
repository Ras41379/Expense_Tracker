#  Group 312: Chika Chuku, Sharon Lee, Christian Escobar, Ray Swenton
from argparse import ArgumentParser
import sys
import pandas as pd

class ExpenseTracker:
    '''
    Program that allows users to track expenses. 
    Attributes: 
        balance(float): initial available funds.  
        deduction (float): the amount to be subtracted from balance. 
        update_amount(float): total balance after deducted expenses.
        new_balance(float): total balance after funds are deposited.
        totals (dict): Holds the balance values for the user.
      

    '''
    
    def __init__(self): #Chika
        '''
        Initializes attributes and dictionary that will hold data.
        '''
        self.balance = 0.00
        print(self.balance)
        self.deduction = 0.00
        print(self.deduction)
        self.amount = 0.00
        print(self.amount)
        self.person = " "
        print(self.person)
        self.item = " "
        print(self.item)
        
        
    def funds(self): #Sharon
        '''
        Allows user to input available funds and add to existing balance
        Returns:
            Updated amount/new balance after user inputs desired funds
        '''                                      
        # use f string to ask user to input balance 
        #will be used for suctration method
        print(self.balance)
        print(self.deduction)
        deposit = float(input("Enter amount of funds that you wish to input:"))
        self.balance = self.balance + deposit
        print(f"Amount of funds available {self.balance}")
        return self.balance
        
    def subtraction(self): #Chika
        ''' 
        Subtracts the amount of each expense from the new_balance.
        Returns: 
            Updated amount after subtracting expense(updated_amount).
        '''  
        print(self.balance)
        print(self.deduction)      
        while True:
            self.deduction = float(input("Enter amount spent: "))
            self.amount = self.balance - self.deduction      
            if self.deduction > self.balance:
                print("Not enough availble funds. Please enter new expense: ")
                continue  
            else:
                print(f"Your updated balance is ${self.amount}")
                break
        return self.deduction, self.amount
                
    
    def store_balance(self): #Ray #Not completed
        ''' After user is done, saves the amount_spent to a dictionary
        (Used with catorgize_shopping method to build the dictionary)
        
        Attribute:
            totals (dict): Holds the balance values for the user.
        
        Side effect:
            Value of the dictionary will change    
        '''  
        
        #working on a way to put the information into a dict and then into a pandas
        #dataframe for storage and listing when the user is done entered amounts.
    
        my_dict = dict() 
        total = self.balance
        print(total)
        amount = self.deduction
        print(amount)
        bal = self.amount
        print(bal)
        my_dict = {"total": float(total), "sub": float(amount), "amount": float(bal)}
        print(my_dict)
        obj = pd.DataFrame.from_dict(my_dict, orient = 'index')
        print(obj)
        #return obj
        
    def print_amount(self): #Sharon: not yet completed
        """This method will print the amount of funds remaining after using the 
        funds
        Side effect:
            print statement
        """
        print(f"Amount left in your account: {self.balance}")
        
    def balance_warning(self): #Christian #done?
        '''This method will notify the user with a balance 
        warning for half and low available funds. 
	    '''
        if self.amount <= self.balance / 4:
            print(self.amount)
            print(self.balance)
            print(f"LOW BALANCE WARNING: You have used 75 percent of your "
               f"available funds. Remaining balance: {self.amount}")
        elif self.amount <= self.balance / 2:
            print(self.amount)
            print(self.balance)
            print(f"WARNING: You have used half of your available funds. "
              f"Remaining balance: {self.amount}")
        
        
    def categorize_shopping(self): #Christian #semi done
        '''This method will contain a dictionary with categories the user will 
        use to know what to shop for.   
        '''
        
        list = []
        item = []
        number = int(input("Enter 1 to add a name, 0 when done: "))
        while number == 1:
            person = input("Enter who you are shopping for: ")
            list.append(person)
            print(list)
            number = int(input("Enter 1 to add another name, 2 for an item, " +
            "0 when done: "))
        while number == 2:
            item1 = input("Name item bought: ")
            item.append(item1)
            print(item)
            number = int(input("Enter 1 to add another name, 2 for an item, " +
            "0 when done: "))
        else:
            self.person = list
            self.item = item
            return self.person, self.item
        
def main(): #Ray
    s = ExpenseTracker()
    s.categorize_shopping()    
    s.funds()
    s.subtraction()
    s.balance_warning()
    s.store_balance()
    
main()
        
        