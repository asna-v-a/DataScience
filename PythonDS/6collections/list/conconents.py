string='Luminar technolab'
vowels='aeiouAEIOU'
count_list=[]
for i in string:
    if i not in vowels and i!=' ':
        count_list.append(i)

print(count_list)
print(len(count_list))