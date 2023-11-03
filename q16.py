# 16. Write a python program to check a number n is prime or not.
# The number to be inputted through keyboard

n = int(input("Please enter a number : "))
z=0
for i in range (2,n):
    if n%i==0:
        z+=1
if z==0:
    print("Number is a prime number ")
else:
    print("Number is not a prime number ")