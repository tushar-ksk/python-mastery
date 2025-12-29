from gtts import gTTS
import pygame
import os

pygame.mixer.init()

text = None
speech = gTTS(text=text, lang='en', tld= "co.in")
speech.save("temp.mp3")

pygame.mixer.music.load("temp.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick()

pygame.mixer.music.unload()
os.remove("temp.mp3")