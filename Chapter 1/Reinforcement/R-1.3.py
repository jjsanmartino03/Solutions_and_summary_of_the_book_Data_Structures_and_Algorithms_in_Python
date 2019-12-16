def minmax(data):
    maxie, minie = data[0], data[0]
    for i in data:
        maxie = i if i > maxie else maxie
        minie = i if i < minie else minie
    return minie, maxie
