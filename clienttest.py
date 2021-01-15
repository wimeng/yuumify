# Import socket module
import socket

# Create a socket object
s = socket.socket()
print ('kdjsafhklajsfh\n')
# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('192.168.1.8', port))

# receive data from the server
message = s.recv(1024)
print (str(message))
# close the connection
s.close()
