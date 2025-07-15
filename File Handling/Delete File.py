# Common Errors
'''
Error	                      Reason

FileNotFoundError	          File does not exist
PermissionError	              No permission to delete file
IsADirectoryError	          Trying to delete a folder with os.remove()
'''

# 1. Basic File Deletion
import os
# Delete a file
os.remove("myfile.txt")
# 🔸 If the file does not exist, this will raise a FileNotFoundError.




# 2. Safe File Deletion (with Check)
import os
filename = "myfile.txt"
if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} deleted successfully.")
else:
    print(f"{filename} does not exist.")




# 3. Delete an Empty Folder (Not File)

os.rmdir("myfolder")  # Only works if folder is empty
# 🔸 To remove folders with content, use shutil (advanced).