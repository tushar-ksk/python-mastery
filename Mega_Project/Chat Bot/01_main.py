import os
import sys
import time
import keyboard
import pyperclip
import pyautogui
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

keyboard.add_hotkey('ctrl', lambda: sys.exit("Program closed by pressing 'ctrl'."))

def last_message(chat, sender_name = "Tushar"):
    # splitting chat by \n
    messages = chat.strip().split("/2025]")[-1]
    if sender_name in messages:
        return True
    else:
        return False
pyautogui.click(1374,1042)

while True:

    # step2: selecting area by draging mouse while clicking left 
    time.sleep(1)
    pyautogui.sleep(5)
    pyautogui.moveTo(704,209)
    pyautogui.dragTo(1900,1014, duration= 2, button="left")

    # step3: copying
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(690,208)
    time.sleep(1)

    # printing the copied text to clipboard
    chat = pyperclip.paste()

    # print the copied text to verify
    print(chat)

    if last_message(chat):

        # Configure your API key (be sure to handle it securely in real use)
        genai.configure(api_key= os.getenv('API_KEY'))

        # Define the model
        model = genai.GenerativeModel("gemini-2.0-flash")

        command = chat

        try:
            # Generate content with user input
            response = model.generate_content(
                [
                    {
                        "role": "user",
                        "parts": [
                            f'{os.getenv("PARTS")} {command}.'
                        ]
                    }
                ]
                )
                # Check if the response is valid
            if response.text:
                # click on text bar
                time.sleep(2)
                pyperclip.copy(response.text)
                print(response.text)
                time.sleep(1)
                pyautogui.click(1000, 975)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')

            else:
                print("No response received from the model.")
        except Exception as e:
            print(f"An error occurred: {e}")
