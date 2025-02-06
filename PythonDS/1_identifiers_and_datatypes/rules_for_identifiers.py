# Rules for Creating Identifiers and Variables in Python

# There are certain rules and conventions that must be followed while creating identifiers and variables in Python:

# Rules for Creating Identifiers:
# 1. Must start with a letter or an underscore (_).
#    Valid: num, _age
#    Invalid: 2num (Cannot start with a digit)

# 2. Can only contain letters (a-z, A-Z), digits (0-9), and underscores (_).
#    Valid: my_variable, var_2
#    Invalid: my-variable (Hyphen is not allowed)

# 3. Cannot be a keyword:
#    Keywords in Python (e.g., for, if, while, else, break) cannot be used as identifiers.
#    Example of invalid identifiers: for, if, pass, etc.

# 4. Case-sensitive:
#    Python treats identifiers as case-sensitive.
#    Example: num, Num, and NUM are all distinct identifiers.

# 5. Spaces are not allowed:
#    Instead of using spaces in identifiers, use an underscore (_).
#    Example: company_name is valid, while company name is not.

# 6. Use meaningful names:
#    It’s recommended to use descriptive names for your variables to make the code more readable.
#    Example: age, salary, name are better than a, b, c.

# 7. Multiple variables in a single line:
#    You can declare multiple variables in a single line.
a, b, c = 10, 20, 30

# Example of Invalid Identifiers:
# 2num = 10   # Starts with a number
# company name = 'Luminar'  # Contains a space
