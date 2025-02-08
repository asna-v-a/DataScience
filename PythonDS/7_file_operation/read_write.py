fread=open('C:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/read_write.txt','r')
fwrite=open('C:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/read_write_1.txt','w')

for i in fread:
    fwrite.write(i)