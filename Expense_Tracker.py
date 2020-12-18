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
        self.deduction = 0.00
        self.amount = 0.00
        self.person = " "
        self.item = " "
        
    def funds(self): #Sharon
        '''
        Allows user to input available funds and add to existing balance
        Returns:
            Updated amount/new balance after user inputs desired funds
        '''                                      
        # use f string to ask user to input balance 
        #will be used for suctration method
        while True:
            try:
                deposit = int(input("Enter amount of funds that you wish to input: "))
                self.balance = self.balance + deposit
                print(f"Amount of funds available {self.balance}")
                return self.balance
            except ValueError:
                print("please enter int value")
                continue
            if 0 >= deposit:
                print("Enter a number greater than 0.")
                continue
            break
        
    def subtraction(self): #Chika
        ''' 
        Subtracts the amount of each expense from the new_balance.
        Returns: 
            Updated amount after subtracting expense(updated_amount).
        '''  
        sub = "yes"
        sub_amount = []     
        while sub == "yes":
            try:
                if self.deduction == 0.00:
                    self.deduction = float(input("Enter amount spent: "))
                    self.amount = self.balance - self.deduction
                    sub_amount.append(self.deduction)
                    sub = str(input("Do you have another item to deduct, enter yes or no: "))
                    continue  
                else:
                    self.deduction = float(input("Enter another amount spent: "))
                    self.amount = self.amount - self.deduction
                    sub_amount.append(self.deduction)
                    sub = str(input("Do you have another item to deduct, enter yes or no: "))
                    continue
            except ValueError:
                print("You didn't enter a number for the amount spent!")
                sub = "yes"
            if sub != "yes" or sub != "no":
                print("Invalid response: Please type yes or no")
                sub = str(input("Do you have another item to deduct, enter yes or no: "))
            break
        while True:
            try:    
                if self.amount >= self.balance:
                    self.deduction = int(input("Not enough availble funds. Please enter new expense: "))
                    continue
                else:
                    print(f"Your updated balance is ${self.amount}")
                    break
            except ValueError:
                print("Please type a number greater than 0.")
                continue
            break
        self.deduction = sub_amount
        return self.amount, self.deduction
    
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
        
        per = self.person
        it = self.item
        total = self.balance
        minus = sum(self.deduction)
        money_left = self.amount
        
        my_dict = {"total": total, "minus":minus, "money left": money_left, 
                   "person": per, "items bought": it}
    
        obj = pd.DataFrame.from_dict(my_dict, orient = 'index')
        print(obj)
        
    def print_amount(self): #Sharon: not yet completed
        """This method will print the amount of funds remaining after using the 
        funds
        Side effect:
            print statement
        """
        print(f"Amount left in your account: ${self.amount}")
    
    def overdraw_amount(self):
        """ This method will print out message if funds spent are greater
        than amount left in balance ie if the balance is negative """
        if self.amount < 0:
            print("Not enough left in balance")
        else:
            print(f"Amount left in your account: ${self.amount}")
        if len(self.person) == 0:
            print("Don't know who it was bought for.")    
        elif len(self.person) == 1:
            print(f"Expense tracker of {self.person[0]} with balance of " 
                  f"${self.amount}")
        else:
            print(f"Expense tracker of {self.person[0]} & {self.person[1]} with" 
                  f" balance of ${self.amount}")
        
        
    def balance_warning(self): #Christian
        '''This method will notify the user with a balance 
        warning for half and low available funds. 
	    '''
        while True:
            try:
                if self.amount <= self.balance / 4:
                    print(f"LOW BALANCE WARNING: You have used 75 percent of your" 
                          f"available funds. Remaining balance: {self.amount}") 
                elif self.amount <= self.balance / 2:
                    print(f"WARNING: You have used half of your available funds. " 
                          f"Remaining balance: {self.amount}")
            except ValueError:
        
    def categorize_shopping(self): #Christian #not completed
        '''This method will contain a dictionary with categories the user will 
        use to know what to shop for.   
        '''
        shopping_list = [] 
        item = []
        number = int(input("Enter 1 to add a name, 0 when done: "))
        while number != 0:
            if number == 1:
                person = str(input("Enter who you are shopping for: "))
                shopping_list.append(person)
                number = int(input("Enter 1 to add another name, 2 for an item, " + 
                                   "0 when done: "))
            elif number == 2:
                item1 = str(input("Name of item bought: "))
                item.append(item1)
                number = int(input("Enter 2 to another item, 0 when done: "))
            else:
                print("You entered an invalid number")
                number = int(input("Enter 1 to add a name, 2 to add an item, "
                                   "or 0 when done: "))
        self.person = shopping_list
        self.item = item
        return self.person, self.item

        
def main(): #Ray
    s = ExpenseTracker() 
    s.categorize_shopping()   
    s.funds()
    s.subtraction()
    s.balance_warning()
    s.store_balance()
    s.overdraw_amount()

    
main()
        
        