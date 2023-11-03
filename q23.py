# 23. Input an integer n. Write a python program that will find the smallest
# exact divisor other than one.


n = int(input("Enter the number : "))
x = 2
k = 0
while n != 1:
    if n % x == 0:
        n /= x
        k = x
        break
    else:
        x += 1
print(k)
