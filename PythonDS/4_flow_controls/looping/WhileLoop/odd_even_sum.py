#Sum of Odd and Even Numbers in a range

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

odd_sum = 0
even_sum = 0

while (lower_limit <= upper_limit):
    if (lower_limit % 2 == 0):
        even_sum += lower_limit
    else:
        odd_sum += lower_limit
    lower_limit+=1

print("Odd sum:", odd_sum)
print("Even sum:", even_sum)
