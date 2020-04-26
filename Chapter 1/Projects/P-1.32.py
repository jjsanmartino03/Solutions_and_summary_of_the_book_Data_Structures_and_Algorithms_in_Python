"""
P-1.32 
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
"""
import calc  # This is an inline calculator I had already programmed
#My version works more like a scientific calculator than a simple calculator

complete = ""
ans = 0
print("To exit the calculator write 'quit()'")
print("The unique word available is 'ans'")
while True:
    a = input()
    if a == "quit()":
        break
    if a == "=":
        ans = calc.start(complete, ans)
        print(ans)
        complete = ""
    else:
        complete += a
        print(complete)

