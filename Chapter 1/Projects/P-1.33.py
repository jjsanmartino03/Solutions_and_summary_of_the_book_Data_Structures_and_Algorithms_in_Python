"""
P-1.33 
Write a Python program that simulates a handheld calculator. Your pro
gram should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each 
operation is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
"""


def start_handheld_calculator():
    opers = ["+", "-", "*", "/", "**"]
    cur_oper = ""
    current = ""
    inp = input()

    while inp != "esc":

        if inp not in opers:

            if inp.isdigit() and cur_oper:
                current += inp
                print(current)

            elif inp == "." and "." not in current and cur_oper:
                current += inp
                print(current)

            elif (inp.isdigit() or inp == ".") and not cur_oper:
                current = inp

            elif inp == "cls":
                current = ""
                result = 0
                cur_oper = ""
                print(0)

            elif inp == "=":
                result = eval(f"{result}{cur_oper}{current}")
                cur_oper = ""
                print(result)
                current = result

            else:
                print("Syntax Error, values resetted to 0")
                result = 0
                current = ""
        else:
            if cur_oper and inp in "+-" and not current:
                current += inp
                print(current)

            elif not cur_oper:
                cur_oper = inp
                result, current = current, ""

            else:
                bef_oper, cur_oper = cur_oper, inp

                result = eval(f"{result}{bef_oper}{current}")
                bef_oper = ""
                print(result)

                current = ""
        inp = input()


start_handheld_calculator()
