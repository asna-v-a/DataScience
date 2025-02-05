fread=open('fruits','r')
fwrite=open('fruits1','w')
'''
for i in fread:
    if i != 'Apple\n':
        fwrite.write(i)
'''        
for i in fread:
    if 'Apple\n' not in i:# if i not in 'Apple\n' also works
        fwrite.write(i)
