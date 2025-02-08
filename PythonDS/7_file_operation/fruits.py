fread=open('c:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/fruits','r')
fwrite=open('c:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/fruits_1','w')

'''
for i in fread:
    if i != 'Apple\n':
        fwrite.write(i)
'''        

for i in fread:
    if 'Apple\n' not in i:# if i not in 'Apple\n' also works # Ensures 'Apple\n' lines are not copied
        fwrite.write(i)

# Close the files
fread.close()
fwrite.close()