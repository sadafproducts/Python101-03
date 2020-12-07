# Working with system files
#   1 - create a file
#   2 - create a folder
#   3 - rename a file
#   4 - move a file
# Pay attention to r before the paths: escape the backslashes or use raw strings: "C:\\Users..." or r"C:\Users..."

open(r"D:\Python01_test.txt", "a") # Create a file
import os   # Add os lib to use mkdir and rename commands
os.mkdir(r"D:\_PythonTempTest0") # Create a direcory/folder
os.rename(r"D:\Python01_test.txt", r"D:\Python01.txt") # Rename file 
os.rename(r"D:\Python01.txt", r"D:\_PythonTempTest0\01_file.txt") # Move the file to the new directroy you created

# Create another file and then delete it
open(r"D:\_PythonTempTest0\02_file.txt", "a")
os.remove(r"D:\_PythonTempTest0\02_file.txt") 
# End of this example.