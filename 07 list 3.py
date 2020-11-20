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


