try:
	import psutil
	utils_found = True
except:
	print("psutil not installed. Use: pip install psutil")
	utils_found = False

def sys_stats():
	if utils_found:
		outstr = ""

		cpus = psutil.cpu_count(logical=False)
		vcpus = psutil.cpu_count()
		cpu_speed = psutil.cpu_freq().current
		memory = psutil.virtual_memory().total
		percent_mem = psutil.virtual_memory().percent
		free_disk = psutil.disk_usage('/').free

		outstr += "Physical CPUS: " + str(cpus) + "\n"
		outstr += "Virtual CPUS: " + str(vcpus) + "\n"
		outstr += "CPU speed: " + str(cpu_speed) + " mhz \n"
		outstr += "Virtual Memory: " + str(memory) + " bytes \n"
		outstr += "Percent free: " + str(percent_mem) + "%\n"
		outstr += "Disk space free: " + str(free_disk) + " bytes \n"

		return outstr


	else:
		return "psutil not installed.  Use: pip install psutil"
