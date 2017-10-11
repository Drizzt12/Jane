import shelve
x = shelve.open("KnownPeople")
print x
repeat=True
while repeat:
	name = raw_input("Type in the name of the person who you want to edit, or type 'quit' without the quotations to quit: ")
	if x.has_key(name):
		age = raw_input("Type in their current age: ")
		x[name] = age
	if name=="quit":
		repeat=False
	else:
		print "Incorrect name"
