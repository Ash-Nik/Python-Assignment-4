# Input a number n, write a python program to compute n factorial (written as n!) where n>=0.
n = int(input("Plz enter the number : "))
facto = 1
for i in range(1, n + 1):
    facto *= i
print(facto)
