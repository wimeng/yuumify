import pyautogui
import socket
import time
import keyboard

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

while True:
    # finds the position of the mouse and sends its coordinates
    x, y = pyautogui.position()
    positionStr = '$' + str(x).rjust(4) + '$' + str(y).rjust(4) + '$'



    if (keyboard.is_pressed(']')):
        c.sendall(b'$0$0$]$')
        break;

    if (keyboard.is_pressed('n')):
        positionStr += 'n$' #left click
    if (keyboard.is_pressed('2')):
        positionStr += 'z$' #right click

    if (keyboard.is_pressed('s')):
        positionStr += 'q$' #q
    if (keyboard.is_pressed('3')):
        positionStr += 'w$' #w
    if (keyboard.is_pressed('g')):
        positionStr += 'e$' #e
    if (keyboard.is_pressed('t')):
        positionStr += 'r$' #ult
    if (keyboard.is_pressed('c')):
        positionStr += 'd$' #d
    if (keyboard.is_pressed('v')):
        positionStr += 'f$' #f
    if (keyboard.is_pressed('x')):
        positionStr += '4$' #4
    if (keyboard.is_pressed('space')):
        positionStr += 's$'

    if (keyboard.is_pressed('ctrl')):
        positionStr += 'ctrl$'

    for i in range(0, 29-len(positionStr)):
        positionStr += ' '
    positionStr += ']'


    c.sendall(positionStr.encode("ascii"))
    time.sleep(0.023)




# Close the connection with the client
c.close()
