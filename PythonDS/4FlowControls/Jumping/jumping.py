# Jumping statements

"""
1. break
2. continue
3.pass

"""

# break - to exit a loop

# example
for i in range(1, 51):
    if i == 25:
        break
    print(i,end=' ')
print()

# continue - skip the condition and continue the loop

# example
for i in range(1, 51):
    if i == 25:
        continue
    print(i,end=' ')
print()

#pass - do nothing

for i in range(1, 51):
    if i == 25:
        pass
    print(i,end=' ')