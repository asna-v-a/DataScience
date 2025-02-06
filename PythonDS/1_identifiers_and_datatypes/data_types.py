# Data Types in Python

# In Python, data types are used to define the type of a value or variable. 
# Python is dynamically typed, meaning that the interpreter automatically determines the data type of a variable when it is assigned a value.

# Common Data Types in Python:

# 1. Integer (int):
#    An integer is a whole number, without a decimal point.
#    Example: num = 10
#    The 'int' type is used to represent whole numbers, both positive and negative.
num = 10   # An integer
print("Value of num:", num)  # Printing the value of num
print("Type of num:", type(num))  # Printing the type of num

# 2. Float:
#    A float is a number that has a decimal point.
#    Example: price = 19.99
#    The 'float' type represents real numbers, including decimals.
price = 19.99   # A floating-point number
print("\nValue of price:", price)  # Printing the value of price
print("Type of price:", type(price))  # Printing the type of price

# 3. String (str):
#    A string is a sequence of characters enclosed in single quotes (' ') or double quotes (" ").
#    Example: name = "Asna"
#    The 'str' type is used for textual data.
name = "Asna"   # A string
print("\nValue of name:", name)  # Printing the value of name
print("Type of name:", type(name))  # Printing the type of name

# 4. Boolean (bool):
#    A boolean is a data type that can hold one of two values: True or False.
#    Example: is_active = True
#    The 'bool' type represents logical values: True or False.
is_active = True   # A boolean value
print("\nValue of is_active:", is_active)  # Printing the value of is_active
print("Type of is_active:", type(is_active))  # Printing the type of is_active

# 5. List:
#    A list is an ordered collection of values. Lists can contain different types of values (mixed data types) and are mutable (changeable).
#    Example: fruits = ["apple", "banana", "cherry"]
#    The 'list' type is used to store collections of items.
fruits = ["apple", "banana", "cherry"]   # A list of strings
print("\nValue of fruits:", fruits)  # Printing the value of fruits
print("Type of fruits:", type(fruits))  # Printing the type of fruits

# 6. Tuple:
#    A tuple is similar to a list, but unlike lists, tuples are immutable (cannot be changed).
#    Example: coordinates = (10, 20, 30)
#    The 'tuple' type is used to store a fixed collection of items.
coordinates = (10, 20, 30)   # A tuple of integers
print("\nValue of coordinates:", coordinates)  # Printing the value of coordinates
print("Type of coordinates:", type(coordinates))  # Printing the type of coordinates

# 7. Dictionary (dict):
#    A dictionary is an unordered collection of key-value pairs. Keys must be unique, and values can be of any data type.
#    Example: person = {"name": "Asna", "age": 24}
#    The 'dict' type is used to store data in a key-value structure.
person = {"name": "Asna", "age": 24}   # A dictionary with string keys and mixed values
print("\nValue of person:", person)  # Printing the value of person
print("Type of person:", type(person))  # Printing the type of person

# 8. Set:
#    A set is an unordered collection of unique values. Sets do not allow duplicates.
#    Example: unique_numbers = {1, 2, 3, 4}
#    The 'set' type is used to store unique values.
unique_numbers = {1, 2, 3, 4}   # A set of integers
print("\nValue of unique_numbers:", unique_numbers)  # Printing the value of unique_numbers
print("Type of unique_numbers:", type(unique_numbers))  # Printing the type of unique_numbers

# 9. NoneType:
#    None is a special data type representing the absence of a value or a null value.
#    Example: value = None
#    The 'NoneType' is used to represent a variable that does not have a value.
value = None   # NoneType, representing no value
print("\nValue of value:", value)  # Printing the value of value
print("Type of value:", type(value))  # Printing the type of value

# Example of Type Checking:
# You can use the 'type()' function to check the type of a variable.
print("\nType of num:", type(num))   # <class 'int'>
print("Type of price:", type(price))   # <class 'float'>
print("Type of name:", type(name))   # <class 'str'>
