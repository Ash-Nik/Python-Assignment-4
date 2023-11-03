def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is", result)
