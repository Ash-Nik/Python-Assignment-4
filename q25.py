# 25. A perfect number is one whose divisors add up to the number.
# Example: The first perfect number is 6. because 1, 2, and 3 are its proper divisors, and 1+2+3=6
# Write a python program that prints all perfect numbers in between 1 and 500
def isPerfect(n):
    l = []
    l2 = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            l.append(i)
    a = 0
    for i in l:
        a += i
    if a == n:
        l2.append(a)
    return l2


for i in range(1, 500):
    k = isPerfect(i)
    if len(k) != 0:
        print(k[0])
