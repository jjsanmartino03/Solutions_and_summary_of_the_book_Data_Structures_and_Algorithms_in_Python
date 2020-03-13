"""
R-2.11 
In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector.
"""

"""
To reach that objective you have to add an radd method to the Vector class,
so when python executes v = [5, 3, 10, −2, 1] + u it finds out that is an 
illegal operation (because the add method of the list class haven't got a way
to concatenate itself to a vector object), and then goes to the Vector class
searching an radd method
"""


class Vector:
    # ...
    def __radd__(self, other):
        return self + other

