fread=open('readwrite','r')
fwrite=open('readwrite2','w')

for i in fread:
    fwrite.write(i)