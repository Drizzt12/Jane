try:
	import psutil
	utils_found = True
except:
	print("psutil not installed. Use: pip install psutil")
	utils_found = False

def sys_stats():
	if utils_found:
		return "Got it."
	else:
		return "Nope."
