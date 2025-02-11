import numpy as np

# Creating 1D, 2D, and 3D arrays
arr1d = np.array([1, 2, 3, 4])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("1D Array:\n", arr1d)
print("2D Array:\n", arr2d)
print("3D Array:\n", arr3d)

# Checking data type, shape, and size
print("Array Type:", arr1d.dtype)
print("Array Shape:", arr2d.shape)
print("Array Size:", arr3d.size)
