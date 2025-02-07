# ******************** Dictionary Operations in Python ********************

# ********** 1. Define a Dictionary **********
dic = {
    'id': 101,
    'fname': 'vinay',
    'lname': 'k',
    'age': 28,
    'profession': 'bigdata'
}

# ********** 2. Accessing Dictionary Values **********
print("First Name:", dic['fname'])
print("Last Name:", dic['lname'])
print("Age:", dic['age'])
print()

# ********** 3. Iterating Over Dictionary **********
print("Dictionary Items:")
for key in dic:
    print(key, ":", dic[key])

# Using .items() method
print("Using items() method:")
for key, value in dic.items():
    print(key, ":", value)

# ********** 4. Updating Dictionary Values **********
dic['age'] = 10  # Updating age
print("After updating age:", dic)

dic['age'] += 10  # Incrementing age by 10
print("After incrementing age:", dic)

# ********** 5. Adding a New Key-Value Pair **********
dic['marks'] = 100
print("After adding 'marks':", dic)

# ********** 6. Checking Key Existence **********
print("Is 'age' in dictionary?", 'age' in dic)
print("Is 'age' not in dictionary?", 'age' not in dic)
print("Is 'fname' in dictionary?", 'fname' in dic)
print("Is 'lname' not in dictionary?", 'lname' not in dic)
print("Is 'location' not in dictionary?", 'location' not in dic)

# ********** 7. Deleting a Key-Value Pair **********
del dic['id']
print("After deleting 'id':", dic)

# Using pop() to remove a key and return its value
removed_value = dic.pop('marks')
print("After popping 'marks':", dic, "| Removed Value:", removed_value)

# Using popitem() to remove and return the last inserted key-value pair
removed_pair = dic.popitem()
print("After popitem():", dic, "| Removed Pair:", removed_pair)

# ********** 8. Merging Two Dictionaries **********
dic2 = {'location': 'India', 'experience': 5}
dic.update(dic2)
print("After merging with dic2:", dic)

# ********** 9. Getting Dictionary Keys, Values, and Items **********
print("Keys:", dic.keys())         # Returns all keys as a list-like view
print("Values:", dic.values())     # Returns all values as a list-like view
print("Items:", dic.items())       # Returns all key-value pairs as a list of tuples

# ********** 10. Copying a Dictionary **********
dic_copy = dic.copy()
print("Copied Dictionary:", dic_copy)

# ********** 11. Clearing a Dictionary **********
dic_copy.clear()
print("After clearing dic_copy:", dic_copy)

# ********** 12. Creating a Dictionary with Default Values **********
keys = ['name', 'age', 'city']
default_value = 'N/A'
new_dict = dict.fromkeys(keys, default_value)
print("Dictionary with default values:", new_dict)

# ********** 13. Using the get() Method **********
print("Using get() for 'age':", dic.get('age', 'Not Found'))  # Returns value if key exists, else default
print("Using get() for 'salary':", dic.get('salary', 'Not Found'))

# ********** 14. Using setdefault() Method **********
# Gets the value of a key; if the key doesn't exist, inserts key with default value
print("Using setdefault for 'location':", dic.setdefault('location', 'Unknown'))  # Already exists, returns 'India'
print("Using setdefault for 'company':", dic.setdefault('company', 'UptoSkills'))  # Adds 'company' with default value
print("After using setdefault:", dic)

# ********** 15. Summary **********
"""
- Dictionaries store **key-value pairs** and allow **fast lookup**.
- Keys must be **unique and immutable** (strings, numbers, tuples).
- Values can be **any data type**.
- Supports **modification, addition, and deletion** of key-value pairs.
- Checking key existence using **'in' and 'not in'** operators.
- Methods:
    - `update()` → Merges another dictionary.
    - `pop(key)` → Removes a key and returns its value.
    - `popitem()` → Removes and returns the last inserted item.
    - `keys()` → Returns all dictionary keys.
    - `values()` → Returns all dictionary values.
    - `items()` → Returns all key-value pairs.
    - `copy()` → Creates a copy of the dictionary.
    - `clear()` → Clears all key-value pairs.
    - `fromkeys(keys, default)` → Creates a dictionary with default values.
    - `get(key, default)` → Retrieves a value safely, avoiding errors.
    - `setdefault(key, default)` → Returns key value or inserts default if not present.
"""

