# Summary of Read Methods
'''
Method	                 Description
file.read()	             Reads the whole file as one string
file.readline()	         Reads one line at a time
file.readlines()	     Reads all lines into a list
for line in file	     Iterates over each line (best for large files)
'''


# 1. Open a File for Reading

file = open("example.txt", "r")  # "r" means read mode




 # 2. Read the Entire File

with open("example.txt", "r") as file:
    content = file.read()
    print(content)




# 3. Read Line by Line

with open("example.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1, line2)




# 4. Read All Lines into a List

with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes newline characters




# 5. Loop Through File Directly (Efficient Way)

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())




# 6. What if the File Doesn’t Exist?

try:
    with open("example.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")