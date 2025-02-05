#Lambda function

"""
It is an anonymous function (which doesn't have any name)
Can reduce the length of function

syntax:
variable = lambda num1,num2 : num1+num2

"""

#Add 2 numbers
add=lambda num1,num2:num1+num2
print(add(10,20))


#Multiplication of 3 numbers
mul=lambda num1,num2,num3:num1*num2*num3
print(mul(10,2,3))

#Cube of a number
cube=lambda num:num**3
print(cube(3))