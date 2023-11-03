# 20. For some integer n, write a python program to find the largest factorial
# number present as factor in n.

n = int(input("Enter the number : "))
x = 2
k = 0
while n != 1:
    if n % x == 0:
        # print(x)
        n/=x
        k=x
    else:
        x += 1
print(k)