# Import socket module
import pyautogui
import socket

# Create a socket object
s = socket.socket()
print ('kdjsafhklajsfh\n')
# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('192.168.1.8', port))

# receive data from the server
message = s.recv(30)
datums = str(message).split("$")
x = int(datums[1])
y = int(datums[2])
print (x)
print (y)
pyautogui.moveTo(x,y)
# close the connection
s.close()
