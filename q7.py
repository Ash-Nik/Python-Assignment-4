# 6. Write a python program to evaluate the function sin(x) as defined by the infinite series expansion.
import math


def facto(x):
    if x == 1:
        return 1
    return x * facto(x - 1)


c = 1
x = int(input("Enter the value of x : "))
n = int(input("Enter the value of n : "))
k = 2
for i in range(1, n + 1):
    if i % 2 != 0:
        c -= int(math.pow(x, k)) / facto(k)
        k += 2
    else:
        c += int(math.pow(x, k)) / facto(k)
        k += 2
print(c)