# Your program should handle for all positive values of n.
# Example: If n=1, it will display as: Fibonacci Series is: 0
# If n=2, it will display as: Fibonacci Series is: 0, 1
# If n=3, it will display as: Fibonacci Series is: 0, 1, 1 ….
# If n=10, it will display as: Fibonacci Series is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

n = int(input("Enter the number of terms : "))
if n == 1:
    print(0)
elif n == 2:
    print(0, 1)
else:
    a = 0
    b = 1
    print(0, end="")
    for i in range(1, n ):
        c = a + b
        print("   ", c, " ", end="")
        b = a
        a = c

