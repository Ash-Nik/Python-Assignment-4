# 6. Write a python program to evaluate the function sin(x) as defined by the infinite series expansion.
import math


def facto(x):
    if x == 1:
        return 1
    return x * facto(x - 1)


s = 0
x = int(input("Enter the value of x : "))
n = int(input("Enter the value of n : "))
k = 1
for i in range(1, n + 1):
    if i % 2 != 0:
        s += int(math.pow(x, k)) / facto(k)
        k += 2
    else:
        s -= int(math.pow(x, k)) / facto(k)
        k += 2
print(s)