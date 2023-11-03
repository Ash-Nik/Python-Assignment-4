# 22. Write a python program that reads in a set of n single digits and converts them into a single
# decimal integer. For example, the program should convert the set of 5 digits {2, 7, 4, 9, 3} to the
# integer 27493.

x=[2,7,4,9,3]
k=0
for n in x :
    k=k*10+n
print(k)