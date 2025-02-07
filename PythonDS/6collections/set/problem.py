#Alphabet Shift Program

lst=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lst2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

num = int(input("Enter the number: "))
alpha = input("Enter the alphabet: ")

if alpha.islower():
    for i in range(len(lst2)):
        if lst2[i]==alpha:
            print(lst2[i+num])
            break
elif alpha.isupper():
    for i in range(len(lst)):
        if lst[i]==alpha:
            print(lst[i+num])
            break
else:
    print("Enter a valid alphabet")