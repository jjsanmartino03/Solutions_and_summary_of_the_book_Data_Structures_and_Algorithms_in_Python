"""
P-1.29
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""
import io
import itertools
import math
import sys
import requests

# print(requests.get("douu"))
h = 0

print(input(">>>"))


def last_two(chars):
    global h
    for i in range(2):
        chars[4], chars[5] = chars[5], chars[4]
        h += 1


def last_three(chars):
    for i in range(3):
        chars[3], chars[4] = chars[4], chars[3]
        last_two(chars)


def last_four(chars):
    for i in range(4):
        chars[2], chars[3] = chars[3], chars[2]
        last_three(chars)


def last_five(chars):
    for i in range(5):
        chars[1], chars[2] = chars[2], chars[1]
        last_four(chars)


def word(chars):
    for i in range(6):
        chars[0], chars[1] = chars[1], chars[0]
        last_five(chars)


word(["c", "a", "t", "d", "o", "g"])
print(h)
