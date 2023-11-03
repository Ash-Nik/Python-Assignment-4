# 14. Write a python program that reads an integer and displays all its smallest factors in increasing
# order. For example, if the input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.


n = int(input("Enter the number : "))
x = 2
while n != 1:
    if n % x == 0:
        print(x)
        n/=x
    else:
        x += 1
