# Program to Calculate the Sum of Numbers in a Given Range

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

sum = 0

for i in range(lower, upper + 1):
    if (i % 2 == 0):
        sum += i

print("Sum :", sum)
