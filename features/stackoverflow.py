from functions import *
import webbrowser
import json
import random

intents = json.loads(open('intents.json').read())

def stackoverflow(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'search in stackoverflow about' and tag == 'search in stackoverflow about':
            res = random.choice(intent['responses'])
            speak(res)
            url = 'https://stackoverflow.com/search?q=' + content
            webbrowser.open(url)
            return res
        
        elif intent['tag'] == 'open stackoverflow' and tag == 'open stackoverflow':
            res = random.choice(intent['responses'])
            speak(res)
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.stackoverflow.com')
            return res