#!/usr/bin/env python3
# encoding: utf-8

def write_file(filename, contents):
	try:
		with open(filename, 'w') as f:
			f.write(contents)
		return True
	except Exception:
		return False
	
		
def log(filename, contents):
	try:
		with open(filename, 'a+') as f:
			f.write(contents)
		return True
	except Exception:
		return False
		
def read_file(filename):
	try:
		with open(filename, 'r') as f:
			file_contents = f.read()
			return file_contents
	except Exception:
		return ""
		
if __name__ == '__main__':
	print("This is a file used by PyEdit. Run main.py to run PyEdit.")