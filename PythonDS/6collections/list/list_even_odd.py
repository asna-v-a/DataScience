# Generate a list of numbers from 1 to 100
lst = []
even_list = []
odd_list = []

# Classifying numbers into even and odd lists
for i in range(1, 101):
    lst.append(i)
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

# Print all lists
print("Full List:", lst)
print("Even Numbers List:", even_list)
print("Odd Numbers List:", odd_list)

# Calculate and print sums
print("Sum of Full List:", sum(lst))
print("Sum of Even Numbers List:", sum(even_list))
print("Sum of Odd Numbers List:", sum(odd_list))
