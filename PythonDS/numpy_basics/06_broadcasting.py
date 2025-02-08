import numpy as np

# Broadcasting with scalar
arr = np.array([1, 2, 3])
print("Array + 5:\n", arr + 5)

# Broadcasting with another array
arr2 = np.array([[1], [2], [3]])
arr3 = np.array([10, 20, 30])
print("Broadcasting Example:\n", arr2 + arr3)
