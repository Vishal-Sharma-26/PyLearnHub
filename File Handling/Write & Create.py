# Summary of Write Modes
'''
Mode	       Meaning	                  Behavior
w	           Write	                  Creates or overwrites a file
x	           Exclusive creation	      Creates a file, error if exists
a	           Append	                  Adds to the end if file exists
wt	           Write in text mode	      Same as w, writes strings
wb	           Write in binary mode	      Use for binary data (e.g., images)
'''

# 1. Create and Write to a File using "w" Mode
'''
"w" creates a file if it doesn’t exist.
If it already exists, it overwrites the content.
'''

# Create and write to a file (overwrite if it exists)
with open("myfile.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This file is created using 'w' mode.\n")




# 2. Create a File Only if It Doesn’t Exist using "x" Mode
'''
"x" creates a file.
If the file already exists, it raises an error.
'''

try:
    with open("unique_file.txt", "x") as file:
        file.write("This file was created using 'x' mode.\n")
except FileExistsError:
    print("File already exists. Cannot overwrite.")




# 3. Append to a File using "a" Mode
'''
"a" creates the file if it doesn't exist.
If it exists, it adds content to the end.
'''

with open("myfile.txt", "a") as file:
    file.write("Adding this line at the end using 'a' mode.\n")




 # 4. Create and Write Text (Explicit Text Mode using wt)
'''
You can explicitly use "wt" which is same as "w" because text mode is default.
'''

with open("text_mode_file.txt", "wt") as file:
    file.write("Writing in text mode explicitly.\n")