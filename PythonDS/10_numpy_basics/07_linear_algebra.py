import numpy as np

# Matrix Multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = np.dot(A, B)
print("Matrix Multiplication:\n", result)

# Finding Determinant
det = np.linalg.det(A)
print("Determinant of A:", det)

# Inverse of a Matrix
inverse = np.linalg.inv(A)
print("Inverse of A:\n", inverse)
