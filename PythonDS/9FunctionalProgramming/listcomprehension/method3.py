#method 3
#1-50 even square, odd cube
lst=[(i,i**2) if i%2==0 else (i,i**3) for i in range(1,51)]
print(lst)

#1-30 even print even, odd print odd
lst=[(i,"Even") if i%2==0 else (i,"Odd") for i in range(1,31)]
print(lst)

#1-50 1-15 small, 16-35 medium, above 35 large
lst=[(i,"Small") if i<=15 else (i,"Medium") if i<=35 else (i,"Large") for i in range(1,51)]
print(lst)