"""
Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.
"""

#As I had already done this exercise in R-1.4, I didn't do anything new
def squares_sum(n):
    return sum(x**2 for x in range(1, n))