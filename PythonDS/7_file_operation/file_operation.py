# File Operations in Python

# Three Main File Modes:
# 1. Read ('r') - Reads data from an existing file.
# 2. Write ('w') - Creates a new file (or overwrites if the file exists).
# 3. Append ('a') - Adds data to an existing file without deleting previous content.

# Creating a file reference
# var = open('filename.txt', 'mode')

# 1. Writing to a File ('w' mode)
file = open("c:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/sample.txt", "w")  # Create/Open file in write mode
file.write("Hello, this is a test file.\n")
file.write("File handling in Python is easy!\n")
file.close()  # Close the file

# 2. Reading from a File ('r' mode)
file = open("c:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/sample.txt", "r")  # Open file in read mode
content = file.read()  # Read the entire file
print(content)  # Print file content
file.close()

# 3. Appending Data to a File ('a' mode)
file = open("c:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/sample.txt", "a")  # Open file in append mode
file.write("Appending new content...\n")
file.close()

# 4. Reading File Line by Line
file = open("c:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/sample.txt", "r")
for line in file:
    print(line.strip())  # Read file line by line
file.close()

# 5. Using 'with open()' (Recommended)
# Automatically closes the file after execution
with open("c:/Users/asnav/Desktop/DataScience/PythonDS/7_file_operation/files/sample.txt", "r") as file:
    print(file.read())  # Read the file content

# Additional File Operations
# 1. readline() -> Reads one line at a time.
# 2. readlines() -> Reads all lines and returns a list.
# 3. seek(0) -> Moves file pointer to the beginning.
# 4. tell() -> Returns the current position of the file pointer.
