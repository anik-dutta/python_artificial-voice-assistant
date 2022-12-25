from functions import *
import json
import random
import os

intents = json.loads(open('intents.json').read())

def open_app(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'open chrome' and tag == 'open chrome':
            path = r'C://Program Files (x86)/Google/Chrome/Application/chrome.exe'
            os.startfile(path)
            res = random.choice(intent['responses'])
            speak(res)
            return res
            
        elif intent['tag'] == 'open mozilla firefox' and tag == 'open mozilla firefox':
            path = r'C://Program Files/Mozilla Firefox/firefox.exe'
            os.startfile(path)
            res = random.choice(intent['responses'])
            speak(res)
            return res
            
        elif intent['tag'] == 'open microsoft edge' and tag == 'open microsoft edge':
            path = r'C://Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
            os.startfile(path)
            res = random.choice(intent['responses'])
            speak(res)
            return res
            
        elif intent['tag'] == 'open power point presentation' and tag == 'open power point presentation':
            path = r'C://Program Files/Microsoft Office/Office15/POWERPNT.exe'
            os.startfile(path)
            res = random.choice(intent['responses'])
            speak(res)
            return res 

        elif intent['tag'] == 'open word' and tag == 'open word':
            path = r'C://Program Files/Microsoft Office/Office15/WINWORD.exe'
            os.startfile(path)
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == 'open excel' and tag == 'open excel':
            path = r'C://Program Files/Microsoft Office/Office15/EXCEL.exe'
            os.startfile(path)
            res = random.choice(intent['responses'])
            speak(res)
            return res
            
        elif intent['tag'] == 'open adobe acrobat reader' and tag == 'open adobe acrobat reader':
            path = r'C://Program Files (x86)/Adobe/Acrobat Reader DC/Reader/AcroRd32.exe'
            os.startfile(path)
            res = random.choice(intent['responses'])
            speak(res)
            return res
            
        elif intent['tag'] == 'open k m player' and tag == 'open k m player':
            path = r'C://Program Files/KMPlayer/KMPlayer.exe'
            os.startfile(path)
            res = random.choice(intent['responses'])
            speak(res)
            return res
            
        elif intent['tag'] == 'open vlc media player' and tag == 'open vlc media player':
            path = r'C://Program Files/VideoLAN/VLC/vlc.exe'
            os.startfile(path)
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == 'open notepad' and tag == 'open notepad':
            path = r'C://Windows/System32/notepad.exe'
            os.startfile(path)
            res = random.choice(intent['responses'])
            speak(res)        
            return res