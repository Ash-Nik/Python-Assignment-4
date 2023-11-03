# Write a python program that displays all the numbers from 100 to 1,000, ten per line, that are
# divisible by 5 and 6. Numbers are separated by exactly one space

c = 1
for i in range(100, 1000):
    if i % 5 == 0 and i % 6 == 0:
        if c % 10 == 0:
            print()
        c += 1

        print(i, " ", end=" ")
