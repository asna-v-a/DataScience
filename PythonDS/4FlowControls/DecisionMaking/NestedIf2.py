#Second-largest number

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if(num1 > num2)&(num1>num3):
    if(num2 > num3):
        print("Second largest number:",num2)
    else:
        print("Second largest number:", num3)

elif(num2 > num1)&(num2>num3):
    if(num1 > num3):
        print("Second largest number:",num1)
    else:
        print("Second largest number:", num3)

elif(num3 > num1)&(num3>num2):
    if(num1 > num2):
        print("Second largest number:",num1)
    else:
        print("Second largest number:", num2)

else:
    print("Invalid")