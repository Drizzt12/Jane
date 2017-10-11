import shelve
c = shelve.open("Calories")
from datetime import datetime
now = datetime.now()
month = now.month
year = now.year
day = now.day
date = str(month) + "/" + str(day) + "/" + str(year)
yesterday = str(month) + "/" + str(day-1) + "/" + str(year)
print "In the month/day/year format, today is: ", date
print "Welcome to your calorie tracker!"
todayc = c[date]
todayneeded = 2600-todayc
print "you had", c[yesterday],"calories yesterday"
print "You have had", todayc,"calories today."
print "You need", todayneeded,"calories for the rest of today."
x=0
while x!="quit":
	print "what would you like to do?"
	print "valid answers are 'add' 'subtract' 'data', 'amount', and 'quit'"
	x = raw_input(">>> ")
	todayc = c[date]
	todayneeded = 2600-todayc
	if x=="quit":
		print "Bye!"
	elif x=="data":
		print "Yogurt: 140C, Peach Yogurt: 180C"
		print "Slice of bread: 90C, Sandwich: 200C"
		print "Banana: 105C, Apple: 95C"
		print "Bowl of cereal: 125C, Bowl of oatmeal: 150C"
		print "Large Egg: 78C, Small pancake: 64C"
		print "1 Cup of spaghetti: 221C, Can of lentil soup: 317C"
		print "1 oz of corn chips: 147C, 1 oz of potato chips: 152C"
		print "One medium carrot: 25C, One tablespoon of hummus: 25C"
		print "One multigrain cracker: 10C, Three meat biggie at twisters: 650C"
		print "Twisters Breakfast burrito: 400C, Taco: 156C"
		print "Hot Dog: 170C"
	elif x=="add":
		try:
			add = input("How many calories would you like to add? ")
			c[date] = todayc+add
		except NameError:
			print "Sorry, I do not understand."
		print "ok."
	elif x=="subtract":
		try:
			subtract = input("How many calories would you like to remove? ")
			c[date] = todayc-subtract
		except NameError:
			print "Sorry, I do not understand."
		print "ok."
	elif x=="amount":
		print "you have had", todayc,"calories today."
		print "you need", todayneeded,"calories for the rest of today."
		 
		 
