"""
P-1.29
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""
import copy


def my_function(alr, left):
    print(alr)
    if left:
        for i in left:
            newl = copy.deepcopy(left)
            newl.remove(i)
            my_function(alr + list(i), newl)


"""
original = ["c", "a", "t", "d", "g", "o"]
for i in original:
    new_list = copy.deepcopy(original)
    new_list.remove(i)
    my_function(list(i), new_list)
"""

# txt = "catdog"

# solution = list(itertools.permutations(txt))

# without itertools
def recursed_permutations(txt):
    for i in txt:
        if len(txt) > 1:
            for j in recursed_permutations(txt[:1]):
                yield txt
                print(txt)
        else:
            yield txt
        txt = f"{txt[1:]}{txt[-1]}"


list(recursed_permutations(txt))
