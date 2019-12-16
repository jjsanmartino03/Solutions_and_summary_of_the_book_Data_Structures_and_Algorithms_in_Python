a = []
while True:
    try:
        a.append(input())
    except EOFError:
        break

a.reverse()
for i in a:
    print(i)