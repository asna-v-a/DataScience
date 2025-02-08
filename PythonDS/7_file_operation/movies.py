f = open("C:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/movies_cleaned_pandas.csv", 'r')

count=count2 =count3=count4= 0
row=0
max1=max2=0
min1=min2=10.0
dic = {}
dic2 = {}
dic3 = {}
lst = []
lst2 = []
lst3=[]
lst4=[]
lst5=[]
lst6=[]
lst7=[]

for i in f:
    # row count
    count += 1
    data = i.rstrip('\n').split(',')
    lst1 = [int(data[0]), data[1], int(data[2]), float(data[3]), float(data[4])]
    lst.append(lst1)

    # Find Each year release movie count
    year = int(data[2])
    if year not in dic2:
        dic2[year] = 1
    else:
        dic2[year] += 1

    # Each rating count
    rating=data[3]
    if rating not in dic:
        dic[rating] = 1
    else:
        dic[rating] += 1

    # Find duration mxm 1 movies name,year,rating,duration
    duration = float(data[3])
    if duration >max1:
        max1=duration
        lst4=data[1:]

    # Find rating mnm 1 movies name,year,rating,duration
    rating = float(data[3])
    if rating < min1:
        min1=rating
        lst5=data[1:]

    # 2008 and rating above 3 [collect] row count
    year = data[2]
    rating = float(data[3])
    if year == '2008' and rating > 3:
        row+=1


    #2008 movies count
    if year == '2008':
        count2+=1


    #Rating above 4 and release year above 2005
    #A. Rating mxm movies full data
    if year == '2005' and rating > 4:
        if rating>max2:
            max2 = rating
            lst6=data[:]
        # B. Rating mnm movies full data
        if rating<min2:
            min2 = rating
            lst7=data[:]




    # 1975-2000 movies collect Row count
    if year >= '1975' and year<='2000':
        count3+=1

    # 1975-2000 and rating above 3.5 total row count
    if year >= '1975' and year<='2000' and rating>3.5:
        count4+=1

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        # rating max 5 movie name,year,rating
        if lst[i][3] <= lst[j][3]:  # last 5 lst[i][3]<=lst[j][3]
            lst[i], lst[j] = lst[j], lst[i]
        # rating min 3 movie name,year,rating
        if lst[i][3] >= 3:
            lst2.append(lst[i])
        break



# row count
print(count)
print()
# rating max 5 movie name,year,rating
print(lst[:5])
print()
# rating min 3 movie name,year,rating
print(lst2[:5])
print()
#Each rating count
print(dic)
print()
#Find Each year release movie count
print(dic2)
print()
#2008 and rating above 3 [collect] row count
print(row)
print()
#Find duration mxm 1 movies name,year,rating,duration
print(lst4)
print()
#Find rating mnm 1 movies name,year,rating,duration
print(lst5)
print()
#Rating above 4 and release year above 2005
 #A. Rating mxm movies full data
print(lst6)
print()
#B. Rating mnm movies full data
print(lst7)
print()
#2008 movies count
print(count2)
print()
#1975-2000 movies collect Row count
print(count3)
print()
#1975-2000 and rating above 3.5 total row count
print(count4)
print()
