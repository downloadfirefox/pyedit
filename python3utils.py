def printin(inp):
	# Print inline
	print(inp, end="", flush=True)

def cprint(hi):
    print(hi)
    
def run(arr):
    from subprocess import run as subr
    return subr(arr)