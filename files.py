#!/usr/bin/env python3
# encoding: utf-8

def write_file(filename, contents):
	try:
		f = open(filename, 'w')
		f.write(contents)
		f.close()
		return True
	except Exception:
		return False
	
		
def log(filename, contents):
	try:
		f1 = open(filename, 'a+')
		f1.write(contents)
		f1.close()
		return True
	except Exception:
		return False
		
def read_file(filename):
	try:
		f2 = open(filename)
		file_contents = f2.read()
		return file_contents
	except Exception:
		return ""
		
if __name__ == '__main__':
	print("This is a file used by PyEdit. Run main.py to run PyEdit.")