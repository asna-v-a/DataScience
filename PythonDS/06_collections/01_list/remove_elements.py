#How to remove an element in a list

# remove(value) : to remove an element(mention as value) from a list
# pop() : to remove last element in a list
# pop(index) : to remove element in a particular index position
lst=[1,2,3,4,5,6,7,8,9,10]

lst.remove(1)#only one element can be deleted at a time
print(lst)

lst.pop()
print(lst)

lst.pop(0)
print(lst)