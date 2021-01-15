import pyautogui
import sockets
import keyboard

constant_size = '                              ]'

print(pyautogui.size())
print(pyautogui.position())
x, y = pyautogui.position()
positionStr = str(x).rjust(4)[1:] + '$' + str(y).rjust(4)[1:]
for i in range(0, 29-len(positionStr)):
    positionStr += ' '
positionStr += ']'
print(positionStr)
print(positionStr[0])

for i in range(1, 30):
    if (keyboard.is_pressed(']')):
        break
    pyautogui.moveTo(i*30,i*30)
    x, y = pyautogui.position()
    positionStr = str(x).rjust(4)[1:] + '$' + str(y).rjust(4)[1:]
    for i in range(0, 29-len(positionStr)):
        positionStr += ' '
    positionStr += ']'
    print(positionStr)
