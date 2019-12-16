def square_of_odds(n):
    return sum(x**2 for x in range(1, n) if x % 2)


print(square_of_odds(55))
