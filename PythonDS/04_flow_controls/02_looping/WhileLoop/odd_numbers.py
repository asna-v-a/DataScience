#Odd numbers between lower limit and upper limit

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

while (lower_limit <= upper_limit):
    if (lower_limit % 2 == 1):
        print(lower_limit)
    lower_limit += 1
