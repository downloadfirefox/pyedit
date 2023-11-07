#!/usr/bin/env python3
# encoding: utf-8

import curses, sys, os
from uielements import UIElements

def printin(inp):
	# Print inline
	print(inp, end="", flush=True)


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
	match_list = ["-h", "--help", "-l", "-v", "--verbose"]
	for i in args:
		if i not in match_list:
			print(unixcolors.BOLD + unixcolors.RED + "Error:"+unixcolors.END+" argument "+i+" not found.")
			sys.exit()
	
	try:
		if args[1] == "--help" or args[1] == "-h" or args[1] == "-?":
			UIElements.help()
		else:
			if os.path.exists(args[1]) and os.path.isfile(args[1]) != True:
				print(utils.unixcolors.RED + utils.unixcolors.BOLD + "Error: "+utils.unixcolors.END+args[1]+" is a directory, not a file.")
				from subprocess import run
				print("Files inside "+args[1]+":")
				run(["ls", args[1]])
				sys.exit()
			else:
				return True
	except IndexError: # No argument
		return True
				
	
if __name__ == '__main__':
	print("This is a file used by PyEdit. Run main.py to run PyEdit.")