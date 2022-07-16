import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import random

class audioInAndOut:
    def __init__(self):
        pass

    def speak(self, text):
        try:
            print(f"Virtual Assistant: {text()}")
        except:
            print(f"Virtual Assistant: {text}")

    def getAudio(self):
        text = input("Give command: ")
        return text
