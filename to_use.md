### 2._3._2 Operator overloading and Python special mehods
- In python, a and b being classes:
  - `a + b` automatically makes the call `a.___add__(b)`
- That is called **operator overloading**
- Instead, when `b + a` executes, if b does not have support for that **operation** or more specifically for that operation with `a`, then `a.___radd__()` is called

Common Syntax | Special Method Form
--------------|--------------------
a − b | a.\_\_sub\_\_(b); alternatively b._\_\_rsub\_\_(a)
a + b | a.\_\_add\_\_(b); alternatively b._\_\_radd\_\_(a)
a b | a.\_\_mul\_\_(b); alternatively b._\_\_rmul\_\_(a)
a / b | a.\_\_truediv\_\_(b); alternatively b.\_\_rtruediv\_\_(a)
a // b | a.\_\_floordiv\_\_(b); alternatively b.\_\_rfloordiv\_\_(a)
a % b | a.\_\_mod\_\_(b); alternatively b._\_\_rmod\_\_(a)
a b | a.\_\_pow\_\_(b); alternatively b._\_\_rpow\_\_(a)
a << b | a.\_\_lshift\_\_(b); alternatively b._\_\_rlshift\_\_(a)
a >> b | a.\_\_rshift\_\_(b); alternatively b._\_\_rrshift\_\_(a)
a & b | a.\_\_and\_\_(b); alternatively b._\_\_rand\_\_(a)
a ˆ b | a.\_\_xor\_\_(b); alternatively b._\_\_rxor\_\_(a)
a \| b | a.\_\_or\_\_(b); alternatively b._\_\_ror\_\_(a)
a += b | a.\_\_iadd\_\_(b)
a −= b | a.\_\_isub\_\_(b)
a = b | a.\_\_imul\_\_(b)
+a | a.\_\_pos\_\_()
−a | a.\_\_neg\_\_()
˜a | a.\_\_invert\_\_()
abs(a) | a.\_\_abs\_\_()
a < b | a.\_\_lt\_\_(b)
a <= b | a.\_\_le\_\_(b)
a > b | a.\_\_gt\_\_(b)
a >= b | a.\_\_ge\_\_(b)
a == b | a.\_\_eq\_\_(b)
a != b | a.\_\_ne\_\_(b)
v in a | a.\_\_contains\_\_(v)
a[k] | a.\_\_getitem\_\_(k)
a[k] = v | a.\_\_setitem\_\_(k,v)
del a[k] | a.\_\_delitem\_\_(k)
a(arg1, arg2, ...) | a.\_\_call\_\_(arg1, arg2, ...)
len(a) | a.\_\_len\_\_()
hash(a) | a.\_\_hash\_\_()
iter(a) | a.\_\_iter\_\_()
next(a) | a.\_\_next\_\_()
bool(a) | a.\_\_bool\_\_()
float(a) | a.\_\_float\_\_()
int(a) | a.\_\_int\_\_()
repr(a) | a.\_\_repr\_\_()
reversed(a) | a.\_\_reversed\_\_()
str(a) | a.\_\_str\_\_()

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
- mechanism for a modular and **hierarchical organization**
- _base class, parent lcass, super class_ / __child class, subclass__ kind of relationship
- A **subclass** can **override** behabiors of the parent class, or it also can extend the base class by **adding new behaviors**
- An example is Python's exception classes **hierarchy** 

### 2.4.1 Example: PredatoryCreditCard class
![PredatoryCreditCard UML](PredatoryCreditCard.png)
```python
class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)"""

        super().__init__(customer, bank, acnt, limit) # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied."""

        success = super().charge(price) # call inherited method
        if not success:
            self._balance += 5 # assess penalty
        return success # caller expects return value

    def process_mont(self):    
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
        # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self. apr, 1/12)
            self._balance = monthly_factor
```

#### Protected Members
- In other languages, variables that are **nonpublic** can be difined as **private** or **protected**
  - **Protected** members can be accessed by subclasses and not by other classes, while **private** cannot be accessed by either.
- In python, variables that **_should be protected_** are defined with a *single underscore*, and those **which should** be private are defined with *double underscores*

### 2.4.2 Hierarchy of Numeric Progressions
![num progression](numeric_inheritance.png)
```python
class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self. current to a new value.

        This should be overridden by a subclass to customize progression.

        By convention, if current is set to None, this designates the
        end of a finite progression."""

        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None: # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current # record current value to return
            self._advance( ) # advance to prepare for next time
            return answer # return the answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def print_progression(self, n):
        """Print next n values of the progression."""
        print("".join(str(next(self)) for j in range(n)))
```
#### An arithmetic Progression
```python
class ArithmeticProgression(Progression): # inherit from Progression
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.

        increment the fixed constant to add to each term (default 1)
        start the first term of the progression (default 0)"""

        super().__init__(start) # initialize base class
        self._increment = increment

    def _advance(self): # override inherited version
        """Update current value by adding the fixed increment."""
        self._current += self. increment
```
#### A Geometric Progressio class
```python
class GeometricProgression(Progression): # inherit from Progression
    Iterator producing a geometric progression."""
    def __init__(self, base=2, start=1):
        """Create a new geometric progression.

        base the fixed constant multiplied to each term (default 2)
        start the first term of the progression (default 1)"""

        super().__init__(start)
        self._base = base

    def _advance(self): # override inherited version
        """Update current value by multiplying it by the base value."""
        rent = self._base
```

