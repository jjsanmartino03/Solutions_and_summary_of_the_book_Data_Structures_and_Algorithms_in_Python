"""
P-1.34 
A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""

import random

sentence = "I will never spam my friends again."


rows = []
for i in range(8):
    a = random.randint(0, 99)
    while a in rows:
        a = random.randint(0, 99)
    rows.append(a)
        
def make_error(phrase, num):
    index = random.randint(0, len(phrase)-1)
    listed = list(phrase)
    listed[index] = random.choice(phrase)
    phrase = "".join(listed)
    print(num, phrase, sep=".")

for i in range(100):
    if i in rows:
        make_error(sentence, i)
        continue
    print(f"{i+1}.{sentence}")
