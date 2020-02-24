"""
C-1.26 Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
"""

def add_operation(first, second, expected):
    if first + second == expected:
        return '+'
    else:
        return False

def substraction(first, second, expected):
    if first - second == expected:
        return '-'
    else:
        return False

def mult(first, second, expected):
    if first * second == expected:
        return '*'
    else:
        return False

def div(first, second, expected):
    if first / second == float(expected):
        return '/'
    else:
        return False

def pot(first, second, expected):
    if first ** second == expected:
        return '**'
    else:
        return False


def operating(first, second, result, order):
    operations = [add_operation, substraction, mult, div, pot]
    for function in operations:
        oper = function(first, second, result)
        if oper:
            if not order:
                print(f"a {oper} b = c")
            else:
                print(f"a = b {oper} c")


values = input("Insert values 'a b c':")
a, b, c = list(int(i) for i in values.split(" "))
operating(a, b, c, 0)
operating(b, c, a, 1)


