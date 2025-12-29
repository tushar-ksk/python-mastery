import pyautogui
import os


parts = os.getenv('parts')
print(parts)


while True:
    a = pyautogui.position()
    print(a)

