import cmd, os
import sys
from collections import defaultdict
from code import InteractiveConsole, InteractiveInterpreter
from lifxlan import BLUE, COLD_WHITE, CYAN, GOLD, GREEN, LifxLAN, \
    ORANGE, PINK, PURPLE, RED, WARM_WHITE, WHITE, YELLOW
lifxlan = LifxLAN
#Needs python 2 -> import commands

class EmbeddedConsoleExit(SystemExit):
	pass

"""
Jane class based on the Cmd module.
Documentation on how to add things can be found here:
https://wiki.python.org/moin/CmdModule
"""
class jane_shell(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = "jane: "
		self.intro = "Hello, welcome to the Jane AI.  How may I serve you?"
		self.vars = defaultdict(dict)
		self.pystate = {}
		print("Loading plugins...")


	def emptyline(self):
		pass

	""" do_ commands """
	def do_shell(self, s):
		os.system(s)

	def do_exit(self, s):
		return True

	def do_py(self, s):
		self.pystate['self'] = self
		for v in self.vars:
			self.pystate[v] = self.vars[v]
		interp = InteractiveConsole(locals=self.pystate)

		def quit():
			raise EmbeddedConsoleExit
		self.pystate['quit'] = quit
		self.pystate['exit'] = quit
		try:
			interp.interact(banner="Python Interactive Shell within Jane.")
		except EmbeddedConsoleExit:
			pass

	def do_music(self, s):
		print("Sorry, this service is unavailable")
#		artist=commands.getoutput("osascript -e 'tell application \"iTunes\" to artist of current track as string'")
#		print(artist)
#		artist = artist.split("\n")
#		artist = str(artist[1])
#		track=commands.getoutput("osascript -e 'tell application \"iTunes\" to name of current track as string'")
#		track = track.split("\n")
#		track = str(track[1])
#		state=commands.getoutput("osascript -e 'tell application \"iTunes\" to player state as string'")
#		state = state.split("\n")
#		state = str(state[1])
#		currentvolume=commands.getoutput("osascript -e 'tell application \"iTunes\" to sound volume as integer'")
#		currentvolume = currentvolume.split("\n")
#		currentvolume = str(currentvolume[1])
#		if s == "play":
#			if state == "paused":
#				print("Playing your current track")
#				commands.getoutput("osascript -e 'tell application \"iTunes\" to play'")
#				print("Currently playing: '%s' by '%s'" % (track, artist))
#			elif state == "playing":
#				print("Already playing")
#			else:
#				print("No track selected")
#		elif s == "pause":
#			if state == "playing":
#				commands.getoutput("osascript -e 'tell application \"iTunes\" to pause'")
#				print("Paused")
#			elif state == "paused":
#				print("Already paused")
#		elif s[:8] == "favorite":
#			music.fav()
#		elif s[:3] == "all":
#			music.print_all()

	def do_lights(self, s):
		colors = {
		    "red": RED,
		    "orange": ORANGE,
		    "yellow": YELLOW,
		    "green": GREEN,
		    "cyan": CYAN,
		    "blue": BLUE,
		    "purple": PURPLE,
		    "pink": PINK,
		    "white": WHITE,
		    "cold_white": COLD_WHITE,
		    "warm_white": WARM_WHITE,
		    "gold": GOLD
		}
		color = None
		if len(s) == 2:
		    if s[1].lower() not in colors:
		        print(error_message)
		        sys.exit()
		    else:
		        color = colors[s[1].lower()]
		elif len(s) == 5:
		    color = []
		    for (i, value) in enumerate(s[1:]):
		        try:
		            value = int(value)
		        except:
		            print("Problem with {}.".format(value))
		            print(error_message)
		            sys.exit()
		        if i == 3 and (value < 2500 or value > 9000):
		            print("{} out of valid range.".format(value))
		            print(error_message)
		            sys.exit()
		        elif value < 0 or value > 65535:
		            print("{} out of valid range.".format(value))
		            print(error_message)
		            sys.exit()
		        color.append(value)
		else:
		    print("Fail")
		    sys.exit()

		print(color)
		lifxlan.set_color_all_lights(color, rapid=True)

	""" help_ entries """
	def help_shell(self):
		print("Run a bash command.")

	def help_exit(self):
		print("Exit the interpreter.")

	def help_py(self):
		print("Run an embedded python interpreter with persistant state.")

	def help_music(self):
		print("Unavailable, Work in Progress")

jshell = jane_shell()
jshell.cmdloop()
