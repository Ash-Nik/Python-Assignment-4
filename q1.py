import math

x = int(input("Enter a number \n "))
for i in range(0, x + 1):
    print(i, "   ", int(math.pow(2, i)))
