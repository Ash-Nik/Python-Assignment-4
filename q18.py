# Write a python program to generate the first n terms of the sequence without using multiplication.
# 1 2 4 8 16 32 ………
import math

n = int(input("Enter the number : "))
for i in range(0, n):
    print(int(math.pow(2, i)),"   ",end="")
