import numpy as np

# arange -> To get values within a range
a = np.arange(1, 11)
print(a)

a = np.arange(1, 31, 3)  # start, stop, step
print(a)

print("\nTwo Dimension")
a = np.arange(1, 26).reshape([5, 5])
print(a)
print()

a = np.arange(5, 51, 5).reshape([2, 5])
print(a)

# Arithmetic operations : order of the matrices should be same, else error
a = np.array([[1, 3, 4], [5, 6, 7], [3, 4, 5]])
b = np.array([[3, 5, 6], [1, 2, 3], [5, 6, 7]])

# Addition
c = np.add(a, b)
print(c)

# Subtraction
d = np.subtract(a, b)
print(d)

# Multiplication
e = np.multiply(a, b)
print(e)

# Division
f = np.divide(a, b)
print(f)

# Square
g = np.square(a)
print(g)

# Square root
h = np.sqrt(a)
print(h)

# Splitting arrays
a = np.array([1, 23, 5, 2, 9, 57, 24, 50])
b = np.array_split(a, 4)  # 4: no of arrays to split
print(b)

# Dot Product
# One dimension
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.dot(a, b)
print(c)

# Two dimension
d = np.array([[1, 3, 4], [5, 6, 7], [3, 4, 5]])
e = np.array([[3, 5, 6], [1, 2, 3], [5, 6, 4]])
f = np.dot(d, e)
print(f)

# linspace : equally divide from start to stop with step no of elements
a = np.linspace(10, 50, 5)
print(a)

a = np.linspace(10, 50, 10)
print(a)

# Finding max value & index
a = np.array([1, 23, 5, 2, 9, 57, 24, 50])
print(np.max(a))
print(np.argmax(a))

a = np.array([[1, 14, 5], [2, 23, 15], [23, 47, 60]])
print(np.max(a))
print(np.argmax(a))
print(np.max(a, axis=1))
print(np.argmax(a, axis=1))
print(np.max(a, axis=0))
print(np.argmax(a, axis=0))

# Finding min value & index
print(np.min(a))
print(np.argmin(a))
print(np.min(a, axis=1))
print(np.argmin(a, axis=1))
print(np.min(a, axis=0))
print(np.argmin(a, axis=0))

# Indexing and Slicing
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a[3])
print(a[3:7])
print(a[3:])
print(a[:7])
print(a[2:7:2])
print(a[2::3])
print(a[::3])
print(a[::-1])

b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 1], [2, 4, 1, 3, 5], [3, 8, 6, 9, 2]])
print("\nTwo Dimension")
print(b[2:, :3])
print(b[:2, 1:3])
print(b[1:3, 2:4])
print(b[1:4:2, 2::2])
print(b[::2, ::3])
print(b[2, 3])
print(b[0, :])
print(b[:, 0])

# Sorting
# One dimension
a = np.array([5, 1, 2, 6, 4, 3, 1, 6, 4, 2, 3, 5])
print(np.sort(a))
print(np.sort(a)[::-1])
print(np.argsort(a))

# Two dimension
d = np.array([[1, 3, 4, 2, 2], [5, 8, 6, 7, 1], [1, 3, 4, 5, 0], [5, 7, 6, 3, 4]])
print(np.sort(d))
print(np.sort(d, axis=0))
print(np.argsort(d))
print(np.argsort(d, axis=0))

# Summation
a = np.array([1, 2, 3])
print(np.sum(a))

c = np.array([[1, 3, 4, 1], [5, 6, 7, 2], [3, 4, 5, 1], [1, 2, 3, 4]])
print(np.sum(c))
print(np.sum(c, axis=0))
print(np.sum(c, axis=1))

# where condition
a = np.array([1, 23, 5, 2, 9, 57, 24, 50])
print(np.where(a > 9))

a = np.array([[1, 14, 5], [2, 23, 15], [23, 47, 60]])
print(np.where(a > 9))
