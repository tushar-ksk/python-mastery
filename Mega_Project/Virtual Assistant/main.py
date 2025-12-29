import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import time
import datetime
import os
import json
import random
import pywhatkit as kit
import sys
import pyjokes
import pygame
import google.generativeai as genai
from gtts import gTTS
from dotenv import load_dotenv
load_dotenv()

# engine = pyttsx3.init()

# rate = engine.getProperty('rate')
# print(rate)  # Print the current speech rate
# engine.setProperty('rate', 150)  # Set the speech rate to 150 words per minute


# volume = engine.getProperty('volume') 
# Get the current volume level (0.0 to 1.0)
# engine.setProperty('volume', 1)  # Set volume level 0 to 1 but it is already 1


# Get the available voices
# voices = engine.getProperty('voices')

# Iterate through voices to print the properties
# for voice in voices:
#     print(f"Voice: {voice.name}")
#     print(f"Voice ID: {voice.id}")
#     print(f"Languages: {voice.languages}")
#     print(f"Gender: {voice.gender}\n")

# engine.setProperty('voice', voices[0].id)    # already seleted

# def speak(text):
    
#     engine.say(text)
#     engine.runAndWait()
recognizer = sr.Recognizer()
pygame.mixer.init()



def speak(text):
    speech = gTTS(text=text, lang='en', tld="co.in")
    speech.save("temp.mp3")
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")       
        



def AIprocess(command):
        # Configure your API key (be sure to handle it securely in real use)
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

        # Define the model
        model = genai.GenerativeModel("gemini-2.5-flash-lite")
        prompt = os.getenv("PARTS", "") + command

        try:
            # Generate content with user input
            response = model.generate_content(
                [
                    {
                        "role": "user",
                        "parts": [
                            prompt
                        ]
                    }
                ]
            )

            # Check if the response is valid
            if response.text:
                time.sleep(1)
                return (response.text)
            else:
                return ("No response received from the model.")
        except Exception as e:
            return (f"An error occurred: {e}")


