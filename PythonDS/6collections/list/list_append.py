# append() : To add a new element in a list

# Creating an empty list
lis = []

# Using a loop to append numbers from 1 to 40
for i in range(0, 40):
    lis.append(i + 1)

# Printing the list
print("List with appended elements:", lis)

# Example of appending elements manually
lst = [10]
print(lst)  # Output: [10]
lst.append(20)
print(lst)  # Output: [10, 20]
lst.append(30)
print(lst)  # Output: [10, 20, 30]
lst.append(40)
print(lst)  # Output: [10, 20, 30, 40]
