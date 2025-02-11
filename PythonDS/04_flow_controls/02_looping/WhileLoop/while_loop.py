# While loop: executes a block of code repeatedly as long as the given condition is True.

"""
It is commonly used when the number of iterations is not known in advance.

Syntax:
while condition:  # The loop runs as long as 'condition' is True
    statement(s)  # Code to be executed inside the loop
    
"""

# Example:
i = 1  # Initialization
while i <= 10:  # Condition to check
    print(i, end=" ")  # Statement executed in each iteration
    i += 1  # Increment to avoid infinite loop
