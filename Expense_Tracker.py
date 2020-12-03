from argparse import ArgumentParser
import sys

class ExpenseTracker:
    '''
    Program that allows users to track expenses. 
    Attributes: 
        value(float): the amount to be subtracted from total
        deduction (float): the amount to be subtracted from total   
    '''
    
    def __init__(self): #Chika
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
        
<<<<<<< Updated upstream
    def subtraction(self): #Chika
=======
    def Subtraction(self, balance, deduction): #Chika
>>>>>>> Stashed changes
        ''' Subtracts the amount of each expense from the total_amount_to_spend
            Parameters:
                balance (int): 
        '''
<<<<<<< Updated upstream
        #  call stored balance to get remaining balance  
               
        total_amount  = self.balance - self.deduction
        print(f"You new balance is {total_amount}") 
        if self.deduction > self.balance:
            print("Not enough availble funds.")
=======
        #  call stored balance to get remaining balance        
        
        total_amount  = balance - deduction 
        print(f"You new balance is {total_amount}")   
>>>>>>> Stashed changes
                
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
<<<<<<< Updated upstream
        if self.balance <= self.funds / 2:
            print(f"WARNING: You have used half of your available funds. Remaining balance: {self.balance}")
        if self.balance <= self.funds / 4:
            print(f"LOW BALANCE WARNING: You have used 75 percent of your available funds. Remaining balance: {self.balance}")  
            
=======
    #if else statement, if balance equals half of stored_balance
    #make an f string for available balance of x, print warning message
    #if balance == stored_amount/2 
    #if stored_balance <=0 
    
>>>>>>> Stashed changes
    def categorize_shopping(self,shopping_list): #Christian
        '''
        This method will contain a dictionary with categories the user will 
        use to divide who/what to shop for 
        
        
        Args:
            shopping_list: the dictionary that will add the categories the user 
            inputs.
        '''
        #shopping_list = []
    
    def parse_args(self):
        """ Parse command-line arguments"""
        parser = ArgumentParser()
        parser.add_argument("filename")
        return parser.parse_args()    
    
    if __name__ == "__main__": #Ray
        args = parse_args(sys.argv[1:])
        
``