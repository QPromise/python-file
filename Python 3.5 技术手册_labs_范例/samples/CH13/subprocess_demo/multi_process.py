import sys, subprocess

ps = [
    subprocess.Popen(
	    ['python', 'one_process.py', filename], 
		stdout=subprocess.PIPE
	) for filename in sys.argv[1:]
]

count = 0
for p in ps:
    count += int(p.stdout.read())

print(count)	
