# How to check if items of a list are in another list

# For example, we want to throw away non-healthy foods from my bag.

healthyFoods = ["Apple", "Orange"]
myBag = ["Chips", "Coca Cola", "Apple"]

myBag = [item for item in myBag if item in healthyFoods] # WOW! This is new! How does it work? Simply tt says: KEEP item for item in myBag of they are health

print(myBag)


# Warning
# #the id will change

myBag2 = ["Chips", "Coca Cola", "Apple"]
print(id(myBag2))
myBag2 = [item for item in myBag2 if item in healthyFoods] 
print(id(myBag2)) # This id is different => The orginal list did NOT changed

# if you want to change the orgonal list then do this
myBag3 = ["Chips", "Coca Cola", "Apple"]
print(id(myBag3))
myBag3[:] = [item for item in myBag3 if item in healthyFoods] # ***** IT CHANGES THE ORIGONAL LIST ****** [:] slice a list
print(id(myBag3)) # This id is different => The orginal list did NOT changed
print(myBag3)




# IMportant

name = "hassan"
#BAD
print("length is", len(name))
msg = "length is", len(name)
print(msg) #NOT WHAT WE WANTED!

#GOOD
length = len(name)
msg = "length is " + str(length)
print(msg)



#EVEN BETTER
#We can also nest function calls:
print("length is " + str(len(name)))
#The order in which these are invoked are in to out...
#len(name) is first which returns a number.
#this number is passed to str which converts it to a string
#this string is then concatenated with the string on the left
#this final string is then passed to print

#That's the end of your introduction to strings!

