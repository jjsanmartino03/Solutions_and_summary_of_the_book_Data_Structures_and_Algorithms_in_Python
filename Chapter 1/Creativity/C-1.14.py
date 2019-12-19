"""
C-1.14 
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

def find_odd_products(data):
    for i in data:
        for j in data:
            if j != i:
                if (j*i) % 2:
                    return True
    return False
