st = {1,2,3,4,5,6,7,8,9,10,1}

# Sum()
print(sum(st))# 1 will be considered once, duplicate values are not supported

# Max()
print(max(st))

# Min()
print(min(st))

# Add()
st.add(50)
print(st)

# Update()
st.update([45,60,75])
print(st)

# remove() : if there is no element that to be deleted in the set, it will return a KeyError
st.remove(50)
print(st)

# discard() : if there is no element that to be deleted in the set, it will not return anything
st.discard(60)
print(st)

# pop()
st.pop()
print(st)

