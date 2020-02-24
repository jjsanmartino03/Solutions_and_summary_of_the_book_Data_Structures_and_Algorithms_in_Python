"""
C-1.15 
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""

def all_dif(data):
    for index, number in data:
        for j in data[index+1:]:
            if number == j:
                return False
    return True

