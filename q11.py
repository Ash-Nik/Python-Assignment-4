# 11. Write a python program that accepts a positive integer n and reverses the order of its digits.
n = int(input("Please enter a number  : "))
x = 0
while n != 0:
    x = x * 10 + (n % 10)
    n //= 10
print(x)