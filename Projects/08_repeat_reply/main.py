import pyautogui as pa
import webbrowser as wb
import time
wb.open("https://web.whatsapp.com/")
time.sleep(20)
for i in range(1, 101):
    pa.typewrite(f"{i}. Hello Satyam.")
    pa.press("enter")
    time.sleep(0.5)