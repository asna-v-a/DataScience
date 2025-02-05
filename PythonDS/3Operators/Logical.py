#Logical Operators
"""
1.AND - & (ampersand)
2.OR - | (pipe symbol)
3.XOR - ^ (Cap symbol)


AND - all conditions should be True
Input    Output
 0 0       0
 0 1       0
 1 0       0
 1 1       1


OR - any of the conditions should be True
Input    Output
 0 0       0
 0 1       1
 1 0       1
 1 1       1


XOR - gives True when both conditions are different and False when both conditions are same
Input    Output
 0 0       0
 0 1       1
 1 0       1
 1 1       0
 
 """

#Example
num1 = 2
num2 = 4
print(num1&num2)# gives 0 - Binary operation

num3 = 4
num4 = 4
print(num3&num4)# gives 4 - Binary operation
