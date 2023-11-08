#!/usr/bin/env python3
# encoding: utf-8

# TODO: fix the arguments, allow them to be in any order, etc..., also add -l and --log
# TODO: add filename in save prompt
# TODO: add 'Command not found'
# TODO: hoist character input out into a function?
# TODO: change logging to be in the command bar, not a file
# TODO: add a .pyeditrc folder

# Text editor?
import curses, editor, sys, files, utils



def main(win):
	try:
		init(win)
		args = sys.argv
		editor.editor(win, args)
	except Exception:
		curses.nocbreak()
		win.keypad(False)
		curses.echo()
		curses.endwin()
		raise

def init(win):
	# Clear terminal
	files.write_file("pyedit_LOG.log", "")
	curses.noecho() # Prevent echoing of keypresses
	win.keypad(True) # Enable special keys!
	win.nodelay(1) # Enable no-blocking mode
	curses.cbreak()
	# curses.start_color()
	# Get transparency
	curses.use_default_colors()
	# Gain access to all colors (even though gnome-terminal and macOS don't properly report their support for 256 colors)
	curses.init_pair(1, 0, curses.COLOR_WHITE)
	curses.init_pair(0, curses.COLOR_WHITE, 0) # Default terminal
	
	win.clear()
	
if __name__ == "__main__":
	args = sys.argv
	if utils.handleargs(args):
		curses.wrapper(main)