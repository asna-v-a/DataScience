# ================================
# Set Operations in Python
# ================================

# 1. Basic Operations
st = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1}  # Duplicates are ignored

print("\n# Basic Operations")
print("Sum:", sum(st))  # Adds all unique elements
print("Max:", max(st))  # Returns the highest value
print("Min:", min(st))  # Returns the lowest value

# 2. Adding Elements
print("\n# Adding Elements")
st.add(50)  # Adds a single element
print("After adding 50:", st)
st.update([45, 60, 75])  # Adds multiple elements
print("After updating with multiple values:", st)

# 3. Removing Elements
print("\n# Removing Elements")
st.remove(50)  # Raises KeyError if not found
print("After removing 50:", st)
st.discard(60)  # Does not raise an error if not found
print("After discarding 60:", st)
st.pop()  # Removes an arbitrary element
print("After pop operation:", st)

# 4. Set Operations (Union, Intersection, Difference)
st1 = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7, 8}

print("\n# Set Operations")
print("Union:", st1.union(st2))  # Combines elements from both sets
print("Intersection:", st1.intersection(st2))  # Common elements
print("Difference:", st1.difference(st2))  # Elements in st1 but not in st2
print("Symmetric Difference:", st1.symmetric_difference(st2))  # Elements in either set but not both

# 5. Set Comparisons
print("\n# Set Comparisons")
print("Is st1 a subset of st2?", st1.issubset(st2))  # Checks if st1 ⊆ st2
print("Is st1 a superset of st2?", st1.issuperset(st2))  # Checks if st1 ⊇ st2
print("Are st1 and st2 disjoint?", st1.isdisjoint(st2))  # True if no common elements

# 6. Clearing and Copying
print("\n# Clearing and Copying")
st_copy = st.copy()  # Creates a shallow copy
print("Copied Set:", st_copy)
st.clear()  # Removes all elements from the set
print("After clearing the set:", st)  # Empty set

"""
Summary of Set Functions:
-------------------------
add(x)               : Adds an element x to the set.
update(iterable)     : Adds multiple elements from an iterable.
remove(x)            : Removes x (raises KeyError if not found).
discard(x)           : Removes x (does nothing if not found).
pop()                : Removes and returns an arbitrary element.
union(set2)          : Returns a new set with elements from both sets.
intersection(set2)   : Returns a new set with common elements.
difference(set2)     : Returns elements in the first set but not in the second.
symmetric_difference(set2) : Returns elements in either set but not both.
issubset(set2)       : Checks if a set is a subset of another.
issuperset(set2)     : Checks if a set is a superset of another.
isdisjoint(set2)     : Checks if two sets have no elements in common.
copy()               : Creates a copy of the set.
clear()              : Removes all elements from the set.
"""

