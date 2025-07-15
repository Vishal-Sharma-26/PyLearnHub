# 🧰 Python os Module – Complete Guide
# The os module in Python provides a way to interact with the operating system. You can use it to work with files, directories, environment variables, and system-level tasks.

'''
🔹 Common Uses of the os Module
Task	                                           Function
Get current working directory	                   os.getcwd()
Change working directory	                       os.chdir(path)
List files and folders	                           os.listdir(path)
Create a folder	                                   os.mkdir(folder_name)
Create nested folders	                           os.makedirs(path)
Remove a file	                                   os.remove(file_name)
Remove a folder	                                   os.rmdir(folder_name)
Remove nested folders	                           os.removedirs(path)
Rename a file or folder	                           os.rename(old, new)
'''

'''
🧠 FILE PATH UTILITIES (os.path)
Function	                                       Description
os.path.exists(path)	                           Check if file/folder exists
os.path.isfile(path)	                           Is it a file?
os.path.isdir(path)	                               Is it a directory?
os.path.getsize(path)	                           Size in bytes
os.path.abspath(path)	                           Get absolute path
os.path.basename(path)	                           File/folder name only
os.path.dirname(path)	                           Get directory name only
os.path.join(a, b)	                               Join paths safely (cross-platform)
'''

'''
🧑‍💻 PROCESS & SYSTEM INFO
Function	                                       Description
os.name	                                           OS type ('posix' for Unix, 'nt' for Windows)
os.system("command")	                           Run a shell command
os.cpu_count()	                                   Get number of CPUs
os.getlogin()	                                   Get current user name
os.getpid()	                                       Get current process ID
os.uname() (Linux only)	                           System info
'''

'''
🧱 Summary Table
Category	                        Functions
Directory Mgmt	                    getcwd(), chdir(), listdir(), mkdir()
File Mgmt	                        remove(), rename(), makedirs(), rmdir()
Path Ops	                        exists(), isfile(), join(), getsize()
System Info	                        name, getlogin(), cpu_count()
Env Variables	                    os.environ, os.environ.get()
Directory Walk	                    os.walk()
'''

# 1. Importing the Module.
import os


# 2. Get Current Working Directory
print(os.getcwd())


# 3. Change Directory
os.chdir("Enter your path here")


# 4. List Files and Folders
print(os.listdir())  # Current folder
print(os.listdir("C:/Users"))  # Specific folder


# 5. Create Folder
os.mkdir("new_folder")


# 6. To create nested folders:
os.makedirs("parent_folder/child_folder")


# 7. Rename File or Folder
os.rename("old.txt", "new.txt")


# 8. Delete File or Folder
os.remove("file.txt")         # Delete file
os.rmdir("empty_folder")      # Delete empty folder
os.removedirs("a/b/c")        # Delete nested empty folders


# 9. Check if File/Folder Exists
if os.path.exists("myfile.txt"):
    print("File exists!")
else:
    print("Not found")


# 10. Join Paths (Cross-Platform Safe)
path = os.path.join("folder", "file.txt")
print(path)  # Outputs folder/file.txt


# 11. Get File or Directory Info
print(os.path.isfile("myfile.txt"))    # Check if it's a file
print(os.path.isdir("myfolder"))       # Check if it's a folder


# 12. Delete All .txt Files in a Folder
folder = "Select folder"

for file in os.listdir(folder):
    if file.endswith(".txt"):
        os.remove(os.path.join(folder, file))


# 🧬 ENVIRONMENT VARIABLES

# 13. Access System Environment Variables
print(os.environ['PATH'])  # Get PATH variable


# 14. Get and Set Variables
os.environ['MY_VAR'] = 'hello'
print(os.environ.get('MY_VAR'))  # Output: hello


# 🧮 EXECUTE SYSTEM COMMANDS

# 15. Run Terminal Commands
os.system("echo Hello")            # Prints Hello
os.system("dir")                   # Windows directory listing
os.system("ls")                    # Linux/Mac directory listing


# 📋 WALKING THROUGH FILE SYSTEM

# Traverse Directories Recursively
for root, dirs, files in os.walk("my_folder"):
    print("Current Directory:", root)
    print("Subdirectories:", dirs)
    print("Files:", files)