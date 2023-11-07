#!/usr/bin/env python3
# encoding: utf-8

import curses

def test_colors(win):
	try:
		for i in range(8):
			curses.init_pair(i, i, 0)
			win.addstr(str(i), curses.color_pair(i))
		win.getch()
	except curses.ERR:
		# Reached end of screen
		pass
		
if __name__ == '__main__':
	# print("This is a file used by PyEdit. Run main.py to run PyEdit.")
	curses.wrapper(test_colors)