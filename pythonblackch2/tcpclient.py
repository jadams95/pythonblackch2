import socket

# initalizing variables
target_host = 'ellasgourmet.net'
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: ellasgourmet.net\r\n\r\n")

# receive some data
response = client.recv(4096)

print response