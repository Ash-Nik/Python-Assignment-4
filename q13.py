# Write a python program that puts the binary representation
# of a positive integer N into a String s.
def decimal_to_binary(x):
    if x == 1:
        return x
    return decimal_to_binary(x // 2) * 10 + x % 2


n = int(input("Please enter a number : "))
s = str(decimal_to_binary(n))
print(s, type(s))
