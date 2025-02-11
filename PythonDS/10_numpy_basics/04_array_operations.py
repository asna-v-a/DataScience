import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Basic mathematical operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Standard Deviation:", np.std(arr))

# Element-wise operations
arr2 = np.array([10, 20, 30, 40, 50])
print("Addition:", arr + arr2)
print("Multiplication:", arr * arr2)
