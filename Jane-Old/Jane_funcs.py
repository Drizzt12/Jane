print "importing required modules..."
import shelve
print "Shelve module successfully imported..."
import time
print "Time module successfully imported..."
from time import sleep
print "Sleep module successfully imported..."
from random import randrange
print "Randomizer module successfully imported..."
from google import search
print "Internet Browsing module successfully imported..."
print "Setting up required functions..."
def Introduction():
	x = shelve.open("KnownPeople")
	print "Hello! My name is Jane, I am an artificial intelligence program designed and created by Eirik Mulder."
	print "What is your name?"
	name = raw_input("> ")
	if name=="Eirik_":
		print "Hello admin."
	else:
		name = subs(name,True)
		nameC = name.capitalize()
		if x.has_key(name):
			print "Hello", nameC+",","I know you!"
		else:
			print "Hello", nameC+",","I don't remember meeting you, how old are you?"
			NotNumber=True
			while NotNumber:
				try:
					age = raw_input("> ")
					if age=="n":
						print "ok"
						NotNumber=False
					else:	
						int(age)
						NotNumber=False
				except AttributeError:
					print "Can you please type a number? Type 'n' without the quotations if you would not like to specify."
					NotNumber=True
			PrintedName=nameC+"."
			print "Nice to meet you,", PrintedName
			x[name] = age
			return name
def subs(x,y)
	if not y:
		x = x.lower()
		x = x.translate(None, "!?;,.'`~/*+)(-:")
		x = x.replace("hey jane","")
		x = x.replace("jane","")
		x = x.replace("today","")
		x = x.replace("hey","hello")
		x = x.replace("hi","hello")
		x = x.replace("howdy","hello")
		x = x.replace("xd","lol")
		x = x.replace("ya","you")
		x = x.replace("ye","you")
		x = x.replace("yee","you")
		x = x.replace("great","good")
		x = x.replace("well","good")
		x = x.replace("mornin","morning")
		x = x.replace("how long have you lived","how old are you")
		x = x.replace("thank you","thanks")
		x = x.replace("thx","thanks")
		x = x.replace("love","like")
		x = x.replace("dirt bikes","dirtbikes")
		x = x.replace("dirt bike","dirtbike")
		x = x.replace("exhausted","tired")
		x = x.replace("very","")
		x = x.replace("terrible","bad")
		x = x.replace("horrible","bad")
		x = x.replace("bout","about")
		x = x.replace("see you later","byou")
		x = x.replace("i have to go","byou")
		x = x.replace("helo","hello")
		x = x.replace("see you","byou")
		x = x.replace("too","to")
		x = x.replace("open","")
		x = x.replace("the","")
		x = x.strip()
		return x
	if y:
		x = x.lower()
		x = x.translate(None, "!?;,.'`~/*+-")
		x = x.replace("jane","")
		x = x.replace("today","")
		x = x.replace("hey","hello")
		x = x.replace("hi","hello")
		x = x.replace("howdy","hello")
		x = x.replace("xd","lol")
		x = x.replace("ya","you")
		x = x.replace("ye","you")
		x = x.replace("yee","you")
		x = x.replace("great","good")
		x = x.replace("well","good")
		x = x.replace("mornin","morning")
		x = x.replace("how long have you lived","how old are you")
		x = x.replace("thank you","thanks")
		x = x.replace("thx","thanks")
		x = x.replace("love","like")
		x = x.replace("dirt bikes","dirtbikes")
		x = x.replace("dirt bike","dirtbike")
		x = x.replace("im ","")
		x = x.replace("doing ","")
		x = x.replace("i am ","")
		x = x.replace("thanks ","")
		x = x.replace("exhausted","tired")
		x = x.replace("sad","bad")
		x = x.replace("terrible","bad")
		x = x.replace("devastated","bad")
		x = x.replace("ever","")
		x = x.replace("viewed","seen")
		x = x.replace("and","an")
		x = x.replace("fine","good")
		x = x.strip()
		return x
def math(x):
	x = subs(x,False)
	x = x.replace("what is ","")
	x = x.replace("solve ","")
	x = x.replace("the answer to ","")
	x = x.replace("hmm ","")
	print x
def moodteller(x):
	x = subs(x,False)
	x = subs(x,True)
	if x == "good":
		print "That's good!"
	elif x == "tired":
		print "I'm sorry you feel tired."
	elif x == "bad":
		print "I'm sorry you feel bad."
	elif x == "excited":
		print "I'm glad you feel that way!"
def Parse(x,name):
	quit = False
	replies = shelve.open("responses")
	replies2 = shelve.open("responses2")
	replies3 = shelve.open("responses3")
	sc = {"hello":"Hi!, how are you today?"}
	x = subs(x,False)
	if x == "quit" or x == "goodbyou" or x == "i have to go now" or x=="byou" or x == "i have to go now ":
		quit = True
	elif x == "math":
		print "You can now ask me math problems, but nothing else. Type exit to go back to normal mode"
		x = raw_input(">>> ")
		math(x)
		while x != "exit":
			x = raw_input(">>> ")
			math(x)
	elif x == "what day is it":
		print time.strftime("Day %d, of month %m, of %y")
	elif x == "what time is it":
		from datetime import datetime
		now = datetime.now()
		if now.hour > 12:
			hour = now.hour-12
			pm = True
		else:
			hour = now.hour
			pm = False
		if pm:
			time = str(hour) + ":" + str("%02d" % now.minute) +" PM"
		if not pm:
			time = str(hour) + ":" + str("%02d" % now.minute) +" AM"
		print time
	elif x== "calorie tracker":
		print "loading calorie tracker..."
		import Calorie_Tracker
	elif x=="search":
		print "what would you like to search google for?"
		google = raw_input(">>> ")
		print "the URLs I got were:"
		for url in search(google, stop=10):
			print url
		print "you can copy paste URLs into your web browser to see contents"
	elif sc.has_key(x):
		print sc[x]
		subs(sc[x],False)
		answer = raw_input("> ")
		if sc[x] == "Hi!, how are you today?":
			moodteller(answer)
	elif replies.has_key(x):
		randomreply=randrange(1,4)
		if randomreply == 1:
			print replies[x]
		elif randomreply == 2:
			print replies2[x]
		elif randomreply == 3:
			print replies3[x]
	else:
		incorrect = True
		while incorrect:
			print "The response to that phrase is not in my database."
			print "This could either be because you mistyped something, or because I havn't learned it yet."
			print "If you mistyped something, type in 'n' without the quotations, and if you would like me to learn it, type in 'y' without the quotations"
			mistype = raw_input(">>> ")
			x = x.lower()
			x = x.translate(None, "!?;,.'`~/*+)(-:")
			x = x.strip()
			if mistype == "y":
				print "Because I am a learning program, could you type in the three best answers to that statement or question."
				reply=raw_input("> ")
				reply2=raw_input("> ")
				reply3=raw_input("> ")
				replies[x] = reply
				replies2[x] = reply2
				replies3[x] = reply3
				incorrect=False
			elif mistype == "n":
				print "ok!"
				incorrect=False
			else:
				print "that is not one of the answers this question accepts..."
	return quit
def Exit():
	print "Goodbye!"
	return True
def RunCode():
	name = Introduction()
	quit = False
	while quit is not True:
		x = raw_input("> ")
		quit = Parse(x, name)
	Exit()


