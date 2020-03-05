"""
R-2.6 
If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.
"""


class NewCreditCard(CreditCard):
    def make_payment(self, amount):
        try:
            if not type(amount) in (float, int):
                raise ValueError
            if amount < 0:
                raise ValueError
            super().make_payment(amount)
        except ValueError:
            print("Invalid payment value")

    def charge(self, amount):
        try:
            if not type(amount) in (float, int):
                raise ValueError
            super().charge(amount)
        except ValueError:
            print("Invalid charge value")

