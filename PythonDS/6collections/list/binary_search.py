# Binary Search Algorithm :divides a sorted list in half, checking the middle, and continues in the left or right half until the element is found or not
# Time complexity is low

lst = [1, 6, 2, 10, 6, 5, 15, 21, 13, 30]

search_element = int(input("Enter the element to be searched: "))

lst.sort()
lower = 0
upper = len(lst) - 1

while lower <= upper:
    mid = (lower + upper) // 2
    if search_element == lst[mid]:
        print(search_element, "found")
        break
    elif search_element > lst[mid]:
        lower = mid + 1
    else:
        upper = mid - 1
else:
    print(search_element, "not found")
