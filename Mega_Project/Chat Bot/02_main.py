import os
import time
# from xml.parsers.expat import model
import keyboard
import pyperclip
import pyautogui
from dotenv import load_dotenv
import google.generativeai as genai
# from groq import Groq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Load environment variables
load_dotenv()

sender = os.getenv('SENDER_NAME')
last_seen_message = None
last_bot_reply = None



def get_last_line(chat_text):
    lines = [l.strip() for l in chat_text.splitlines() if l.strip()]
    if not lines:
        return None
    return lines[-1]

def is_new_message(chat_text):
    global last_seen_message

    last_line = get_last_line(chat_text)
    if not last_line:
        return False

    # First time run: bas store karo, reply mat karo
    if last_seen_message is None:
        last_seen_message = last_line
        print("Initial message stored, no reply")
        return False

    # Same message again → ignore
    if last_line == last_seen_message:
        return False
    last_msg = get_last_line(chat_text)

    # Agar message bot ka hi hai → ignore
    if last_bot_reply and last_msg.strip() == last_bot_reply.strip():
        print("Ignoring bot's own message")
        return False

    # New message detected
    last_seen_message = last_line
    return True


if sender:
    # Chrome options setup
    chrome_options = Options()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_options.add_argument("--user-data-dir=C:/selenium/whatsapp-profile")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--remote-debugging-port=9223")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://web.whatsapp.com/")
    time.sleep(10)
    pyautogui.click(680,270)

    # Select the chat (you can change the name of the chat you want to select)
    # Change this to the name of the chat you want to open
    chat = driver.find_element(By.XPATH, f'//span[@title="{sender}"]')
    chat.click()

    # client = Groq(api_key=os.getenv("API_KEY"))
    # Configure your API key (be sure to handle it securely in real use)
    genai.configure(api_key= os.getenv('API_KEY'))
    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    while True:

        if keyboard.is_pressed('esc'):
            print("Exiting program........")
            break

        # step2: selecting area by draging mouse while clicking left 
        time.sleep(1)
        pyautogui.moveTo(680,270)
        pyautogui.dragTo(1900,1014, duration = 1, button="left")

        # step3: copying
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(680,285)
        pyautogui.click(680,270)
        time.sleep(0.5)

        # printing the copied text to clipboard
        chat = pyperclip.paste()   

        # print the copied text to verify
        print("----- RAW CHAT START -----")
        print(chat)
        print("----- RAW CHAT END -----")


        if is_new_message(chat):
            print("New message detected")

            last_msg = chat
            print("Sending to AI:", last_msg)

            try:
                """
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": os.getenv('System_Prompt')},
                        {"role": "user", "content": last_msg}
                    ]
                )
                """
                # Generate content with user input
                response = model.generate_content(
                    [
                        {
                            "role": "user",
                            "parts": [
                                f'{os.getenv("PARTS")} {last_msg}.'
                            ]
                        }
                    ]
                    )
                # reply = response.choices[0].message.content.strip()     # for Groq
                reply = response.text.strip()                            # for Gemini
                last_bot_reply = reply
                print("AI Reply:", reply)
                
                if reply:
                    pyperclip.copy(reply)
                    time.sleep(0.5)
                    pyautogui.click(1000, 975)
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(0.5)
                    pyautogui.press('enter')
            except Exception as e:
                print("Gemini Error:", e)
        time.sleep(5)