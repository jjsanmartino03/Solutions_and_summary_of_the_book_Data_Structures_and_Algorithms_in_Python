def all_dif(data):
    for i in data:
        data.remove(data[0])
        for j in data:
            if i == j:
                return False
    return True


print(all_dif([1, 2, 5, 78]))

