import cmd, os

class jane_shell(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = "jane: "
		self.intro = "Hello, welcome to the Jane AI.  How may I serve you?"

	def emptyline(self):
		pass

	""" do_ commands """
	def do_shell(self, s):
		os.system(s)

	def do_exit(self, s):
		return True

	""" help_ entries """
	def help_shell(self):
		print("Run a bash command.")

	def help_exit(self):
		print("Exit the interpreter.")

jshell = jane_shell()
jshell.cmdloop()