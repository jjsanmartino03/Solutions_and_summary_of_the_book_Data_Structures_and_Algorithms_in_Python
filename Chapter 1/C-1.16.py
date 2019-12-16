#It is possible because the parameter is a mutable object,
# a list with values.
def prove(inpud):
    for i in range(len(inpud)):
        inpud[i] += 5
    print(inpud)


ab = [5, 6, 7]
prove(ab)
print(ab)