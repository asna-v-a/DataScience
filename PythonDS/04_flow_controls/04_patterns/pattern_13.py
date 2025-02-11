for i in range(5,0,-1):
    for j in range(i-1):
        print(' ',end=' ')
    for k in range(6,i,-1):
        print('*',end=' ')
    for l in range(5,i,-1):
        print('*',end=' ')

    print()


"""
        * 
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *

"""

print('\n\n\n')

for i in range(1,6):
    print(" "*(6-i),end='')
    for j in range(i,2*i):
        print('*',end='')
    for j in range(2*i-2,i-1,-1):
        print('*',end='')
    print()

for i in range(4,0,-1):
    print(" "*(6-i),end='')
    for j in range(i,2*i):
        print('*',end='')
    for j in range(2*i-2,i-1,-1):
        print('*',end='')
    print()


"""
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *

"""


print('\n\n\n')


for i in range(1,6):
    print(" "*(6-i),end='')
    for j in range(i,2*i):
        print(j,end='')
    for j in range(2*i-2,i-1,-1):
        print(j,end='')
    print()


"""
                  1
                2 3 2
              3 4 5 4 3
            4 5 6 7 6 5 4
          5 6 7 8 9 8 7 6 5

"""

