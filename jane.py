import cmd, os
from collections import defaultdict
from code import InteractiveConsole, InteractiveInterpreter
import plistlib

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
		try:
			# Copied from python playground book to see if it works and figure out how
			fileName = s
			print("Finding duplicate tracks in %s..." %fileName)
			# Read playlist
			plist = plistlib.readPlist(fileName)
			# Get tracks
			tracks = plist["Tracks"]
			# Create a track name directory
			trackNames = {}
			# iterate through the tracks
			for trackId, track in tracks.items():
				try:
					name = track["Name"]
					duration = track["Total Time"]
					# look for existing entries
					if name in trackNames:
						# if a name and duration match, increment the count
						# round the track length to the nearest second
						if duration//1000 == trackNames[name][0]//1000:
							count = trackNames[name][1]
							trackNames[name] = (duration, count+1)
					else:
						# add dictionary entry as tuple (duration, count)
						trackNames[name] = (duration, 1)
				except:
					# ignore
					pass
			print trackNames
		except:
			print("Please enter a music playlist name")

	""" help_ entries """
	def help_shell(self):
		print("Run a bash command.")

	def help_exit(self):
		print("Exit the interpreter.")

	def help_py(self):
		print("Run an embedded python interpreter with persistant state.")

	def help_music(self):
		print("Print out all of the songs in an iTunes playlist.")

jshell = jane_shell()
jshell.cmdloop()
