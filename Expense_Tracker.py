#  Group 312: Chika Chuku, Sharon Lee, Christian Escobar, Ray Swenton
from argparse import ArgumentParser
import sys

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
        self.deduction = 0.00
        
    def funds(self): #Sharon
        '''
        Allows user to input available funds and add to existing balance
        Returns:
            Updated amount/new balance after user inputs desired funds
        '''                                      
        # use f string to ask user to input balance 
        #will be used for suctration method
        
        deposit = int(input("Enter amount of funds that you wish to input:"))
        self.new_balance = self.balance + deposit
        print(f"Amount of funds available {self.new_balance}")
        return (self.new_balance)
        
    def subtraction(self): #Chika
        ''' 
        Subtracts the amount of each expense from the new_balance.
        Returns: 
            Updated amount after subtracting expense(updated_amount).
        '''        
        while True:
            deduct = int(input("Enter amount spent: "))
            self.updated_amount = self.new_balance - deduct      
            if deduct > self.new_balance:
                print("Not enough availble funds. Please enter new expense: ")
                continue
            else:
                print(f"Your updated balance is ${self.updated_amount}")
                return self.updated_amount
    
    def store_balance(self): #Ray #Not completed
        ''' After user is done, saves the amount_spent to a dictionary
        (Used with catorgize_shopping method to build the dictionary)
        
        Attribute:
            totals (dict): Holds the balance values for the user.
        
        Side effect:
            Value of the dictionary will change    
        '''  
        
        
    def print_amount(self): #Sharon: not yet completed
        """This method will print the amount of funds remaining after using the 
        funds
        Side effect:
            print statement
        """
        print(f"Amount left in your account: {self.balance}")
        
    def balance_warning(self): #Christian
        '''This method will notify the user with a balance 
        warning for half and low available funds. 
	    '''
        if self.balance <= self.deduction / 4:
            print(f"LOW BALANCE WARNING: You have used 75 percent of your" 
                  f"available funds. Remaining balance: {self.updated_amount}") 
        elif self.deduction <= self.balance / 2:
            print(f"WARNING: You have used half of your available funds." 
                  f"Remaining balance: {self.updated_amount}")
        
        
    def categorize_shopping(self): #Christian #not completed
        '''This method will contain a dictionary with categories the user will 
        use to know what to shop for.   
        '''
        #shopping_list = [] 
        
def main(): #Ray
    s = ExpenseTracker()    
    s.funds()
    s.subtraction()
    s.balance_warning()
main()
        
        