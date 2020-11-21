# Python 101-03 Collection


[README Markdown Guide](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)





## Read More


### Python.org


[Naming rules](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names "Naming Rules")



[Keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)


[Escape sequences](https://docs.python.org/2.0/ref/strings.html)

[math](https://docs.python.org/3/library/math.html)


## Tips
#skip newline using \ (without it, it would go down a line each line)
print("""\

msg = "hi"
#print(msg[42]) #doesn't work
print(msg[42:43]) #works 



#operations that appear to change string actually replace:
#Java is actually coffee (contrary to popular belief).
coffee += " (contrary to popular belief)."
print(coffee)



########## RANGE FUNCTION ##########


#instead of iterating through a list, we can use a function called range
#This loop runs 10 times
for i in range(10):
    print("loading...", end= " ")
print()


#We can count 1-10 instead of 0-9 if desired:
for i in range (1, 11):
    print(i, end=" ")
print()

#The third argument is called the step. we can set it to whatever
#Count down from 100 to 0, by 10s.
#100 included. -1 not included
for i in range (100, -1, -10):
    print(i, end=" ")
print()

### Print
########## PRINT WITHOUT NEWLINE ##########

print("One", end=" ")
print("Line")
#You could alternatively use end="\t" or end="" or whatever you want.
