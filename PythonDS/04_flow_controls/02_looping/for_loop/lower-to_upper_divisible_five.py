# Program to Find the Sum of Multiples of 5 in a Given Range

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

sum = 0

for i in range(lower, upper + 1):
    if (i % 5 == 0):
        sum += i

print("Sum: ", sum)
