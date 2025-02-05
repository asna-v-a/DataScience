# Set

#1. Define Set
st = {1,2,3,4,5} # st={} : it is an empty dictionary not a set, a set can be defined with values in {}
print(st)

st2 = set()# Empty tuple
print(st2)
lst=[1,2,3]
st3=set(lst)# set using function, used to change other collections to set --> set(collection_name)
print(st3)
# tu2 = (10,10.5,10,20,20,20.5,1234567890,True,False,'bigdata','python')
#
# print(tu1)
# print(tu2)
# print(tu2[4])#Index : start with 0 and ends with n-1 , used to get a particular element in tuple

#2. Heterogeneous data
#3. It doesn't support duplicate values
st4={1,0,True,False,10,10,20,20,'python','bigdata'}
print(st4) #{0, 1, 20, 'bigdata', 10, 'python'}
#4. Insertion order is not preserved
#5. It's Mutable
st5={1,2,3,4,5,6}
