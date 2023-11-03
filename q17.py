# 17. Write a python program called PrimeCounter that takes a command line
# argument N and finds the number of primes less than or equal to N.

def check_prime(x):
    z = 0
    for i in range(2, x):
        if x % i == 0:
            z += 1
    if z == 0:
        return f"{x} is prime"
    else:
        return "Not prime"


x = int(input("Enter a number = "))
for i in range(2, x + 1):
    print(check_prime(i))
