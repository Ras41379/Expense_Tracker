from argparse import ArgumentParser
import sys

class ExpenseTracker:
    '''
    Program that allows users to track expenses. 
    Attributes: 
        value(float): the amount to be subtracted from total
        deduction (float): the amount to be subtracted from total   
    '''
    
    def __init__(self, balance, deduction): #Chika
        '''
        Initializes the user attribute and tuple that will hold data.
        '''
        self.balance = 0
        self.deduction = 0
        
    def funds(self): #Sharon
        '''
        Allows user to input available funds and add to existing balance
        '''                                      
        # use f string to ask user to input balance 
        #will be used for suctration method
        
        deposit = int(input("Enter amount of funds that you wish to input:"))
        new_balance = self.balance + deposit
        print(f"Amount of funds available {new_balance}")
        return (new_balance)
        
    def subtraction(self): #Chika
        ''' Subtracts the amount of each expense from the total_amount_to_spend
            Parameters:
                balance (int): 
        '''
        #  call stored balance to get remaining balance        
        
        updated_amount = self.balance - self.deduction
        if self.deduction > self.balance:
            print("Not enough availble funds. Please enter new expense: ")        
        # print(f"You new balance is {updated_amount}")   
        return updated_amount        
    
    def store_balance(self,total_amount): #Ray
        ''' After user is done, saves the amount_spent to a dictionary
        
        # Attribute:
        #     totals (dict): Holds the balance values for the user.
        
        Side effect:
            Value of the dictionary will change    
        '''  
        
        
    def print_amount(self): #Sharon
        """This method will print the amount of funds remaining after using the 
        funds
        
        Args:
            funds (float): the funds available for use
        Side effect:
            print statement
        """
        print("Amount left in your account: "+ str(self.balance))
        
    def balance_warning(self): #Christian
        '''This method will notify the user with a balance 
        warning (based on what they set as half and minimum funds). 
	    '''
    
        if self.deduction <= self.balance / 2:
            print(f"WARNING: You have used half of your available funds. Remaining balance: {self.balance}")
        elif self.balance <= self.deduction / 4:
            print(f"LOW BALANCE WARNING: You have used 75 percent of your available funds. Remaining balance: {self.balance}")  
        
    def categorize_shopping(self,shopping_list): #Christian
        '''
        This method will contain a dictionary with categories the user will 
        use to divide who/what to shop for 
        
        Args:
            shopping_list: the dictionary that will add the categories the user 
            inputs.
        '''
        #shopping_list = [] 

s = ExpenseTracker()    
s.funds()
s.subtraction()
s.balance_warning()
        
        