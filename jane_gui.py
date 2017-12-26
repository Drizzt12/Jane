
import Tkinter as tk 

class Jane_Gui:
	def __init__(self, master):
		frame = tk.Frame(master)
		frame.pack()
		textbox = tk.Text(frame)
		textbox.pack()
		textbox.insert(tk.END, "Welcome to the Jane GUI!")

root = tk.Tk()
jane_gui = Jane_Gui(root)

root.mainloop()
