# List slicing : Taking elements from a list

"""
Positive indexing : 0 to n-1 (Start from left to right)
Negative indexing : -1 to -n (Start from right to left)
"""
"""
Positive Indexing
syntax:

list[start:stop]  : Index starts from start and ends in stop-1

list[start:]    : Index starts from start and ends in last index

list[:stop]    : Index starts from index 0 and ends in last stop-1

list[:]    : Full index

list[start:stop:step] : Index starts from start and ends in stop-1 with index gap(step)

list[start::step] : Index starts from start and ends in last index with index gap(step)

list[:stop:step] : Index starts from index 0 and ends in stop-1 with index gap(step)

list[::step] : Index starts from index 0 and ends in last index with index gap(step)
"""

lst=[0,1,2,3,4,5,6,7,8,9,10]
print(lst[3:7])
print(lst[3:])
print(lst[:7])
print(lst[:])
print(lst[1:8:2])
print(lst[3::2])
print(lst[:8:2])
print(lst[::2])

print()
print()

"""
Negative Indexing

syntax:

list[start:stop]  : Index starts from start and ends in stop-1

list[start:]    : Index starts from start and ends in last index

list[:stop]    : Index starts from index 0 and ends in last stop-1

list[:]    : Full index

list[start:stop:step] : Index starts from start and ends in stop-1 with index gap(step)

list[start::step] : Index starts from start and ends in last index with index gap(step)

list[:stop:step] : Index starts from index 0 and ends in stop-1 with index gap(step)

list[::step] : Index starts from index 0 and ends in last index with index gap(step)
"""

lst1=[0,1,2,3,4,5,6,7,8,9,10]
print(lst1[-1])
print(lst1[-5])
# print(lst[3:7])
# print(lst[3:])
# print(lst[:7])
# print(lst[:])
# print(lst[1:8:2])
# print(lst[3::2])
# print(lst[:8:2])
# print(lst[::2])