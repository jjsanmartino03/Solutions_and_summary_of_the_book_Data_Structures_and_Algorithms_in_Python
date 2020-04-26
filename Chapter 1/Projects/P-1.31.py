"""
P-1.31 
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
"""

"""I chose the American currency: $1, $2, $5, $10, $20, $50, and $100; 
1¢, 5¢, 10¢, 25¢, 50¢, and $1"""

currencies = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
while True:
    charge = float(input("Write the amount charged: $"))
    given = float(input("Write the amount given: $"))
    change_amount = given - charge
    already = 0
    unity_times = {}
    for i in currencies:
        unity_times[i] = 0
        while True:
            if i + already > change_amount:
                break
            else:
                already += i
                unity_times[i] += 1
    print(f"Total change: ${already}")
    print("Bills and coins:")
    for i in unity_times:
        if unity_times[i]:
            print(i, unity_times[i], sep=" --> ")
