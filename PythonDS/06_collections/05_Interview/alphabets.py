#Sorting alphabets in a string

# def sort_words(words):
#     lst=[]
#     for i in range(len(words)):
#         if words[i].isalpha():
#             lst.append(words[i])
#     st=set(lst)
#     lst=list(st)
#     lst.sort()
#     word=[','.join(lst)]
#     return word


def sort_words(words):
    lst=[]
    sen=words.replace(' ','')
    for i in sen:
        if i not in lst:
            lst.append(i)
    lst.sort()
    word=[','.join(lst)]
    return word

words = input("Enter the string: ")
result=sort_words(words)
print(result)

