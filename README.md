# Python 101-03 Collection

There are two ways you can get the list of installed packages on python.
Using help function. You can use help function in python to get the list of modules installed. Get into python prompt and type the following command. help("modules") ...
using python-pip. sudo apt-get install python-pip. pip freeze.
3rd way: use pip3 list


## Review
============== 1 ==============

    open()                                  # Create file
    import os                               # To use rename(), mkdir(), ...
    r"mystring"                             # Put r for raw string to ignore \ operators
    path + r'\' + filename                  # Put r for raw string to ignore \ operators
    path + '\\' + filename                  # Escape the backslashes
    os.rename()                             # Rename path, filename, extension
    os.mkdir()                              # Make folder
    os.rmdir()                              # Remove folder; Can remove only empty folder
    os.remove()                             # Remove file
    os.removedirs()                         # Remove folders AND the current empty folder 

============== 2 ==============

    print(str)
    print(str + str)
    print(str, int, str)
    for i in range(n):
    str(int)
    int(str)

============== 3 ==============

    os.listdir()
    for item in items:
    for itme in os.listdir():
    filePath.endswith('.pdf')
    os.path.splitext(myfilename)[0]         # returns the filename
    os.path.splitext(myfilename)[1]         # returns the .extension

============== 4 ==============

    os.remove()                             # Remove file

============== 5 ==============

    f.write()                               # write to file
    os.path.exists(myFolderPath)            # if a file exists
    if not os.path.exists(myFolderPath):    # without last \\

============== 6 ==============

    str2 = str1 + str(int(myStrAge) + 100)  # adding 100 to a string number

============== 7 ==============

    open()
    f = open()
    f.read()
    f.read(n)
    f.readline()
    print(f.read())
    f.write()
    f.close()
    os.remove()
    with
    join()

============== 8 ==============    

## Read More
### Python.org

[Naming rules](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names "Naming Rules")

[Keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)

[Escape sequences](https://docs.python.org/2.0/ref/strings.html)

[math](https://docs.python.org/3/library/math.html)

[List form range](https://docs.python.org/3/library/stdtypes.html#list)


## Tips
1. skip newline using \ (without it, it would go down a line each line)

print("""\

2. Out of range trick

msg = "hi"

#print(msg[42]) #doesn't work

print(msg[42:43]) #works 


3. operations that appear to change string actually replace:

#Java is actually coffee (contrary to popular belief).

coffee += " (contrary to popular belief)."

print(coffee)


4. ########## RANGE FUNCTION ##########

#instead of iterating through a list, we can use a function called range

#This loop runs 10 times

    for i in range(10):

        print("loading...", end= " ")

    print()


5. #We can count 1-10 instead of 0-9 if desired:

for i in range (1, 11):

    print(i, end=" ")

print()


6. #The third argument is called the step. we can set it to whatever

#Count down from 100 to 0, by 10s.

#100 included. -1 not included

for i in range (100, -1, -10):

    print(i, end=" ")

print()


### Print
7. ########## PRINT WITHOUT NEWLINE ##########

print("One", end=" ")

print("Line")

#You could alternatively use end="\t" or end="" or whatever you want.


8.########## LIST FROM RANGE ##########

#We can make the range an official list using the list ctor

#https://docs.python.org/3/library/stdtypes.html#list

numbers = list(range(1, 11))

print(numbers)




[README Markdown Guide](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Completed reading to the end of 
https://github.com/CalebCurry/python/blob/master/beginner_python/06-loop-basics.py
