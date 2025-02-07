# Function to calculate cube

def cube(num):
    cube=num**3
    return cube
num = int(input("Enter the number: "))
value=cube(num)
print("Cube of",num,"is",value)