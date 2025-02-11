# Function Definitions
def add(num1, num2):
    sum = num1 + num2
    return sum


def sub(num1, num2):
    sub = num1 - num2
    return sub


def mul(num1, num2):
    mul = num1 * num2
    return mul


def div(num1, num2):
    div = num1 / num2
    return div


print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
choice=1

while(choice>0):
    if choice > 0 and choice < 5:
        choice = int(input("Enter your choice:"))
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if choice == 1:
            result = add(num1, num2)
            print(num1, "+", num2, "=", result)
        elif choice == 2:
            result = sub(num1, num2)
            print(num1, "-", num2, "=", result)
        elif choice == 3:
            result = mul(num1, num2)
            print(num1, "*", num2, "=", result)
        elif choice==4:
            if num2 != 0:
                result = div(num1, num2)
                print(num1, "/", num2, "=", result)
            else:
                print("A number can't be divided by 0")
        else:
            choice=0

    else:
        print("Invalid choice")



# if choice > 0 and choice < 5:
#
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#
#     if choice == 1:
#         result = add(num1, num2)
#         print(num1, "+", num2, "=", result)
#     elif choice == 2:
#         result = sub(num1, num2)
#         print(num1, "-", num2, "=", result)
#     elif choice == 3:
#         result = mul(num1, num2)
#         print(num1, "*", num2, "=", result)
#     else:
#         if num2 != 0:
#             result = div(num1, num2)
#             print(num1, "/", num2, "=", result)
#         else:
#             print("A number can't be divided by 0")
# else:
#     print("Invalid choice")
#