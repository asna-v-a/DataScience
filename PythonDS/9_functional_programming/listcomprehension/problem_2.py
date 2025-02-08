# Given string
str1 = 'Practice list comprehension problems to drill your head'

# 1. Generate a list of numbers from 1 to 1000
lst1 = [i for i in range(1, 1001)]
print(lst1)

# 2. Generate a list of numbers from 1 to 500 that are divisible by 7
lst2 = [i for i in range(1, 501) if i % 7 == 0]
print(lst2)

# 3. Generate a list of numbers from 1 to 300 that contain the digit '3'
lst3 = [i for i in range(1, 301) if '3' in str(i)]
print(lst3)

# 4. Count the number of spaces in the given string
lst4 = len([i for i in str1 if i == ' '])
print(lst4)

# 5. Count the total number of vowels in the given string
lst5 = len([i for i in str1 if i in 'aeiouAEIOU'])
print(lst5)

# 6. Extract words from the given string that have less than 4 letters
str2 = str1.split(' ')  # Split the string into words
lst6 = [i for i in str2 if len(i) < 4]
print(lst6)
