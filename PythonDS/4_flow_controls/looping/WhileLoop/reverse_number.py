#Reverse a Number

num = int(input("Enter the number: "))

length = len(str(num))
rev = 0
rem = 0
while (num != 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
print("Reversed number:", rev)
