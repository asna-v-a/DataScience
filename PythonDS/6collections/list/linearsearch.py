# Linear Search Algorithm : Search each element in a list from the start, stopping if found or continuing to the end if not
#Time complexity is high

lst=[10,15,11,12,17,20,22,23,36,16,1,32,40]

search_element = int(input("Enter the element to be searched: "))

flag =0
for i in lst:
    if i==search_element:
        flag=1
        break
if flag==1:
    print(search_element, "found in list")
else:
    print(search_element,"not found in list")
