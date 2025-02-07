# List Operations: append(), extend(), insert()

lst = [1, 4, 6, 7, 8]

# append() - Adds a single element to the end of the list
lst.append(30)

# extend() - Adds multiple elements to the list
lst.extend([15, 20, 25, 30])

# insert() - Inserts an element at a specified index
lst.insert(1, 3)  # Inserts 3 at index 1

# Printing the final list after modifications
print(lst)

"""
Summary of List Methods:
1. append(value)  -> Adds a single element at the end.
2. extend(iterable)  -> Adds multiple elements from an iterable (e.g., list).
3. insert(index, value)  -> Inserts an element at the specified index.
"""
