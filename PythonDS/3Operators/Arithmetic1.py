#sum of two numbers

num1 = int(input("Enter the first number: ")) #variable read as integer
num2 = int(input("Enter the Second number: "))

sum = num1 + num2 # without int() ,it read as string - concatenation (1 + 2 -> 12)

print(num1,"+",num2,"=",sum)
