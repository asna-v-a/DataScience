#Second-largest number

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


if(num1 > num2) & (num1 < num3) or (num1 < num2) & (num1 > num3) :
    print("Second largest number: ",num1)
elif(num2 > num1) & (num2 < num3) or (num2 < num1) & (num2 > num3):
    print("Second largest number: ", num2)
else:
    print("Second largest number: ", num3)


