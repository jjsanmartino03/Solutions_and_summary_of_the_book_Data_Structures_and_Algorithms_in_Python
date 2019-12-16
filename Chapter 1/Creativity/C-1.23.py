test = [1, 2, 3, 4]
try:
    print(test[34])
except IndexError:
    print("Don’t try buffer overflow attacks in Python!")
