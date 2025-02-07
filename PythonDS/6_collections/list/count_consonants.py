# Counting consonants in a string

string = 'Luminar technolab'
vowels = 'aeiouAEIOU'
count_list = []

# Iterating through the string
for i in string:
    if i not in vowels and i != ' ':  # Checking for non-vowel and non-space characters
        count_list.append(i)

# Printing the consonants list and count
print("Consonants in the string:", count_list)
print("Total number of consonants:", len(count_list))
