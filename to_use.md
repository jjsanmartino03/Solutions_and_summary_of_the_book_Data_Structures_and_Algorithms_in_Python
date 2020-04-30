### 2._3._2 Operator overloading and Python special mehods
- In python, a and b being classes:
  - `a + b` automatically makes the call `a.___add__(b)`
- That is called **operator overloading**
- Instead, when `b + a` executes, if b does not have support for that **operation** or more specifically for that operation with `a`, then `a.___radd__()` is called

Common Syntax | Special Method Form
--------------|--------------------
a − b | a._\_\_sub\_\_(b); alternatively b._\_\_rsub\_\_(a)
a + b | a._\_\_add\_\_(b); alternatively b._\_\_radd\_\_(a)
a b | a._\_\_mul\_\_(b); alternatively b._\_\_rmul\_\_(a)
a / b | a._\_\_truediv\_\_(b); alternatively b._\_\_rtruediv\_\_(a)
a // b | a._\_\_floordiv\_\_(b); alternatively b._\_\_rfloordiv\_\_(a)
a % b | a._\_\_mod\_\_(b); alternatively b._\_\_rmod\_\_(a)
a b | a._\_\_pow\_\_(b); alternatively b._\_\_rpow\_\_(a)
a << b | a._\_\_lshift\_\_(b); alternatively b._\_\_rlshift\_\_(a)
a >> b | a._\_\_rshift\_\_(b); alternatively b._\_\_rrshift\_\_(a)
a & b | a._\_\_and\_\_(b); alternatively b._\_\_rand\_\_(a)
a ˆ b | a._\_\_xor\_\_(b); alternatively b._\_\_rxor\_\_(a)
a \| b | a._\_\_or\_\_(b); alternatively b._\_\_ror\_\_(a)
a += b | a._\_\_iadd\_\_(b)
a −= b | a._\_\_isub\_\_(b)
a = b | a._\_\_imul\_\_(b)
+a | a._\_\_pos\_\_()
−a | a._\_\_neg\_\_()
˜a | a._\_\_invert\_\_()
abs(a) | a._\_\_abs\_\_()
a < b | a._\_\_lt\_\_(b)
a <= b | a._\_\_le\_\_(b)
a > b | a._\_\_gt\_\_(b)
a >= b | a._\_\_ge\_\_(b)
a == b | a._\_\_eq\_\_(b)
a != b | a._\_\_ne\_\_(b)
v in a | a._\_\_contains\_\_(v)
a[k] | a._\_\_getitem\_\_(k)
a[k] = v | a._\_\_setitem\_\_(k,v)
del a[k] | a._\_\_delitem\_\_(k)
a(arg1, arg2, ._._._) | a._\_\_call\_\_(arg1, arg2, ._._._)
len(a) | a._\_\_len\_\_()
hash(a) | a._\_\_hash\_\_()
iter(a) | a._\_\_iter\_\_()
next(a) | a._\_\_next\_\_()
bool(a) | a._\_\_bool\_\_()
float(a) | a._\_\_float\_\_()
int(a) | a._\_\_int\_\_()
repr(a) | a._\_\_repr\_\_()
reversed(a) | a._\_\_reversed\_\_()
str(a) | a._\_\_str\_\_()

#### Some Non-operator overloads
- `str(foo) --> foo.___str__()` is called when foo is not a built-in class
- `len(foo) --> foo.___len__()`
- `iter(foo) --> foo.___iter__()`

#### Implied Methods
- `bool(foo) --> foo.___bool__()`, if foo does not support `bool()`, then it returns True, and if the object can be lenght-measured, it returns `True` if length > 0
- If a **container object** has `__len__()` and `__getitem__()`, then `iter(foo)` is automatically provided
- `a == b` is equal to `a is b` when either object supports the operation

### 2._3._3 Example: Multidimensional Vector Class
```python
class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector._"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other._"""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other  # rely on existing eq definition

    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self._coords)[1:-1] + ">"  # adapt list representation
```

### 2._3._4 Iterators
- Iterators **for a collection** are objects that return the nexts elements of a collection, when `next(object)` is called._
- An alternative is the use of `yield`, the generator syntax
- Example of low-level sequence iterator:

```python
class SequenceIterator:
    """An iterator for any of Python s sequence types._"""

    def __init__(self, sequence):
        """Create an iterator for the given sequence._"""
        self._seq = sequence # keep a reference to the underlying data
        self._k = −1 # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1 # advance to next index
        if self._k < len(self._seq):
            return(self._seq[self._k]) # return the data element
        else:
            raise StopIteration( ) # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self
```

### 2._3._5 Example: Range Class
```python
class Range:
    """A class that mimic s the built-in range class._"""

    def init (self, start, stop=None, step=1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError( "step cannot be 0" )

        if stop is None: # special case of range(n)
            start, stop = 0, start # should be treated as if range(0,n)

        # calculate the effective length once
        self._length = max(0, (stop − start + step − 1) // step)

        # need knowledge of start and step (but not stop) to support getitem
        self._start = start
        self._step = step

    def len (self):
        """Return number of entries in the range."""
        return self._length

    def getitem (self, k):
        """Return entry at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self) # attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError("index out of range")

        return self._start + k self._step
```

## 2.4 Inheritance
