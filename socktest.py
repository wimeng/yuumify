import pyautogui
import socket

# next create a socket object
s = socket.socket()
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)
print ("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
# while True:

# Establish connection with client.
c, addr = s.accept()
print ('Got connection from', addr )

# finds the position of the mouse and sends its coordinates
x, y = pyautogui.position()
positionStr = '$' + str(x).rjust(4) + '$' + str(y).rjust(4) + '$'
for i in range(0, 29-len(positionStr)):
    positionStr += ' '
positionStr += ']'

c.sendall(positionStr.encode("ascii"))

# finds the position of the mouse and sends its coordinates
x, y = pyautogui.position()
positionStr = str(x).rjust(4)[1:] + '$' + str(y).rjust(4)[1:]
for i in range(0, 29-len(positionStr)):
    positionStr += ' '
positionStr += ']'

c.sendall(positionStr.encode("ascii"))

# Close the connection with the client
c.close()
