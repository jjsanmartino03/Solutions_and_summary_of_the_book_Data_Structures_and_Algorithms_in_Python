def norm(v, p=2):
    discriminer = sum(i**p for i in v)
    for i in range(discriminer):
        if i ** p == discriminer:
            return i
    return False


print(norm([2], 3))




