"""
Dictionary Comprehension

1. Extract keys from a dictionary based on a condition.
2. `dic[i] > 2500` filters items where the value is greater than 2500.
3. `i for i in dic` extracts only the keys that satisfy the condition.

"""

dic = {'bike': 350, 'car': 2500, 'jeep': 3000, 'bus': 8000, 'van': 3000}

# Extract vehicle names with a value greater than 2500
lst = [i for i in dic if dic[i] > 2500]
print(lst)  # Output: ['jeep', 'bus', 'van']
