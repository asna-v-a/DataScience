# Largest number among 3 numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if (num1 > num2) & (num1 > num3):  # The '&' operator is used to combine conditions. It works as a logical AND.
    print(num1,"is greater than",num2,"and",num3)
elif num2 > num3:
    print(num2,"is greater than",num1,"and",num3)
else:
    print(num3,"is greater than",num1,"and",num2)
