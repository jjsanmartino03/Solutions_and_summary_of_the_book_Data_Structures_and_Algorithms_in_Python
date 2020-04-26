"""
P-1.30 
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""

while True:
    number = int(input("Write a number greater than 2:\n"))
    count = 0
    while number >= 2:
        number /= 2
        count += 1
    print(
        f"You must divide that number {count} times by 2 to get a value less than 2: {number}"
    )

