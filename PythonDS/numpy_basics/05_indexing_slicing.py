import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Indexing
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing
print("First 3 elements:", arr[:3])
print("Elements from index 2 to 4:", arr[2:5])

# 2D Array Slicing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("First row:", arr2d[0, :])
print("First column:", arr2d[:, 0])
