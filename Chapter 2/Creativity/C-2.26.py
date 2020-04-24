"""
The SequenceIterator class of Section 2.3.4 provides what is known as a
forward iterator. Implement a class named ReversedSequenceIterator that
serves as a reverse iterator for any Python sequence type. The first call to
next should return the last element of the sequence, the second call to next
should return the second-to-last element, and so forth.
"""


class ReversedSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._n = len(sequence)

    def __next__(self):
        self._n -= 1
        if self._n > -1:
            return self._seq[self._n]
        else:
            raise StopIteration()

    def __iter__(self):
        return self
