"""
R-1.7 
Give a single command that computes the sum from Exercise R-1.6, relying
on Python’s comprehension syntax and the built-in sum function.
"""

# As I had already done this exercise in R-1.6, I didn't do anything new
def square_of_odds(n):
    return sum(x ** 2 for x in range(1, n) if x % 2)
