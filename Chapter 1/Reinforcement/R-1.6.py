"""
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""


def square_of_odds(n):
    return sum(x ** 2 for x in range(1, n) if x % 2)
