def suma(first, secon, expected):
    if first + secon == expected:
        return '+'
    else:
        return False

def resta(first, secon, expected):
    if first - secon == expected:
        return '-'
    else:
        return False

def mult(first, secon, expected):
    if first * secon == expected:
        return '*'
    else:
        return False

def div(first, secon, expected):
    if first / secon == float(expected):
        return '/'
    else:
        return False

def pot(first, secon, expected):
    if first ** secon == expected:
        return '**'
    else:
        return False


def operating(first, second, result, order):
    operations = [suma, resta, mult, div, pot]
    for i in operations:
        oper = i(first, second, result)
        if oper:
            if not order:
                print(f"a {oper} b = c")
            else:
                print(f"a = b {oper} c")


while True:
    passing = False
    values = input("Insert values 'a b c':")
    a, b, c = list(int(i) for i in values.split(" "))
    operating(a, b, c, 0)
    operating(b, c, a, 1)


