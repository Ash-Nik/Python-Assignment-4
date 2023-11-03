import math


def facto(x):
    if x == 1:
        return 1
    return x * facto(x - 1)


c = 1
x = int(input("Enter the value of x : "))
n = int(input("Enter the value of n : "))
k = 1
for i in range(1, n + 1):
    c += int(math.pow(x, k)) / facto(k)
    k += 1

print(c)
