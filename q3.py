# Write a python program to compute the sum of the first n terms (n>=1) of the series.
# S=1-3+5-7+9- ………
n = int(input("Enter the value of n : "))
s = 0
z = 1
for i in range(1, n + 1):
    if i % 2 != 0:
        s += z
        z += 2
    else:
        s -= z
        z += 2
print(s)
