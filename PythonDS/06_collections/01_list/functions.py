# List Operations: Sum, Min, Max, and Length

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum1 = 0

# Calculating sum using a loop
for i in list1:
    sum1 += i

print("Sum using For loop:", sum1)

# Using built-in sum() function
print("Sum using Function:", sum(list1))

# Finding largest and smallest elements in the list
print("Largest element in list:", max(list1))
print("Smallest element in list:", min(list1))

# Finding the length of the list
print("Total number of elements in list:", len(list1))

# Functions used in list
"""
1. sum(list)  : Returns the sum of elements in the list
2. max(list)  : Returns the largest element in the list
3. min(list)  : Returns the smallest element in the list
4. len(list)  : Returns the total number of elements in the list
"""
