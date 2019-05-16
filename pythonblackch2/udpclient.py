import socket

#declare variables and assignment
target_host = '192.168.1.126'
target_port = 80
Message = "Hello, Server"

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(Message, (target_host, target_port))

#receive some data
data, addr = client.recvfrom(4096)

print data