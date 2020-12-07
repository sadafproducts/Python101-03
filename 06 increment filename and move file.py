# rename files by by incrementing filename and move them to new folders
# We changed txt to pdf because we can!

print("Before running this example, make a copy of 02 folder then rename it to 06")

import os
rootFolder = r"D:\_PythonTempTest\06"
for filename in os.listdir(rootFolder):
    if filename.endswith('.txt'):
        newFolderName = os.path.splitext(filename)[0]
        newFolderPath = rootFolder + '\\' + str( int(newFolderName) + 500 ) # To increment filename you need to convert string to int and int to string 
        print(newFolderPath)        
        if not os.path.exists(newFolderPath):
            os.mkdir(newFolderPath)
        os.rename(rootFolder + '\\' + filename, newFolderPath + '\\data.pdf')
# End of this example
