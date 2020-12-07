# Create, open, write, and read file
# This needs cleaning up

import os

rootFolder= r"D:\_PythonTempTest\07"

if not os.path.exists(rootFolder):
    os.mkdir(rootFolder)

# File handler
f = open(rootFolder + "\\demoFile_1.txt", "a")     
                                    # "a"  Append         It creates the file, if it does not exist
                                    # "r"  Read file      
                                    # "rb" Read Binary    Binary mode (e.g. images)
                                    # "rt" Read Text      Default: Text
                                    # "w"  Overwrie       It creates the file, if it does not exist
                                    # "wb" Write Binary   Binary mode (e.g. images)
                                    # "x"  Create file    returns an error if the file already exists

# Open and read the file after the appending:
f = open("demoFile_2.txt", "r")
print(f.read())

f = open("D:\\demoFile_1.txt", "r") # if in different dir
print(f.read())

f.write("Woops! I have deleted the content!")
f.close()


# Check if file exists, then delete it:
# import os
if os.path.exists("demoFile_2.txt.txt"):
  os.remove("demoFile_2.txt.txt")
else:
  print("The file does not exist so I can not delete it!")

# Delete Entire Folder
os.rmdir("demoFolder_1")      # Note: You can only remove empty folders.


# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# Example eturn the 5 first characters of the file:
#f = open("delete this test file 8.txt", "r")
print(f.read(5))


# Read Lines
# You can return one line by using the readline() method:
# Example Read one line of the file:
#f = open("delete this test file 9.txt", "r")
print(f.readline())
print(f.readline())     # By calling readline() two times, you can read the two first lines:

# By looping through the lines of the file, you can read the whole file, line by line:
#Example Loop through the file line by line:
#f = open("delete this test file 10.txt", "r")
for x in f:
  print(x)


# https://www.w3schools.com/python/python_file_open.asp
# https://www.w3schools.com/python/python_file_write.asp
# https://www.w3schools.com/python/python_file_remove.asp

#https://www.youtube.com/watch?v=2vmvtxHVPJI

#You can use a parameter in the with statement representing the file you're writing to. From there, use .write(). This assumes that everything in l is a string, otherwise you'd have to wrap all of them with str().
import array
l = ['3', '6', '9', '12', '60', '70']
#x/3.0
print(l)

with open('delete this test file 11', 'w') as f:
    f.write(l[1] + "\t" + l[2] + "\t" + l[3] + "\t" + l[4] + "\t" + l[5] + "\n")

#Alternatively, and more efficiently, you can use .join():

with open('delete this test file 11', 'w') as f:
    f.write('\t'.join(l[1:]) + '\n')