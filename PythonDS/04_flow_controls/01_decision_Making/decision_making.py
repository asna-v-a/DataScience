# Decision-Making: Making decisions based on the condition/criteria passed in program
"""
1.if
2.if....else
3.if....elif....else
"""
    
# 1. if: checks only 1 condition
# Syntax:
# if(condition):
#     statements
num = 10
if num > 5:
    print("num is greater than 5")



# 2. if...else: checks 1 condition, and executes else block if condition is false
# Syntax:
# if(condition):
#     statements
# else:
#     statements
num = 3
if num > 5:
    print("num is greater than 5")
else:
    print("num is less than or equal to 5")



# 3. if...elif...else: checks more than 1 condition
# Syntax:
# if(condition1):
#     statements
# elif(condition2):
#     statements
# elif(condition3):
#     statements
# .
# .
# .
# else:
#     statements
num = 7
if num > 10:
    print("num is greater than 10")
elif num > 5:
    print("num is greater than 5 but less than or equal to 10")
else:
    print("num is less than or equal to 5")
