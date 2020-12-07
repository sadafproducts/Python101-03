# Create, open, write, and read file
#===================================
# Overview
#===================================
    # open()
    # f.read()
    # f.read(n)
    # f.readline()
    # f.write()
    # f.close()
    # os.remove()
    # with
    # join()

#===================================
# Sources
#===================================
# https://www.w3schools.com/python/python_file_open.asp
# https://www.w3schools.com/python/python_file_write.asp
# https://www.w3schools.com/python/python_file_remove.asp
# https://www.youtube.com/watch?v=2vmvtxHVPJI

#===================================
# Code
#===================================
import os
rootFolder= r"D:\_PythonTempTest\07"
if not os.path.exists(rootFolder):
    os.mkdir(rootFolder)

# File handler
    # "a"  Append         It creates the file, if it does not exist
    # "r"  Read file      
    # "rb" Read Binary    Binary mode (e.g. images)
    # "rt" Read Text      Default: Text
    # "w"  Overwrie       It creates the file, if it does not exist
    # "wb" Write Binary   Binary mode (e.g. images)
    # "x"  Create file    returns an error if the file already exists
f = open(rootFolder + "\\demoFile_1.txt", "a")
f.write("This is a test\n")
f.close()

# Open and read the file after the appending:
f = open(rootFolder + "\\demoFile_1.txt", "r")
#f = open("demoFile_1.txt", "r") # if in same dir use rel. pathing
print("The content of the file, Start:\n")
print(f.read()) # By default the read() method returns the whole text
print("The content of the file, End.\n")

# Remove/Delete file
f = open(rootFolder + "\\demoFile_2.txt", "a")
if os.path.exists(rootFolder + "demoFile_2.txt"):
    os.remove(rootFolder + "demoFile_2.txt")
else:
  print("The file does not exist so I can not delete it!")
  
# Read Only Parts of the File
print("This is the 5 first ch of the file:\n")
f = open(rootFolder + "\\demoFile_1.txt", "r")
print(f.read(5)) # Return the 5 first characters of the file:

# Read Lines
print("Read the fisrt and second lines:\n")
print("line 1:", f.readline())     # Read first line 
print("line 2:", f.readline())     # By calling readline() two times, you can read the two first lines:

# Read the whole file line by line:
print("Read line by line:\n")
f = open(rootFolder + "\\demoFile_1.txt", "r")
for x in f:
  print(x)

# write file using open, write, close
f = open(rootFolder + "\\demoFile_3.txt", "a")
f.write("This is test 3\n")
f.close()

# import array
myList = ['3', '6', '9', '12', '60', '70']
print(myList)

f = open(rootFolder + "\\demoFile_4.txt", 'w')
myLine = myList[1] + "\t" + myList[2] + "\t" + myList[3] + "\t" + myList[4] + "\t" + myList[5] + "\n"
f.write(myLine)
f.close()

f = open(rootFolder + "\\demoFile_5.txt", 'w')
f.write('\t'.join(myList[1:]) + '\n')
f.close()

# write file using WITH statement => No need to close the file
with open(rootFolder + "\\demoFile_6.txt", 'w') as f:
    f.write(myList[1] + "\t" + myList[2] + "\t" + myList[3] + "\t" + myList[4] + "\t" + myList[5] + "\n")

# More efficiently, use .join():
with open(rootFolder + "\\demoFile_7.txt", 'w') as f:
    f.write('\t'.join(myList[1:]) + '\n')