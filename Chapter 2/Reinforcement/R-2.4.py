"""
R-2.4 
Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""


class Flower:
    def _init_(self, name, n_petals, price):
        self._name = name
        self._n_petals = n_petals
        self._price = price

    def get_name(self):
        return self._name

    def get_n_petals(self):
        return self._n_petals

    def get_price(self):
        return self._price

    def set_name(self, new_name):
        self._name = new_name

    def set_n_petals(self, new_quantity):
        self._n_petals = new_quantity

    def set_price(self, new_price):
        self._price = new_price

