# This creates multiple files
print("*** Note ***: Befor running make sure folder 02 exists!")
for i in range(10): # Pay attention to the ending with :
    completeFileName = "D:\\_PythonTempTest\\02\\" + str(i) + ".txt" # Wrap i with str() to get a string
    open(completeFileName, "a")
# End of this example.