def processCommand(command):
  
    if "exit" in command.lower() or "quit" in command.lower():
        speak("Goodbye! Have a great day!")
        sys.exit()

    elif "joke" in command.lower():
        joke = pyjokes.get_joke(language="en")
        print(joke)
        speak(joke)

    elif "open google" in command.lower():
        wb.open("http://www.google.com")
    
    elif "open facebook" in command.lower():
        wb.open("http://www.facebook.com")
    
    elif "open instagram" in command.lower():
        wb.open("http://www.instagram.com")
    
    elif "open twitter" in command.lower():
        wb.open("http://www.twitter.com")
    
    elif "open whatsapp" in command.lower():
        os.system("start whatsapp:")
    
    elif "open telegram" in command.lower():
        os.system("start telegram:")
    
    elif "open stack overflow" in command.lower():
        wb.open("http://www.stackoverflow.com")
    
    elif "open amazon" in command.lower():
        wb.open("http://www.amazon.com")
    
    elif "open flipkart" in command.lower():
        wb.open("http://www.flipkart.com")
    
    elif "open linkedin" in command.lower():
        wb.open("http://www.linkedin.com")
    
    elif "open spotify" in command.lower():
        wb.open("http://www.spotify.com")
    
    elif "open netflix" in command.lower():
        wb.open("http://www.netflix.com")
    
    elif "open youtube" in command.lower():
        wb.open("http://www.youtube.com")
    
    elif "your name" in command.lower():
        print("I am Naruto, your virtual assistant.")
        speak("I am Naruto, your virtual assistant.")
    
    elif "how are you" in command.lower():
        print("I am just a program made by Tushar Kaushik, but thanks for asking!")
        speak("I am just a program made by Tushar Kaushik, but thanks for asking!")
    
    elif "open wikipedia" in command.lower():
        wb.open("http://www.wikipedia.org")
    
    elif "open gmail" in command.lower():
        wb.open("http://www.gmail.com")
    
    elif "what can you do" in command.lower():
        speak("I can open websites, answer questions, and assist you with simple tasks.")
    
    elif "who created you" in command.lower():
        speak("I was created by Tushar Kaushik , just for you!")
    
    elif "tell me a joke" in command.lower():
        speak("Why don’t scientists trust atoms? Because they make up everything!")
    
    elif "time" in command.lower():
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
        print(f"The time is {current_time}")

    elif "date" in command.lower():
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"Today's date is {current_date}")
        speak(f"Today's date is {current_date}")

    elif "open settings" in command.lower():
        os.system("start ms-settings:")
    
    elif "open notepad" in command.lower():
        os.system("notepad.exe")
   
    elif "open word" in command.lower():
        os.system(r'"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"')

    elif "open powerpoint" in command.lower():
        os.system(r'"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"')

    elif "open chrome" in command.lower():
        os.system("chrome.exe")

    elif "open weather" in command.lower():
        os.system("start bingweather:")

    elif "open calculator" in command.lower():
        os.system("calc.exe")

    elif "open excel" in command.lower():
        os.system(r'"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"')

    elif "open paint" in command.lower():
        os.system("mspaint.exe")

    elif "open photos" in command.lower():
        os.system("start ms-photos:")

    elif "open vscode" in command.lower() or "open vs code" in command.lower():
        os.system("code")
    
    elif "rp singh" in command.lower():
        print("Here are some songs by RP Singh")
        speak("Here are some songs by RP Singh")
        url = random.choice([
            "https://youtu.be/GSvXhs7ihNE?si=s5kzNrenX4r2s1BO&t=7",
            "https://youtu.be/xckmjiNJQPg?si=q8Y0Srow21j5Kh3B&t=6",
            "https://youtu.be/HDiJAdwOFaM?si=vLEAj4XYYzG7lXoh&t=6",
            "https://youtu.be/1W41GuOYmo0?si=BwGG3Sg68mVDmzfM&t=6",
            "https://youtu.be/aXgNp1lPkNw?si=gyQidZYVSKyMRprL",
            "https://youtu.be/2TIibPp-hxM?si=A3_Smhb8G586Sk33&t=6",
            "https://youtu.be/umAL1lqXNz4?si=S5_KrBzohObffD2d&t=6",
            "https://youtu.be/YgYq-e1_VVg?si=zorv4yQyQYIjunYw&t=6",
            "https://youtu.be/qva2vi8y5Tc?si=mvc6OxDJtUwCkUFp&t=6",
            "https://youtu.be/gb_pBFiHnTU?si=IpZ9QQY0Xf3ts00y&t=6"
        ])
        wb.open(url)

    elif "masoom sharma" in command.lower():
        print("Here are some songs by Masoom Sharma")
        speak("Here are some songs by Masoom Sharma")
        url = random.choice([
            "https://youtu.be/obgMGM6I2rE?si=Um9Tjn2B7aAVGDTN",
            "https://youtu.be/yBou90w8Y38?si=vO-xf1Eq2SV7uA4X",
            "https://youtu.be/ByjxJyKUXC8?si=YAPudO9R3TgL1P0N&t=14",
            "https://youtu.be/ITAx-69zLWg?si=WAiF9ueSsuhB5I6h&t=6",
            "https://youtu.be/HMI28k_b_dE?si=CfPawHvhpV9-HSPL&t=6",
            "https://youtu.be/afwruTBTILw?si=b_AKU8NCtqY-kT9t&t=6",
            "https://youtu.be/idicKytMbfk?si=ytXS63NQRGrGj9f-t&t=6",
            "https://youtu.be/ZZ86YrRjIOs?si=iEFbBBhUDDLpzdVt&t=6",
            "https://youtu.be/AE1yo-xgEB0?si=l73d2LI_VbFZaJl3&t=6"
        ])
        wb.open(url)

    elif "play song" in command.lower() or "gana" in command.lower():
        print("")
        print("Which song do you want to play?")
        speak("Which song do you want to play?")
        print("Listening....")
        songname = r.listen(source)
        song = r.recognize_google(songname)
        kit.playonyt(song)

    elif "bhajan" in command.lower():
        print("")
        print("Playing bhajan")
        speak("Playing bhajan")
        kit.playonyt("bhajan")
    
    elif "aarti" in command.lower():
        print("")
        print("Playing aarti")
        speak("Playing aarti")
        kit.playonyt("aarti")

    elif "geet" in command.lower():
        print("")
        print("Playing geet")
        speak("Playing geet")
        kit.playonyt("haryanvi geet")

    elif "news"  in command.lower():
        if "english" in command.lower():
            print("")
            print("Playing news headlines in English")
            speak("Playing news headlines in English")
            kit.playonyt("Latest news headlines India English")
    
        elif "hindi" in command.lower():
            print("")
            print("Playing news headlines in Hindi")
            speak("Playing news headlines in Hindi")
            kit.playonyt("Latest news headlines India Hindi")
    
        elif "haryana" in command.lower():
            print("")
            print("Playing news headlines in Haryana")
            speak("Playing news headlines in Haryana")
            kit.playonyt("Latest news headlines Haryana")

        else:
            print("")
            speak("Which language do you prefer for the news?")
            print("Which language do you prefer for the news?")
            print("Listening....")
            language = r.listen(source)
            language_choice = r.recognize_google(language).lower()
            print(f"Language: {language_choice}")
            speak(f"Playing news headlines in {language_choice}")
            kit.playonyt(f"Latest news headline") 
            speak("Please confirm by saying oks India {language_choice}")

    elif "send message" in command.lower() or "message bhejo" in command.lower():
        print("")
        print("Please tell me the name of the person whom you want to send message.")
        speak("Please tell me the name of the person whom you want to send message.")
        print("Listening....")
        person = r.listen(source)
        person_name = r.recognize_google(person).replace(" ", "").lower()
        print(f"Person: {person_name}")
        
        numberdict = json.loads(os.getenv("CONTACTS", "{}"))
     
        number = numberdict.get(person_name)
        if number:
            number = number.replace(" ", "")

            print("Please tell me the message you want to send:")
            speak("Please tell me the message you want to send")
            print("Listening....")
            message = r.listen(source)
            msg = r.recognize_google(message)

            print(f"Message: {msg}")
            speak(f"You said send {msg} to {person_name}")


            print("Please confirm by saying confirmed")
            print("listening for confirmation...")
            print("Listening....")
            ask = r.listen(source)
            verify = r.recognize_google(ask).lower()

            if  "confirmed" in verify.lower():
                print("Sending message...")
                speak("Sending message...")
                kit.sendwhatmsg_instantly(number, msg)
            else:
                print("Message not sent.")
                speak("Message not sent.")
                return
        
        else:
            print("Person not find in list")                
            
    else:
        output = AIprocess(command)
        time.sleep(2)
        print(output)
        speak(output)
            
        

if __name__ == "__main__":
    print("\n\n>>>>>>>>>>This is your assistant<<<<<<<<<<\n\n")
    print("Initializing Naruto....")
    speak("Initializing Naruto...")
    while True:
        
        try:
            # Listen for the wake  work "Naruto"
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("\nListening for the WAKE WORD...\n")
                audio = r.listen(source, timeout = 1.5, phrase_time_limit = 1)
                print("Processing...\n") 
                Word = r.recognize_google(audio)
                
                if "naruto" in Word.lower():
                    # If the wake word is detected, activate the assistant
                    print("Wake word detected!\nNaruto activated..")
                    speak("Hukum mere aaka!")
                
                # listen for command after wake word
                    with sr.Microphone() as source:
                        print("\nListening....\n")
                        audio = r.listen(source, timeout=2)
                        print("Processing your command...\n")
                        command = r.recognize_google(audio)
                        print(f"Command: {command}\n")
                        # Process the command

                        processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
            continue