def factors(n):
    k = 1
    bigger = []
    while k * k < n:
        if not n % k:
            yield k
            bigger.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for i in bigger[::-1]:
        yield i

