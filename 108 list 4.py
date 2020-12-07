#00:18:24 - Intro to LIst Comprehension

print(range(1,11))
print(list(range(1,11)))



########## FOR LOOP WITH INDEX ##########
 
languages = ["Python", "C++", "Java"]
for i in range(len(languages)):
    print(i, languages[i])

#len will return 3. Passing 3 to range gives us 0, 1, 2