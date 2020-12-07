# Intro to list
# Overview
# list 1    define, append, len
# list 2    in, not in, remove

weekdays = ['Monday', "Tuesday", 'Wednesday', "Thursday", "Friday", 'Saturday'] # Single and double qoute work
print(weekdays)
# oops I forgot Sunday. This is the way we add it
weekdays.append("Sunday")
print(weekdays)
# We must have 7 days. Lets check it
print(len(weekdays))
# Or better you can say
print("The number of days I added to the list is", len(weekdays)) # Do not use +! use comma!