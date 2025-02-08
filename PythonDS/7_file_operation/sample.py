f = open('C:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/sample_1.txt', 'r')

# for i in f:
#     print(i)
# print()

# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if age=='21':
#         print(data[1:5])

# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if age>'23':
#         print(data[1:4])

# for i in f:
#     data=i.rstrip('\n').split(',')
#     location=data[5]
#     if location=='Chennai':
#         print(data[1:5])

for i in f:
    data=i.rstrip('\n').split(',')
    age = data[3]
    location=data[5]
    if age>'23' and location=='Chennai':
        print(data[1:4])