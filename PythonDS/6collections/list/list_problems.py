# Problem 1: List Indexing and Addition
print("Problem 1")
lst = [15, 20, 25, 30, 35, 40, 50]
print(lst[-2] + lst[0] + lst[1])  # lst[-0] is same as lst[0]
print()

# Problem 2: Compute difference between sum of list and each element
print("Problem 2")
lst = [15, 3, 10, 6, 9, 7]
result = sum(lst)  # Total sum of list elements
lst1 = [result - i for i in lst]  # Subtract each element from sum
print(lst1)
print()

# Problem 3: Find peaks and valleys in a list
print("Problem 3")
lst = [1, 3, 8, 6, 5, 3, 2, 4, 6, 8, 9, 7, 5, 4, 8, 9, 12]
lst1 = []

# Identifying peaks and valleys in the list
for i in range(1, len(lst) - 1):  # Start from index 1 to avoid out-of-bounds errors
    if (lst[i - 1] < lst[i] > lst[i + 1]) or (lst[i - 1] > lst[i] < lst[i + 1]):
        lst1.append(lst[i])

print(lst1)
