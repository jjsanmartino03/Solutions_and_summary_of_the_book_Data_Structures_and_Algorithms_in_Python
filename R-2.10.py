"""
R-2.10
Implement the __neg__ method for the Vector class of Section 2.3.3, so
that the expression −v returns a new vector instance whose coordinates
are all the negated values of the respective coordinates of v.
"""


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self.coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self.coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self.coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self.coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
            return result

    def __sub__(self, other):
        """Return substraction of two vectors"""
        if len(self) != len(other):  # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self.coords == other.coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other  # rely on existing eq definition

    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self.coords)[1:-1] + ">"  # adapt list representation

    def __neg__(self):
        """
        Returns a new vector instance whose coordinates 
        are all the negated values of the respective coordinates of self
        """
        new_vector_list = [-i for i in self[:]]
        new_vector = Vector(len(self))
        new_vector[:] = new_vector_list
        return new_vector


if __name__ == "__main__":
    b = Vector(5)
    b[:] = [3, 5, 6, 9, 1]
    print(-b)

