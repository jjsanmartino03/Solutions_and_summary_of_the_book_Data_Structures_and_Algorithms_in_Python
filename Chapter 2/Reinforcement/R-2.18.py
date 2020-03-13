"""
R-2.18 
Give a short fragment of Python code that uses the progression classes
from Section 2.4.2 to find the 8th value of a Fibonacci progression that
starts with 2 and 2 as its first two values.
"""

fibo = FibonacciRegression(2, 2)

for i in range(8):
    next(fibo)

print(fibo)
