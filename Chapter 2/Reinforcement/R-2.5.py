"""
R-2.5 
Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter.
"""


class NewCreditCard(CreditCard):
    def make_payment(self, amount):
        try:
            float(amount)
            super().make_payment(amount)
        except ValueError:
            print("Invalid payment value")

    def charge(self, amount):
        try:
            float(amount)
            super().make_payment(amount)
        except ValueError:
            print("Invalid charge value")

