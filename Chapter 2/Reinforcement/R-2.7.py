"""
R-2.7 
The CreditCard class of Section 2.3 initializes the balance of 
a new account to zero. Modify that class so that a new account can 
be given a nonzero balance using an optional fifth parameter to the 
constructor. The four-parameter constructor syntax should continue 
to produce an account with zero balance.
"""


def _init_(self, customer, bank, acnt, limit, bqlance=0):
    """
	Create a new credit card instance
    
	The initial balance is provided.
	
	customer    the name of the customer(e.g.,JohnBowman)
	bank        the name of the bank(e.g.,CaliforniaSavings)
	acnt        the acount identifier(e.g.,5391037593875309)
	limit       credit limit(measured in dollars)
	balance     the initial balance of the account
	"""
    self.customer = customer
    self.bank = bank
    self.account = acnt
    self.limit = limit
    self.balance = balance

