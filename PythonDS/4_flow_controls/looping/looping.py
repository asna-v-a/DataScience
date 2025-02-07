# Looping - checking a condition or executing a statement continuously

"""
Two types of loops:
1. while loop
2. for loop

Basic structure of a loop:
1. Initialization - Defines the starting point of the loop.
2. Condition - Specifies when the loop should stop.
3. Increment or Decrement - Controls the loop progression to avoid infinite looping.

"""

# Example of a while loop:
i = 1  # Initialization
while i <= 5:  # Condition
    print(i, end=" ")  # Statement inside the loop
    i += 1  # Increment to progress the loop
print()

# Example of a for loop:
for i in range(1, 6):  # Initialization, Condition, and Increment handled by range()
    print(i, end=" ")  # Statement inside the loop
