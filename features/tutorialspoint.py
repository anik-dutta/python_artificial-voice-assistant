from functions import *
import webbrowser
import json
import random

intents = json.loads(open('intents.json').read())

def tutorialspoint(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'search in tutorialspoint about' and tag == 'search in tutorialspoint about':
            res = random.choice(intent['responses'])
            speak(res)
            url='https://www.tutorialspoint.com/index.htm?q='+content
            webbrowser.open(url)
            return res 
        
        elif intent['tag'] == 'open tutorialspoint' and tag == 'open tutorialspoint':
            res = random.choice(intent['responses'])
            speak(res)
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.tutorialspoint.com')
            return res