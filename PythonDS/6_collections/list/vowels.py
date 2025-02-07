# Counting vowels in a string

string='Luminar technolab'
vowels='aeiouAEIOU'
count_list=[]

for i in string:
    if i in vowels:
        count_list.append(i)

print(count_list)
print(len(count_list))