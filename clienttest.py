# Import socket module
import pyautogui
import socket

pyautogui.PAUSE = 0.02

# Create a socket object
s = socket.socket()
print ('kdjsafhklajsfh\n')
# Define the port on which you want to connect
port = 12345
pyautogui.FAILSAFE = False
prevbutton = ' '

# connect to the server on local2 computer
s.connect(('192.168.1.8', port))

# receive data from the server
while True:
    message = s.recv(30)
    datums = str(message).split("$")
    #print(datums)
    x = int(datums[1])
    y = int(datums[2])
    if (datums[3] == ']'):
        break
    if (datums[3] == 'n' and prevbutton != 'n'):
        pyautogui.click(button='left')
        prevbutton = 'n'
    elif (datums[3] == 'z' and prevbutton != 'z'):
        pyautogui.click(button='right')
        prevbutton = 'z'
    elif (datums[3] == 's' and prevbutton != 's'):
        pyautogui.press('space')
        prevbutton = 's'
    elif (datums[3][0] != ' ' and prevbutton != datums[3]):
        if (datums[4][0] != ' '):
            pyautogui.keyDown('ctrl')
            pyautogui.press(datums[3])
            pyautogui.keyUp('ctrl')
        else:
            pyautogui.press(datums[3])
        prevbutton = datums[3]
    else:
        prevbutton = ' '

    #print (x)
    #print (y)
    pyautogui.moveTo(x,y)

# close the connection
s.close()
