"""
R-1.4 
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def squares_sum(n):
    return sum(x**2 for x in range(1, n))
