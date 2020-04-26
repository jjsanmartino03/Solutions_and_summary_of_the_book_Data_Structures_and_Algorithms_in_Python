"""
C-1.17 
Had we implemented the scale function (page 25) as follows, does it work
properly?

def scale(data, factor):
    for val in data:
        val = factor
        
Explain why or why not.
"""

#No, it does not work because you are only multiplying a value
# by a number, but you are not assigning the product to a
# variable or a part of a list
def scale(data, factor):
    for val in data:
        val *= factor
