import sys
import pyautogui
import sockets

print(pyautogui.size())
print(pyautogui.position())
for i in (0,50):
    pyautogui.moveTo(i * 30, 150)
