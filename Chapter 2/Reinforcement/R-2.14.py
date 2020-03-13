"""
R-2.14 
Implement the mul method for the Vector class of Section 2.3.3, so
that the expression u*v returns a scalar that represents the dot product of
the vectors, that is, Σdi=1 ui · vi.
"""


class Vector:
    # ...
    def __mul__(self, other):
        if len(self) != len(other):  # relies on len method
            raise ValueError("dimensions must agree")
        results = []
        for i in range(len(self)):
            results.append(self[i] * other[i])
        return sum(results)

