"""
R-2.12 
Implement the mul method for the Vector class of Section 2.3.3, so
that the expression v*3 returns a new vector with coordinates that are 3
times the respective coordinates of v.
"""
class Vector:
    #...
    def __mul__(self, other):
        new_vector_list = [coor*other for coor in self[:]]
        new_vector = Vector(len(self))
        new_vector[:] = new_vector_list
        return new_vector