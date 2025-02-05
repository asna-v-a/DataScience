#vowels
string='Luminar Technolab'
lst=[i for i in string if i in 'aeiouAeiou']
print(lst)
print(len(lst))

#or
lst=len([i for i in string if i in 'aeiouAeiou'])
print(lst)

#consonents
lst=[i for i in string if i not in 'aeiouAeiou']
print(lst)
print(len(lst))



