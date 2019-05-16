import urllib.request
import sys

if len(sys.argv) < 3:
	sys.exit("Usage " + sys.argv[0] + "<hostname> <port> \n")

host = sys.argv[1]
port = sys.argv[2]

client = http.client.HTTPSConnection(host, port)
client.HTTPSConnection.request("GET", "/")
resp = client.getresponse()
client.close()
if resp.status == 200:
	print(host + ":Ok")

sys.exit()
print(host + ":Down('+ resp.status', 'resp.reason +')")