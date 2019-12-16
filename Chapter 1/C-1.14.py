def find_odd_products(data):
    for i in data:
        for j in data:
            if j != i:
                if (j*i) % 2:
                    return True
    return False


print(find_odd_products([2, 4]))

