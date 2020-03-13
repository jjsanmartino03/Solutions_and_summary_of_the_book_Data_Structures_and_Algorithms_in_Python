"""
R-2.13 
Exercise R-2.12 asks for an implementation of mul , for the Vector
class of Section 2.3.3, to provide support for the syntax v 3. Implement
the rmul method, to provide additional support for syntax 3 v.
"""


class Vector:
    # ...
    def __rmul__(self, other):
        return self * other
