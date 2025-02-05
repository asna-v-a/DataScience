str1='Practice list comprehension problems to drill your head'
# 1-1000 elements
lst1=[i for i in range(1,1001)]
print(lst1)

# 1-500 divisible by 7
lst2=[i for i in range(1,501) if i%7==0]
print(lst2)

# 1-300 3 in them
lst3=[i for i in range(1,301) if '3' in str(i)]
print(lst3)

# count no of space in string
lst4=len([i for i in str1 if i==' '])
print(lst4)

# total no of vowels in a string
lst5=len([i for i in str1 if i in 'aeiouAEIOU'])
print(lst5)

# words in a string less than 4 letters
str2=str1.split(' ')
lst6=[i for i in str2 if len(i)<4]
print(lst6)

