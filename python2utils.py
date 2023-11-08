def printin(inp):
	# Print inline
	print inp,

def cprint(hi):
    print hi
    
def run(arr):
    from subprocess import Popen
    return Popen(arr)