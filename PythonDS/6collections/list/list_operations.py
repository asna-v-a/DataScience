# Python List Operations - Complete Guide

# 1️ Creating Lists
lst = [1, 2, 3, 4, 5]
empty_lst = []  # Empty list
nested_lst = [[1, 2], [3, 4]]  # Nested list

# 2️ Adding Elements
lst.append(6)               # Adds a single element
lst.extend([7, 8, 9])       # Adds multiple elements
lst.insert(2, 10)           # Inserts 10 at index 2

# 3️ Removing Elements
lst.remove(3)               # Removes first occurrence of 3
lst.pop()                   # Removes last element
lst.pop(1)                  # Removes element at index 1
del lst[0]                  # Deletes first element
lst.clear()                 # Removes all elements

# 4️ Accessing Elements
lst = [1, 2, 3, 4, 5]
print(lst[0])               # First element
print(lst[-1])              # Last element
print(lst[1:4])             # Slicing (index 1 to 3)

# 5️ Searching
print(5 in lst)             # Check if 5 exists
print(lst.index(5))         # Index of 5

# 6️ Sorting and Reversing
lst.sort()                  # Ascending order
lst.sort(reverse=True)      # Descending order
lst.reverse()               # Reverse list

# 7️ Copying a List
lst_copy = lst.copy()       # Creates a copy

# 8️ Counting Occurrences
print(lst.count(5))         # Counts occurrences of 5

# 9️ Length of List
print(len(lst))             # Number of elements

# 10 Summation, Min, Max
print(sum(lst))             # Sum of all elements
print(min(lst))             # Minimum element
print(max(lst))             # Maximum element

# 1️1 List Comprehension (Creating Lists Efficiently)
squares = [x**2 for x in range(1, 6)]
evens = [x for x in lst if x % 2 == 0]

# 1️2️ Filtering Elements (Using filter())
greater_than_3 = list(filter(lambda x: x > 3, lst))

# 1️3️ Mapping Elements (Using map())
doubled = list(map(lambda x: x * 2, lst))

# 1️4️ Zipping Multiple Lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))

# 1️5️ Unpacking Lists (* Operator)
a, b, *rest = [1, 2, 3, 4, 5]

# 1️6️ Enumerating Lists (Getting Index & Value)
for index, value in enumerate(lst):
    print(f"Index {index}: {value}")

# 1️7️ Converting List to String & Vice Versa
str_list = ['Python', 'is', 'awesome']
joined_str = ' '.join(str_list)  # List → String
split_list = joined_str.split()  # String → List

# Display Results
print("Final List:", lst_copy)
