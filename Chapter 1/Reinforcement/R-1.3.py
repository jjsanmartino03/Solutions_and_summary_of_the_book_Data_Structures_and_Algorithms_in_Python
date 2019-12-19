"""
R-1.3 
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""

def minmax(data):
    maxie, minie = data[0], data[0]
    for i in data:
        maxie = i if i > maxie else maxie
        minie = i if i < minie else minie
    return minie, maxie
