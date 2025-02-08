# Write a function called capitalize. This function takes a string as an argument and capitalizes the first letter of each word.
# #For example,'i like learning' becomes 'I Like Learning'.


def capitalize(words):
    word =''

    for i in range(len(words)):
        if i == 0 or words[i-1]==' ':
            word += words[i].upper()

        else:
            word+=words[i]

    # word=words.title()
    # word=words.capitalize()
    return word


words = input("Enter the string: ")
result = capitalize(words)
print(result)
