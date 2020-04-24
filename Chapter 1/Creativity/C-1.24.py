"""
C-1.24 
Write a short Python function that counts the number of vowels in a given
character string.
"""


def count_vowels(phrase):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in phrase.lower():
        if i in vowels:
            count += 1
    return count
