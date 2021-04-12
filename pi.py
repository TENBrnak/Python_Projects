# this should calculate pi
pi = 4
value1 = 3
counter = 0
plusminus = 2
num = int(input("input number"))

while counter <= 10**num:  # the Liebniz series
    if (plusminus % 2) == 0:
        pi = pi - (4 / value1)
        plusminus = plusminus - 1
    else:
        pi = pi + (4 / value1)
        plusminus = plusminus + 1
    value1 = value1 + 2
    counter = counter + 1
    print(pi)
print("Final value by using 10**", num, "is", pi, "sequence end", plusminus)
input()
