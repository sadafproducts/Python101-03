# Move multiple files to multiple folders and renames them
# 1 list files and forldes in a directory
# 2 filter based on fileType
# 3 take the name of a file and create a folder base on that
# 4 move the file to the new folder and then rename the file

print("Before running this example, run 02 and make a copy of 02 folder then rename it to 03")

import os

# Get all contents and filter based on file extention
for filename in os.listdir(r"D:\_PythonTempTest\03"): # for loop always end with :
    if filename.endswith('.txt'): # if ends with :
        print(filename) # You can see the contents in terminal
        
# Now lets create folder for each file using the same name
rootFolder = r"D:\_PythonTempTest\03"

for filename in os.listdir(rootFolder):
    if filename.endswith('.txt'):   
        newFolderPath = rootFolder + '\\' + os.path.splitext(filename)[0] # We simply remove the file extension to get the path of the new folder! [1] is the .extension
        print(newFolderPath)
        os.mkdir(newFolderPath)
        os.rename(rootFolder + '\\' + filename, newFolderPath + '\\data.txt') # move the file to its folder and at the same time rename fileName
# End of this example.