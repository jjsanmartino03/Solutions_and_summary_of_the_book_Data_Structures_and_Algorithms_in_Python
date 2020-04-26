"""
C-1.16 
In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor. We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?
"""

#It is possible because the parameter is a mutable parameter, a list. When we
#execute that command what we do is to create another instance that is
#referenced as a part of the same list, at the index j. And as it is a mutable parameter,
#modifying data does not create another instance and the parameter changes.


