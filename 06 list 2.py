# How to check if an item is in a list

myWeekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print("Monday" in myWeekdays) # Look at the terminal. It must say True

# Lets do some actions with it

if 'Monday' in myWeekdays:
    print("Removing Monday from my list ...")
    myWeekdays.remove("Monday")

print(myWeekdays)

# Lets add Monday back to the list

if 'Monday' not in myWeekdays:
    print("Removing Monday from my list ...")
    myWeekdays.append("Monday") # WRONG: It adds Monday to the end of the list

print(myWeekdays)


