#No, it does not work because you are only multiplying a value
# by a number, but you are not assigning the product to a
# variable or a part of a list
def scale(data, factor):
    for val in data:
        val *= factor
    print(data)

scale([2, 3, 6], 5)