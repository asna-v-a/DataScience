# Pattern Problems

# Nested for loop
num = int(input("Enter the number: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(i, end=" ")
    print()

print()

"""
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

"""


for i in range(0, num):
    for j in range(1, num + 1):
        print(j+i, end=" ")

    print()
print()

"""
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9

"""

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

"""

"""

for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=" ")
    print()

print()

General Notes on Pattern Printing:
print() - Moves to a new line after each row
i - Controls the number of rows
j - Controls the number of columns
print(i) - Prints the same value in a row
print(j) - Prints different values in a row

Pattern Direction Guidelines:
- Top-down decreasing pattern: Outer loop (i) should decrement (num, 0, -1)
- Bottom-up decreasing pattern: Inner loop (j) should decrement (num, 0, -1)

"""