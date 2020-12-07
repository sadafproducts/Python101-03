# This creates a dated calendar 
# The date of a day id placed inside every single files
# If you want to delete files, see the comment at the end

print("Tip: It smartly creates the root folder so you do NOT need to make sure it exists!")
rootFolder= r"D:\_PythonTempTest\05"

import os

if not os.path.exists(rootFolder):
    os.mkdir(rootFolder)

# Start creating your calender
print("Starting creating... ")
for month in range(12):
    monthFolder = rootFolder + '\\' + str(month+1)
    if not os.path.exists(monthFolder):
        os.mkdir(monthFolder)
    for day in range(30):
        filename = monthFolder + '\\' + str(day+1) + '.txt'
        f = open(filename, "a")
        f.write(str(day+1) + '.' + str(month+1) + '.2020')
        f.close()
os.remove(filename) # Since the last month is 29 days so we deleted the day 30
# End of this example

print("Do you want to delete files? See the commented lines")

'''
# First delete garbages that was created last time
for month in os.listdir(rootFolder):
    monthFolder = rootFolder + '\\' + month
    for day in os.listdir(monthFolder):
        filename = monthFolder + "\\" + day
        os.remove(filename)
        print("Delete file", filename)
    os.rmdir(monthFolder)
    print("Delete folder", monthFolder)

# Do not use this method it removes the mother folder!
#for i in range(12):
    #print(rootFolder + "\\" + str(i+1) + "\\")
    #os.removedirs(rootFolder + "\\" + str(i+1) + "\\")
'''

