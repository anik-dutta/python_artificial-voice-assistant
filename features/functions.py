import speech_recognition as sr
import pyttsx3
import datetime
import smtplib
import shutil
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 115)

def speak(audio):
    time.sleep(1)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
        speak('I\'m listening...')
        audio = r.listen(source)
  
    try:      
        query = r.recognize_google(audio, language ='en-in')
        query = query.strip()
        print(f'User said: {query}\n')
        return query
  
    except Exception as e:
        speak('Unable to Recognize your voice.')  
        return 'None'
    return query