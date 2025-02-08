# Given string
string = 'Luminar Technolab'

# Extract vowels from the string
vowels_list = [i for i in string if i in 'aeiouAEIOU']
print(vowels_list)  # List of vowels
print(len(vowels_list))  # Count of vowels

# Alternative way to count vowels directly
vowel_count = len([i for i in string if i in 'aeiouAEIOU'])
print(vowel_count)

# Extract consonants from the string
consonants_list = [i for i in string if i not in 'aeiouAEIOU' and i.isalpha()]
print(consonants_list)  # List of consonants
print(len(consonants_list))  # Count of consonants
