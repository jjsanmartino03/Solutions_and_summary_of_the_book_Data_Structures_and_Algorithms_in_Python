import calc

num = ""
opers = ["+", "-", "*", "/", "**"]
complete = ""
ans = 0
print(
    "The only supported inputs that are not operators or numbers are: 'cls', 'ans' and '√'"
)
print(0)
while True:
    pressed = input("> ")
    if pressed == "cls":
        num = ""
        complete = 0
        ans = 0
        print(0)
        continue
    if pressed in opers:
        print(num)
        complete += num
        complete += pressed
        num = ""
    elif pressed == "=":
        complete += num
        ans = calc.start(complete, ans)
        print(ans)
        complete = ""
        num = ""
    else:
        num += pressed
        print(num)

