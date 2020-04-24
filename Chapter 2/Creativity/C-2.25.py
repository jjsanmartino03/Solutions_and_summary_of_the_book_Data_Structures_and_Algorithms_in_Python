"""
Exercise R-2.12 uses the mul method to support multiplying a Vector
by a number, while Exercise R-2.14 uses the mul method to support
computing a dot product of two vectors. Give a single implementation of
Vector. mul that uses run-time type checking to support both syntaxes
u v and u k, where u and v designate vector instances and k represents
a number.
"""

class Vector:
    # ...
    def __mul__(self, other):
        try:
            int(other):
            new_vector_list = [coor*other for coor in self[:]]
            new_vector = Vector(len(self))
            new_vector[:] = new_vector_list
            return new_vector
        except TypeError:
            if len(self) != len(other):  # relies on len method
                raise ValueError("Dimensions must agree")
            results = []
            for i in range(len(self)):
                results.append(self[i] * other[i])
            return sum(results)