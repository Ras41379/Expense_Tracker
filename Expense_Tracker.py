from argparse import ArgumentParser
import sys

class ExpenseTracker:
    '''
    Program that allows users to track expenses. 
    Attributes: 
        value(float): the amount to be subtracted from total
        deduction (float): the amount to be subtracted from total 
        update_amount(float): total balance after dedcted expses
        new_balance(float):  
          
    '''
    
    def __init__(self): #Chika
        '''
        Initializes the user attribute and tuple that will hold data.
        '''
        self.balance = 0.00
        self.deduction = 0.00
        
    def funds(self): #Sharon
        '''
        Allows user to input available funds and add to existing balance
        '''                                      
        # use f string to ask user to input balance 
        #will be used for suctration method
        
        deposit = int(input("Enter amount of funds that you wish to input:"))
        self.new_balance = self.balance + deposit
        print(f"Amount of funds available {self.new_balance}")
        return (self.new_balance)
        
    def subtraction(self): #Chika
        ''' 
        Subtracts the amount of each expense from the total_amount_to_spend
        Returns: 
            Updated amount after subtracting expense.
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
        print(f"Amount left in your account: {self.balance}")
        
    def balance_warning(self): #Christian
        '''This method will notify the user with a balance 
        warning (based on what they set as half and minimum funds). 
	    '''
        if self.deduction <= self.balance / 2:
            print(f"WARNING: You have used half of your available funds." 
                  f"Remaining balance: {self.updated_amount}")
        elif self.balance <= self.deduction / 4:
            print(f"LOW BALANCE WARNING: You have used 75 percent of your" 
                  f"available funds. Remaining balance: {self.updated_amount}")  
        
        
        
    def categorize_shopping(self,shopping_list): #Christian
        '''
        This method will contain a dictionary with categories the user will 
        use to divide who/what to shop for 
        
        Args:
            shopping_list: the dictionary that will add the categories the user 
            inputs.
        '''
        #shopping_list = [] 
def main():
    s = ExpenseTracker()    
    s.funds()
    s.subtraction()
    s.balance_warning()
main()      
        