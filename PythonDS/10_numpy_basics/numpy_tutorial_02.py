import numpy as np

# --------------------
# 1. Creating Arrays
# --------------------
a = np.arange(1, 11)
b = np.linspace(10, 50, 5)
c = np.array([1, 23, 5, 2, 9, 57, 24, 50])

d = np.array([[1, 3, 4], [5, 6, 7], [3, 4, 5]])
e = np.array([[3, 5, 6], [1, 2, 3], [5, 6, 7]])

# --------------------------
# 2. Arithmetic Operations
# --------------------------
print(np.add(d, e))
print(np.subtract(d, e))
print(np.multiply(d, e))
print(np.divide(d, e))
print(np.square(d))
print(np.sqrt(d))

# --------------------------
# 3. Reshaping Arrays
# --------------------------
a = np.arange(1, 26).reshape([5, 5])
b = np.arange(5, 51, 5).reshape([2, 5])
c = a.flatten()
d = a.ravel()
e = np.expand_dims(a, axis=0)
f = np.squeeze(e)

g = np.transpose(a)
h = np.swapaxes(a, 0, 1)

# -------------------------------------
# 4. Concatenation and Splitting
# -------------------------------------
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
c = np.concatenate((a, b), axis=0)
d = np.hstack((a, b.T))
e = np.vsplit(a, 2)

# --------------------------
# 5. Boolean Masking
# --------------------------
a = np.array([1, 23, 5, 2, 9, 57, 24, 50])
b = np.where(a > 9)
c = np.nonzero(a)
d = np.isin(a, [2, 5, 50])

e = np.any(a > 30)
f = np.all(a > 0)

# --------------------------
# 6. Statistical Functions
# --------------------------
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.var(a))
print(np.percentile(a, 50))
print(np.corrcoef(a))

# --------------------------
# 7. Logical & Comparison
# --------------------------
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
print(np.greater(a, b))
print(np.less(a, b))
print(np.equal(a, b))
print(np.logical_and(a > 2, b < 4))
print(np.logical_or(a > 2, b < 4))
print(np.logical_not(a > 2))

# --------------------------
# 8. Random Operations
# --------------------------
np.random.seed(42)
a = np.random.randint(1, 100, 10)
b = np.random.uniform(0, 1, 10)
c = np.random.choice(a, 5)
np.random.shuffle(a)

# --------------------------
# 9. Linear Algebra
# --------------------------
a = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(a))
print(np.linalg.det(a))
print(np.linalg.eig(a))
b = np.array([5, 6])
print(np.linalg.solve(a, b))
print(np.linalg.norm(a))

# --------------------------
# 10. Set Operations
# --------------------------
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])
print(np.unique(a))
print(np.intersect1d(a, b))
print(np.union1d(a, b))
print(np.setdiff1d(a, b))
print(np.setxor1d(a, b))
