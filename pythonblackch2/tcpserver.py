import socket
import threading


#Delcaring and assignment of variables
bind_ip = "127.0.0.1"
bind_port = 3333

#Calling the socket.socket object from socket module
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5)

print "[*] Listening on {0}:{1}".format(bind_ip, bind_port)

# this os our client-handling threading
def handle_client(client_socket):

	# print out what the client sends
	request = client_socket.recv(1024)
	
	print "[*] Received: {}".format(request)
	
	# send back a packet
	client_socket.send("ACK!")
	client_socket.close()

# logic for the client handler	
while True:
	client,addr = server.accept()
	print "[*] Accepted Connection from: {0}: {1}".format(addr[0], addr[1])
	
	# spin up our client thread to handle incoming data
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()