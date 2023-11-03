#  Amicable numbers are pair of numbers each of whose divisors add to the other number.
# Example: The smallest pair of amicable numbers is (220, 284). They are amicable because the
# proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110, of which the sum is 284; and
# the proper divisors of 284 are 1, 2, 4, 71 and 142, of which the sum is 220.
# Note: 1 is included as a divisor but the numbers are not included as their own divisors.
# Write a python program that tests whether a given pair of numbers is amicable numbers or not.

def isAmicable(n, n2):
    l = []
    l2 = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            l.append(i)

    for i in range(1, (n2 // 2) + 1):
        if n2 % i == 0:
            l2.append(i)
    a, b = 0, 0
    for i in l:
        a += i
    for i in l2:
        b += i
    if a == n2 and b == n:
        return True
    else:
        return False


n = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
if(isAmicable(n,n2)):
    print(n," ",n2 ,"is Amicable")
else:
    print(n, " ", n2, "is not Amicable")
