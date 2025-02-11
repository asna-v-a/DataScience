# Program to Print All Odd Numbers in a Given Range

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

for i in range(lower, upper + 1):
    if (i % 2 == 1):
        print(i, end=" ")
