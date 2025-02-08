import numpy as np
import time

# Comparing NumPy array with Python list
size = 10**6
py_list = list(range(size))
np_array = np.arange(size)

# Python list time
start = time.time()
py_sum = sum(py_list)
end = time.time()
print("Python list sum time:", end - start)

# NumPy array time
start = time.time()
np_sum = np.sum(np_array)
end = time.time()
print("NumPy array sum time:", end - start)

# Vectorization example
A = np.random.rand(1000, 1000)
B = np.random.rand(1000, 1000)

start = time.time()
result = A @ B  # Faster than nested loops
end = time.time()
print("Matrix multiplication time:", end - start)
