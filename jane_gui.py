
import tkinter as tk 

import system_stats

class Jane_Gui:
	def __init__(self, master):
		frame = tk.Frame(master)
		frame.pack()
		textbox = tk.Text(frame)
		textbox.pack()
		textbox.insert(tk.END, "Welcome to the Jane GUI! \n\n")
		textbox.insert(tk.END, "Your system stats: \n")
		stat_str = system_stats.sys_stats()
		textbox.insert(tk.END, stat_str)
		textbox.insert(tk.END, "\n\n Pretty decent system!")

root = tk.Tk()
root.title("Jane")
jane_gui = Jane_Gui(root)

root.mainloop()
