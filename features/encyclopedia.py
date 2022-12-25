from functions import *
import webbrowser
import json
import random

intents = json.loads(open('intents.json').read())

def encyclopedia(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'search in encyclopedia about' and tag == 'search in encyclopedia about':
            res = random.choice(intent['responses'])
            speak(res)
            url = 'https://www.encyclopedia.com/gsearch?q=' + content
            webbrowser.open(url)
            return res

        elif intent['tag'] == 'open encyclopedia' and tag == 'open encyclopedia':
            res = random.choice(intent['responses'])
            speak(res)
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.encyclopedia.com')
            return res