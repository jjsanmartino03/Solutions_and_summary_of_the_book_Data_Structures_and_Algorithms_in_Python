"""
R-2.23 
In similar spirit to the previous problem, augment the Sequence class with
method lt , to support lexicographic comparison seq1 < seq2.
"""


def __lt__(self, other):
    for i in range(len(self)):
        if self[i] < other[i]:
            return True
        elif self[i] > other[i]:
            return False

