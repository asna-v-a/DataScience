# Function to add two numbers with argument and return type

def add(num1,num2):
    sum = num1+num2
    return sum
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

data=add(num1,num2)
print("Sum:",data)