class ExpenseTracker:
    '''
    Program that allows users to track expenses. 
    '''
    
<<<<<<< HEAD
    def __init__(self): # Chika 
=======
    def __init__(self): #Chika
>>>>>>> 20c2763c250886e42c7edef4c29dfe2cf5838ecc
        '''
        Initializes the user attribute and tuple that will hold data.
        '''
        
<<<<<<< HEAD
    def funds(self): # Sharon
=======
    def funds(self): #Sharon
>>>>>>> 20c2763c250886e42c7edef4c29dfe2cf5838ecc
        '''
        Allows user to input available funds
        '''                                      
    
<<<<<<< HEAD
    def Subtraction(self,total_amount): # Chika 
=======
    def Subtraction(self,total_amount): #Chika
>>>>>>> 20c2763c250886e42c7edef4c29dfe2cf5838ecc
        ''' Subtracts the amount of each expense from the total_amount_to_spend
        
        Attributes:
            value(float): the amount to be subtracted from total   
        '''
        
    def Store_balance(self,total_amount): #Ray
        ''' After user is done, saves the amount_spent to a dictionary
        
        Attribute:
            totals (dict): Holds the balance values for the user.
        
        Side effect:
            Value of the tuples will change
        '''  
          
    def print_amount(self,funds): #Sharon
        """This method will print the amount of funds remaining after using the 
        funds
        
        Args:
            funds (float): the funds available for use
        Side effect:
            print statement
        """
        
    def balance_warning(self,halfway_balance,low_balance): #Christian
        '''This method will include a function that will notify the user with a 
        balance warning based on what they set as half and minimum funds.
        
        Args:
            halfway_balance: When the user’s balance is half of what they 
            initially put into the tracker
            low_balance: When the user’s balance is as low as they indicated to 
            avoid.
		'''
    
    def categorize_shopping(self,shopping_list): #Christian
        '''
        This method will contain a dictionary with categories the user will 
        use to divide who/what to shop for 
        
        
        Args:
            shopping_list: the dictionary that will add the categories the user 
            inputs.
        '''
        
    if __name__ == __main__() #Ray