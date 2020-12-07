# This creates an empty calendar 
#   12 folders for months
#   30 empty files for days

print("Note: Befor running make sure folder 04 exists!")

import os
rootfolder= r"D:\_PythonTempTest\04"
for month in range(12):
    monthFolder = rootfolder + '\\' + str(month+1)
    os.mkdir(monthFolder)
    for day in range(30):
        filename = monthFolder + '\\' + str(day+1) + '.txt'
        open(filename, "a")
os.remove(filename) # Since the last month is 29 days so we deleted the day 30
# End of this example
        
    