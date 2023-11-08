#!/usr/bin/env python3
# encoding: utf-8

import curses, sys, os
from uielements import UIElements




class unixcolors:
	# Colors for Unix
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	END = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	# Shorthand for 'underline'
	UL = '\033[4m'

def cursor_to_bottom(win):
	
	# Hide cursor
	# curses.curs_set(0)
	
	height, width = win.getmaxyx()
	
	win.move(height - 1, 0)
	win.clrtoeol()
	
	win.refresh()
	
	# win.getch()
	
def return_to_top(win, togo_y, togo_x):
	y, x = win.getyx()
	win.move(curses.LINES - 1, 0)
	win.clrtoeol()
	
	win.move(togo_y, togo_x)
	win.refresh()
	
def handleargs(args):
	args = args[1:] # Ignore first argument, which is the script name
	match_list = ["-h", "--help", "-l", "-v", "--verbose"]#
	notInList = 0
	for i in args:
		if i not in match_list:
			notInList += 1
			if notInList >= 2:
				print(unixcolors.BOLD + unixcolors.RED + "Error:"+unixcolors.END+" argument "+i+" not found.")
				sys.exit()
	
	try:
		if args[0] == "--help" or args[0] == "-h" or args[0] == "-?":
			UIElements.help()
		else:
			if os.path.exists(args[0]) and os.path.isfile(args[0]) != True:
				print(unixcolors.RED + unixcolors.BOLD + "Error: "+unixcolors.END+args[0]+" is a directory, not a file.")
				print("Files inside "+args[0]+":")
				# run(["ls", args[0]])
				ver = sys.version.split(".")[0]
				if ver == "2":
					import python2utils as verTils
				else:
					import python3utils as verTils

				verTils.run(["ls", args[0]])
				sys.exit()
			else:
				return True
	except IndexError: # No argument
		return True



	
if __name__ == '__main__':
	print("This is a file used by PyEdit. Run main.py to run PyEdit.")