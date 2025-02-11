# String Basics in Python

# 1. Creating a String:
string1 = "Hello World"  # A string enclosed in double quotes
string2 = 'Python'       # A string enclosed in single quotes

print(string1)
print(string2)

# 2. String as a Sequence:
# Strings can be considered as ordered sequences, and we can access elements using indexing.
print("\nFirst character of string1:", string1[0])  # Indexing starts from 0
print("Sixth character of string1:", string1[5])
print("Tenth character of string1:", string1[9])

# 3. Negative Indexing:
# Negative indexing allows us to access characters starting from the end of the string.
print("\nLast character of string1:", string1[-1])   # Last character
print("Fifth character from the end of string1:", string1[-5])

# 4. Binding a String to Another Variable:
new_string = string1  # Assigning string1 to another variable
print("\nNew string:", new_string)

# 5. Using Slicing to Access Substrings:
# Slicing allows us to extract a portion of the string.
print("\nSubstring from index 0 to 5:", string1[0:6])   # Returns 'Hello '
print("Substring with stride of 2:", string1[::2])    # Select every second character: 'Hoo ol'

# 6. Using the len() Function:
# The len() function returns the length of the string.
print("\nLength of string1:", len(string1))

# 7. String Concatenation:
# We can combine two or more strings using the '+' operator.
string3 = "Hello"
string4 = "Python"
concatenated_string = string3 + " " + string4  # Concatenation
print("\nConcatenated String:", concatenated_string)

# 8. String Replication:
# You can replicate a string using the '*' operator.
replicated_string = "Hello " * 3
print("\nReplicated String:", replicated_string)  # 'Hello Hello Hello '

# 9. Strings Are Immutable:
# Strings cannot be changed directly. A new string must be created.
new_string = string1 + " is great!"
print("\nModified String:", new_string)

# 10. Escape Sequences in Strings:
# Escape sequences help in inserting special characters into strings.
print("\nThis is a new line:\nNext Line")
print("This is a tab:\tTab Space")
print("This is a backslash: \\")  # Double backslash to display a single backslash

# 11. Raw Strings:
# Use 'r' to create raw strings where escape sequences are not processed.
raw_string = r"New Line:\nTab:\tBackslash:\\"
print("\nRaw String:", raw_string)

# 12. String Methods:
# Strings have methods that allow us to manipulate or get information about them.
upper_string = string1.upper()  # Converts to uppercase
print("\nUppercase String:", upper_string)

replaced_string = string1.replace("World", "Universe")  # Replaces part of the string
print("\nReplaced String:", replaced_string)

# 13. Finding Substrings:
# The find() method returns the index of the first occurrence of the substring.
substring_index = string1.find("World")
print("\nIndex of 'World' in string1:", substring_index)

# If the substring is not found, find() returns -1.
substring_index_not_found = string1.find("Python")
print("\nIndex of 'Python' in string1:", substring_index_not_found)  # Will return -1

