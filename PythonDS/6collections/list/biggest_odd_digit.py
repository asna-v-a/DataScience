# Function to find the largest odd digit in a given number

def biggest_odd(num):
    lst = []
    
    # Extract odd digits from the number
    for i in num:
        if int(i) % 2 == 1:
            lst.append(i)

    # If there are no odd digits, return a message
    if not lst:
        return "No odd digits found."

    # Sort in descending order and return the largest odd digit
    lst.sort(reverse=True)
    return lst[0]

# User input
number = input("Enter the number: ")
result = biggest_odd(number)

# Output the largest odd digit
print("Largest odd digit:", result)
