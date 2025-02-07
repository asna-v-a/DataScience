#Number divisible by 5 between lower and upper

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

while (lower_limit <= upper_limit):
    if (lower_limit % 5 == 0):
        print(lower_limit,end=" ")
    lower_limit += 1
