#!/usr/bin/env python3
# encoding: utf-8

import signal, sys, os, tests, utils, files, curses
from uielements import UIElements
from datetime import datetime

def checkVersion():
    ver = sys.version.split(".")[0]
    if ver == "2":
        import python2utils as verTils
    else:
        import python3utils as verTils
        
checkVersion()

def editor(win, args):
	# Read file
	try:
		file_contents = files.read_file(args[1])
		total = file_contents
		
	except IndexError:
		file_contents, total = "", ""
		
	
	filename = UIElements.titlebar(win, args)
	
	
	current_y, current_x = win.getyx()
	win.addstr(current_y, current_x, file_contents)
	current_y, current_x = win.getyx()
	win.move(current_y-1, len(total.split('\n')[current_x])+1)
	current_y, current_x = win.getyx()
	
	# Move to below the titlebar
	win.move(1, 0)
	win.refresh()
	
	def ctrlchandler(*args):
		height, width = win.getmaxyx()
		win.move(height - 1, 0)
		win.clrtoeol()
		print('\a') # Ring the bell
		win.addstr(height-1, 0, "Use /quit or /q (followed by ENTER) to quit PyEdit")
		win.refresh()
		win.move(current_y, current_x)
		
	signal.signal(signal.SIGINT, ctrlchandler)
	signal.signal(signal.SIG_IGN, ctrlchandler)
	
	# tests.test_colors(win)
	while True:
		ch = win.getch()
		current_y, current_x = win.getyx()
		if ch != -1: # If it is an actual key we want
			if ch == curses.KEY_RIGHT:
				lines = total.split('\n')
				if len(lines[current_y-1]) <= current_x:
					verTils.printin('\a')
				else:
					win.move(current_y, current_x+1)
			elif ch == curses.KEY_LEFT:
				if current_x == 0:
					if current_y > 1:
						win.move(current_y-1, len(total.split('\n')[current_x])+1)
					else:
						verTils.printin('\a')
				else:
					win.move(current_y, current_x-1)
			elif ch == curses.KEY_DOWN:
				lines = total.split('\n')
				if len(lines) > current_y:
					win.move(current_y+1, current_x)
					while len(lines[current_y-1]) >= current_x:
						win.move(current_y, current_x-1)
				else:
					verTils.printin('\a')
			elif ch == curses.KEY_UP:
				if current_y > 1:
					lines = total.split('\n')
					win.move(current_y-1, current_x)
					while len(lines[current_y-1]) >= current_x:
						win.move(current_y, current_x-1)
				else:
					verTils.printin('\a')
			elif ch == 10: # Enter
				win.addch('\n')
				lines = total.split('\n')
				current_y -= 1
				lines[current_y] = lines[current_y][:current_x] + '\n' + lines[current_y][current_x:]
				current_y += 1
				total = '\n'.join(lines)
				
			elif ch == 8 or ch == 127: # Backspace
				if current_x == 0:
					if current_y > 1:
						win.move(current_y-1, len(total.split('\n')[current_x])+1)
						current_y, current_x = win.getyx()
						lines = total.split('\n')
						current_y -= 1
						lines[current_y] = lines[current_y] + lines[current_y + 1]
						lines.pop(current_y + 1)
						total = '\n'.join(lines)
						current_y, current_x = win.getyx()
					else:
						verTils.printin('\a')
				if current_x > 0 and current_x <= len(total):
					lines = total.split('\n')
					current_y -= 1
					lines[current_y] = lines[current_y][:current_x - 1] + lines[current_y][current_x:]
					current_y += 1
					total = '\n'.join(lines)
					# total = total[:current_x - 1] + total[current_x:]
					files.log('pyedit_LOG.log', str(datetime.now())+" | TOTAL (BACKSPACE): " + total.replace('\n', '[LN]') + "\n")
					
				
				if current_x > 0:
					win.move(current_y, current_x - 1)
					win.delch()
					
			elif ch == ord('/'): # Handle commands
				# TODO: add left/right arrow keys
				utils.cursor_to_bottom(win)
				win.addch(ch)
				def slashString(content):
					y, x = win.getyx()
					win.addstr(y-1, x-1, content)
					win.move(y, x)
				slashString("Press / again to type")
				command = []
				while True:
					ch = win.getch()
					
					if ch != -1:
						slashString("                      ") # Erase message
						if ch == ord('/'):
							utils.return_to_top(win, current_y, current_x)
							win.addstr(current_y, current_x, "/")
							break
						elif ch == 10: # Enter key
							final = ''.join(command)
							
							if final == "quit" or final == "q":
								# verTils.printin(utils.unixcolors.BOLD + "Quitting..." + utils.unixcolors.END)
								# Save prompt
								try:
									justavariabletoseeifthisexists = args[1]
									if total != file_contents+'\n':
										res = UIElements.save_prompt(win, filename, total)
									else:
										res = False
								except IndexError: # No, sir
									if total != "" and total != "\n":
										res = UIElements.save_prompt(win, filename, total)
									else:
										res = False
								
								# files.write_file("pyedit_LOG.log", "")
								if res != True:
									curses.endwin()
									win.clear()
									sys.exit()
								elif res == True:
									utils.return_to_top(win, current_y, current_x)
									break
							else:
								utils.return_to_top(win, current_y, current_x)
								break
						elif ch == 8 or ch == 127: # Backspace or Delete
							if not command: # If array is empty
								pass
							else:
								command.pop() # Get rid of last item in array
							
							y, x = win.getyx()
							if x > 0:
								win.move(y, x - 1)
								win.delch()
						elif ch == 27: # Esc
							utils.return_to_top(win, current_y, current_x)
							break
						else:
							win.addch(ch)
							command.append(chr(ch))
			else:
				win.addch(ch)
				lines = total.split('\n')
				current_y -= 1
				lines[current_y] = lines[current_y][:current_x] + chr(ch) + lines[current_y][current_x:]
				current_y += 1
				total = '\n'.join(lines)
				# total = total[:current_x] + chr(ch) + total[current_x:]
				files.log('pyedit_LOG.log', str(datetime.now())+" | TOTAL (CHARACTER "+chr(ch)+" ADDED): " + total.replace('\n', '[LN]') + " | X: " + str(current_x) + " Y: "+str(current_y-1)+"\n")
				
	curses.endwin()
	
if __name__ == '__main__':
	print("This is a file used by PyEdit. Run main.py to run PyEdit.")
