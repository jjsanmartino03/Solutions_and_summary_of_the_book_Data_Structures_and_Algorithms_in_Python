"""
P-1.35 
The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100.
"""

import random
from datetime import date


def test(data):
    for i in data:
        if data.count(i) > 1:
            return True
    return False


dictio = {}

for i in range(5, 101, 5):
    people_birth = []
    for j in range(i):
        birthday = date.fromordinal(random.randint(1, 365))
        people_birth.append(f"{birthday.month}/{birthday.day}")
    dictio[i] = test(people_birth)

truth = 0
falsety = 0
for i in dictio.values():
    if i:
        truth += 1
    else:
        falsety += 1


print(dictio)

