"""
C-1.20 
Python’s random module includes a function shuffle(data) that accepts a list of elements
and randomly reorders the elements so that each possible order occurs with equal probability.
The random module includes a more basic function randint(a, b) that returns a uniformly
random integer from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""

from random import randint


def shuffle(data):
    positions = {}
    used = []
    new_index = randint(0, (len(data) - 1))
    for i in data:
        while new_index in used:
            new_index = randint(0, (len(data) - 1))
        used.append(new_index)
        positions.setdefault(i, new_index)
    for key, value in positions.items():
        data[value] = key

