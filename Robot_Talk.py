import speech_recognition as sr
import sounddevice
from gtts import gTTS
import subprocess
import random


# Initialize the recognizer
recognizer = sr.Recognizer()


# Functions
def listen_to_microphone():
    global user_input
    global wakeWord
    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)  # Adjust the timeout as needed

        try:
            user_input = recognizer.recognize_google(audio)  # You can use other engines as well
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Sorry, I encountered an error: {e}")

def TTS(var):
    tts = gTTS(var)
    tts.save("temp.mp3")
    playsound("temp.mp3")

def playsound(file_path):
    try:
        subprocess.run(["mpg123", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error playing {file_path}: {e}")
    except FileNotFoundError:
        print("mpg123 is not installed. Please install it using your package manager.")
