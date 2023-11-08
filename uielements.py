#!/usr/bin/env python3
# encoding: utf-8
import curses, files, utils, os, sys

def checkVersion():
    ver = sys.version.split(".")[0]
    if ver == "2":
        import python2utils as verTils
    else:
        import python3utils as verTils
        
checkVersion()

class UIElements:
	@staticmethod
	def writeline(win, save_str, y, x, color):
		height, width = win.getmaxyx()
		win.move(y, x)
		str_length = len(save_str)
		whitespace_to_add = width - str_length
		# win.addstr(1, 0, str(whitespace_to_add))
		whitespace = ""
		for i in range(whitespace_to_add):
			whitespace += " "
		win.addstr(y, x, save_str+whitespace, color)
		win.refresh()
	@staticmethod
	def titlebar(win, args):
		# Find max width of screen to make a complete line
		height, width = win.getmaxyx()
		titlebar_str = "PyEdit v0.0.1-alpha - New file"
		try:
			if args[1] != "":
				if os.path.isfile(args[1]):
					titlebar_str = "PyEdit v0.0.1-alpha - "+str(args[1])
				else:
					titlebar_str = "PyEdit v0.0.1-alpha - New file: "+str(args[1])
		except Exception:
			pass
		
		UIElements.writeline(win, titlebar_str, 0, 0, curses.color_pair(1))
		try:
			return args[1]
		except Exception:
			return ""
	@staticmethod
	def save_prompt(win, filename, contents):
		height, width = win.getmaxyx()
		UIElements.writeline(win, "Do you want to save your file? [y/n/c]", height - 2, 0, curses.color_pair(1))
		utils.cursor_to_bottom(win)
		choice = win.getch()
		while choice != ord('n') and choice != ord('y') and choice != ord('c'):
			choice = win.getch()
		yn = choice
		win.addch(choice)
		while choice != 10:
			choice = win.getch()
		if yn == ord('y'):
			files.write_file(filename, contents)
			return False
		elif yn == ord('c'):
			UIElements.writeline(win, " ", height - 2, 0, curses.color_pair(0))
			return True
		else:
			return False
	@staticmethod
	def help():
		# Help message
		verTils.cprint("""PyEdit (A text editor made using Python, curses and no external libraries).
Current version: v0.0.1-alpha

Usage: pyedit [arguments] [file...] Edit a specific file
       pyedit                       Create a new file and start editing

Arguments:
       --help, -h, -?               Display this help message
       --verbose, -v                Be verbose (messages displyed above command bar)
		""")
		sys.exit()
		
if __name__ == '__main__':
	verTils.cprint("This is a file used by PyEdit. Run main.py to run PyEdit.")