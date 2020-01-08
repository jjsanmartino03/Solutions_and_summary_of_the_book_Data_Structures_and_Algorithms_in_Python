"""
P-1.33 
Write a Python program that simulates a handheld calculator. Your pro
gram should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each 
operation is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
"""

import calc

num = ""
opers = ["+", "-", "*", "/", "**"]
complete = ""
ans = 0
print(
    "The only supported inputs that are not operators or numbers are: 'off', 'cls', 'ans' and '√'"
)
print(0)
while True:
    pressed = input("> ")
    if pressed == "off":
        break
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