#### A Fibonacci Progression class
```python
class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""
    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression.

        first the first term of the progression (default 0)
        second the second term of the progression (default 1)"""

        super().__init__(first) # start progression at first
        self._prev = second − first # fictitious value preceding the first
        
    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current
```
#### Testing the progressions
```python
if name == __main__ :
    print( "Default progression:" )
    Progression( ).print_progression(10)
    print("Arithmetic progression with increment 5:" )
    ArithmeticProgression(5).print_progression(10)
    print( "Arithmetic progression with increment 5 and start 2:" )
    ArithmeticProgression(5, 2).print_progression(10)
    print( "Geometric progression with default base:" )
    GeometricProgression( ).print_progression(10)
    print( "Geometric progression with base 3:" )
    GeometricProgression(3).print_progression(10)
    print( "Fibonacci progression with default start values:" )
    FibonacciProgression( ).print_progression(10)
    print( "Fibonacci progression with start values 4 and 6:" )
    FibonacciProgression(4, 6).print_progression(10)
```

### 2.4.3 Abstract Base Classes
- **The only purpose of Abstract Base Classes is to serve as a base class through inheritance**
  - An abstract base class is one that **cannot be directly instantiated**, while a concrete
    class is one that **can be instantiated**
> In statically typed languages such as Java and C++, an abstract base class serves as a formal type that may guarantee one or more abstract methods. This provides support for polymorphism, as a variable may have an abstract base class as its declared type, even though it refers to an instance of a concrete subclass.

- Because of that, it is not very usual to define ABCs in Python

>`collections` module provides several abstract base classes that assist when defining custom data structures that share a common interface with some of Python’s built-in data structures. These rely on an object-oriented software design pattern known as the **template method pattern**. The template method pattern is when an abstract base class provides concrete behaviors that rely upon calls to other abstract behaviors. In that way, as soon as a subclass provides definitions for the **missing abstract behaviors**, the inherited concrete behaviors are well defined.

- For example, `collections.Sequence`
- Example based on `collections.Sequence`

```python
from abc import ABCMeta, abstractmethod # need these definitions

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def len (self):
        """Return the length of the sequence."""

    @abstractmethod
    def getitem (self, j):
        """Return the element at index j of the sequence."""

    def contains (self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val: # found match
                return True
        return False

    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val: # leftmost match
                return j
        raise ValueError( value not in sequence ) # never found a match

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val: # found a match
                k += 1
        return k
```

- We have defined `ABCMeta` as the **metaclass** of our class
  - A **metaclass** defines the template of the definition of a certain class. In this case, it establishes that the **constructor raises an error**.
- The `@abstractmethod` decorators declares the methods as **abstract**, which makes it compulsory to give an implementation of those methods in a subclass.
  - Otherwise, python does not allow the instatiation of a subclass without them

## 2.5 Namespaces and Object-Orientation

### 2.5.1 Instance and Class Namespaces
- A **namespace** is a "place" (abstract) where identifiers associated with certain values are managed in a certain scope.
- **Instance namespace**
- **Class namespace**, common to all instances
- The `self` keyword defines an identifier as an instance member
- To declare **class data members**, such as constants:

```python
class Proving:
    MY_CONSTANT = 1000

Proving.MY_CONSTANT # equals to 1000
```
- There is also the possibility to have **nested classes**

#### Dictionaries and the __slots__ declaration

>By default, Python represents each namespace with an instance of the built-in dict class (see Section 1.2.3) that maps identifying names in that scope to the associated objects.Python provides a more direct mechanism for representing instance namespaces that avoids the use of an auxiliary dictionary. To use the streamlined representation for all instances of a class, that class definition must provide a class-level member named slots that is assigned to a fixed sequence of strings that serve as names for instance variables. For example, with our CreditCard class, we would declare the following:

```py
class CreditCard:
    slots = "_customer" , "_bank" , "_account" , "_balance" , "_limit"
```

### 2.5.2 Name Resolution and Dynamic Dispatch
- When the dot operation is used as obj.foo, python searches:
    1. The **instance** namespace of `obj`
    2. The **class** namespace
    3. The **parent classes** namespaces
    4. If not found, `AttributeError` is raised

- The third point shows that if a function is called and it is present in the **subclass** and also in the **superclass**, python accesses the _lowest_ one, the one that **overrides** the other.
  - This is known as **dynamic dispatch**, and it refers to how pythons determines at **runtime** which function to call: the inherited or the overrider

## Shallow and Deep Copying
- When we have a list, and we want to modify a copy of it without actually modifying it, we can create a **shallow copy** of it
  - A **shallow copy** is a diferent list, but it still references to the same objects. That is `list1[j] is list2[j]` evaluates to `True`
  - A shallow copy can be made with `list(object)` or with python's `copy` module `copy(object)`
- A **deep copy**, instead, is a new list that has its own set of copied objects.
  - It is made with `copy.deepcopy(object)`