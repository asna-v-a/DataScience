# Jumping statements
"""
1. break - Exits the loop immediately when the condition is met.
2. continue - Skips the rest of the current iteration and continues with the next iteration of the loop.
3. pass - Does nothing and continues with the next iteration without skipping or breaking the loop.
"""

# break - To exit the loop when a certain condition is met
# Example: Break the loop when i reaches 25
for i in range(1, 51):
    if i == 25:
        break  # Exit the loop when i equals 25
    print(i, end=' ')
print()  # This will print numbers from 1 to 24


# continue - Skip the current iteration and continue to the next one
# Example: Skip the number 25 and continue the loop
for i in range(1, 51):
    if i == 25:
        continue  # Skip the iteration when i equals 25
    print(i, end=' ')
print()  # This will print numbers from 1 to 49 except 25


# pass - Do nothing and continue the loop
# Example: No operation is performed when i equals 25
for i in range(1, 51):
    if i == 25:
        pass  # Do nothing when i equals 25
    print(i, end=' ')# This will print numbers from 1 to 50 without any change, as pass does not affect the loop
