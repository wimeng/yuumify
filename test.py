import pyautogui
import sockets

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
