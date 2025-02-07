# For Loop - Used for iterating over a sequence (range, list, string, etc.)

# Syntax 1: Iterating with default step (increment by 1)
# for i in range(start, end):  # Loop runs from 'start' to 'end-1', incrementing by 1
for i in range(1, 5):  # Loop runs from 1 to 4
    print(i)

print()

# Syntax 2: Iterating with a custom step
# for i in range(start, end, step):  # Loop runs from 'start' to 'end-1' with the specified 'step'
for i in range(1, 10, 2):  # Loop runs from 1 to 9 with a step of 2
    print(i)

print()

# Syntax 3: Iterating in reverse order using a negative step
# for i in range(start, end, -step):  # Loop runs from 'start' to 'end+1', decrementing by 'step'
for i in range(10, 0, -2):  # Loop runs from 10 to 2 with a step of -2
    print(i)

