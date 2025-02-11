#Sum of Odd numbers between lower limit and upper limit

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

sum = 0
while (lower_limit <= upper_limit):
    if (lower_limit % 2 == 1):
        sum += lower_limit
    lower_limit += 1
print("Odd Sum:",sum)
