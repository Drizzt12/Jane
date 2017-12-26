import cmd, os
from collections import defaultdict
from code import InteractiveConsole, InteractiveInterpreter
import commands

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
