#speach to text to text to speach

import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
import os
from dotenv import load_dotenv 

load_dotenv()

class VoiceAssistant:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat()
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Speak to chat ...")
            try:
                audio = self.recognizer.listen(source, timeout=5)
                return self.recognizer.recognize_google(audio)
            except:
                return ""

    def run(self):
        self.speak("Hello! How can I help?")
        while True:
            text = self.listen()
            
            if text.lower() in ["quit", "exit"]:
                self.speak("Thank you for having me!!")
                break

            if text:
                print("You:", text)
                response = self.chat.send_message(text).text
                print("AI:", response)
                self.speak(response)

if __name__ == "__main__":
    API_KEY = os.getenv("GOOGLE_API_KEY")
    
    if not API_KEY:
        print("Error: GOOGLE_API_KEY is not set in the environment variables.")
    else:
        assistant = VoiceAssistant(API_KEY)
        assistant.run()
