import numpy as np

# Generating random numbers
rand_nums = np.random.rand(5)
print("Random numbers between 0 and 1:", rand_nums)

# Generating random integers
rand_ints = np.random.randint(1, 100, size=(3, 3))
print("Random integers:\n", rand_ints)

# Normal distribution
rand_normal = np.random.normal(0, 1, 5)
print("Random normal distribution:", rand_normal)
