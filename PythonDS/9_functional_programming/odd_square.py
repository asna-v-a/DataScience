lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter to get odd numbers
f1 = list(filter(lambda num: num % 2, lst))

# Using map to square the filtered odd numbers
f2 = list(map(lambda num: num ** 2, f1))
print(f2)  # Output: [1, 9, 25, 49, 81]

# Combining filter and map in one step
f = list(map(lambda num: num ** 2, filter(lambda num: num % 2, lst)))
print(f)  # Output: [1, 9, 25, 49, 81]