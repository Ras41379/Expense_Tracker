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
                deposit = int(input("Enter amount of funds that you wish to input: $"))
                self.balance = self.balance + deposit
                print(f"Amount of funds available: ${self.balance}")
                return self.balance
            except ValueError:
                print("Please enter int value")
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
        sub_amount = []     
        while True:
            try:
                if self.deduction == 0.00:
                    self.deduction = float(input("Enter amount spent: $"))
                    self.amount = self.balance - self.deduction
                    sub_amount.append(self.deduction)
                    sub = str(input("Do you have another item to deduct, enter yes or no: "))
                    if sub == "yes":
                        True
                        continue
                    elif sub == "no":
                        False
                        break 
                else:
                    self.deduction = float(input("Enter another amount spent: $"))
                    self.amount = self.amount - self.deduction
                    sub_amount.append(self.deduction)
                    sub = str(input("Do you have another item to deduct, enter yes or no: "))
                    if sub == "yes":
                        True
                        continue
                    elif sub == "no":
                        False
                        break    
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
            if sub != "Yes" or sub != "No":
                print("Invalid response: Please type yes or no")
                sub = str(input("Do you have another item to deduct, enter yes or no: "))
            break
        self.deduction = sub_amount
        return self.amount, self.deduction
    
    def store_balance(self): #Ray 
        ''' After user is done, saves the amount_spent to a dictionary
        (Used with catorgize_shopping method to build the dictionary)
        
        Attribute:
            totals (dict): Holds the balance values for the user.
        
        Side effect:
            Value of the dictionary will change    
        '''  
    
        my_dict = dict() 
        
        per = self.person
        it = self.item
        total = self.balance
        minus = sum(self.deduction)
        money_left = self.amount
        
        my_dict = {"Total": total, "Minus":minus, "Money left": money_left, 
                   "Person": per, "Items bought": it}
    
        obj = pd.DataFrame.from_dict(my_dict, orient = 'index')
        print(obj)
        
    def overdraw_amount(self): #Sharon
        """ This method will print out message if funds spent are greater
        than amount left in balance ie if the balance is negative """
        if self.amount < 0:
            print("Not enough left in balance")
        else:
            print(f"Amount left in your account: ${self.amount}")
        
        if len(self.person) == 0:
            print(f"Don't know who it was bought for at ${self.amount}.")    
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
        if self.amount <= self.balance / 4:
            print(f"LOW BALANCE WARNING: You have used 75 percent of your" 
                          f"available funds. Remaining balance: {self.amount}") 
        elif self.amount <= self.balance / 2:
            print(f"WARNING: You have used half of your available funds. " 
                          f"Remaining balance: {self.amount}")
        
        
    def categorize_shopping(self): #Christian 
        '''This method will contain a dictionary with categories the user will 
        use to know what to shop for.   
        '''
        shopping_list = [] 
        item = []
        number = int(input("Enter 1 to add a name, 2 for an item, 0 when done: "))
        while True:
            try:
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
            except ValueError:
                print("Not an integer value")
                continue
            if not 0 <= number <= 2:
                number = int(input("Enter 1 to add a name, 2 for an item, and 0 when done: "))
            break
        self.person = shopping_list
        self.item = item
        return self.person, self.item

        
def main(): #Ray
    s = ExpenseTracker() 
    s.categorize_shopping()   
    s.funds()
    s.subtraction()
    s.balance_warning()
    s.overdraw_amount()
    s.store_balance()
    
if __name__ == "__main__":
    main()
        
      