import shelve
x = shelve.open("responses")
x2 = shelve.open("responses2")
x3 = shelve.open("responses3")
y2 = "when is your birthday"
x[y2] = "May 16th"
x2[y2] = "My birthday is on May 16th"
x3[y2] = "I was created on May 16th, 2016."
print "I was created on May 16th, 2016"
print "Ready for update"
y = "how old are you"
x[y] = raw_input("response1 >>> ")
x2[y] = raw_input("response2 >>> ")
x3[y] = raw_input("response3 >>> ")