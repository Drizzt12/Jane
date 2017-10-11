import cmd, os
from collections import defaultdict
from code import InteractiveConsole, InteractiveInterpreter

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

	""" help_ entries """
	def help_shell(self):
		print("Run a bash command.")

	def help_exit(self):
		print("Exit the interpreter.")

jshell = jane_shell()
jshell.cmdloop()