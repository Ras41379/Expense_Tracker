from argparse import ArgumentParser
import sys

class ExpenseTracker:
    '''
    Program that allows users to track expenses. 
    Attributes: 
        value(float): the amount to be subtracted from total
        deduction (float): the amount to be subtracted from total   
    '''
    
    def __init__(self, value, balance, deduction): #Chika
        '''
        Initializes the user attribute and tuple that will hold data.
        '''
        self.value = value
        self.balance = balance
        self.deduction = deduction
        
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
        
    def Subtraction(self, balance, deduction): #Chika
        ''' Subtracts the amount of each expense from the total_amount_to_spend
            Parameters:
                balance (int): 
        '''
        #  call stored balance to get remaining balance        
        
        total_amount  = balance - deduction 
        print(f"You new balance is {total_amount}")   
                
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
        '''This method will include a function that will notify the user with a 
        balance warning based on what they set as half and minimum funds.
        
        Args:
            halfway_balance: When the user’s balance is half of what they 
            initially put into the tracker
            low_balance: When the user’s balance is as low as they indicated to 
            avoid.
		'''
    #if else statement, if balance equals half of stored_balance
    #make an f string for available balance of x, print warning message
    #if balance == stored_amount/2 
    #if stored_balance <=0 
    
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
        funds(500)
        subtraction(100)
        print_amount()  
    
    if __name__ == "__main__": #Ray
        main()
        