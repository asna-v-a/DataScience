f=open('C:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/number','r')
lst=[]
for i in f:
    data=i.rstrip('/n')
    lst.append(int(data))

print(lst)
print(sum(lst))