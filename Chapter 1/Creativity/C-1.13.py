"""
C-1.13 
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""

#function parameters:list of integers
#for each element in list:
#   insert it in a new list with index zero
#return the new list

data = [2, 73, 5, 89]
#data.reverse(), this is the equivalent function
data[::-1] #this is another way of reaching the same objective

