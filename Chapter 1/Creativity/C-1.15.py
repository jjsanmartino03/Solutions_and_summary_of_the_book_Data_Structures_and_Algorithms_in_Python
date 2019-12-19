"""
C-1.15 
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""

def all_dif(data):
    for i in data:
        data.remove(data[0])
        for j in data:
            if i == j:
                return False
    return True


print(all_dif([1, 2, 5, 78]))

