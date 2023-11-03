# For a given x and a given n, write a python program to compute
# x^n/n!
import math


def facto(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


x = int(input("Plz enter the value of x  : "))
n = int(input("Enter the value of n : "))
print(int(math.pow(x, n)) / facto(n))
