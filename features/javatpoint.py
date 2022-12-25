from functions import *
import webbrowser
import json
import random

intents = json.loads(open('intents.json').read())

def javatpoint(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'search in javatpoint about' and tag == 'search in javatpoint about':
            res = random.choice(intent['responses'])
            speak(res)
            content = 'javatpoint ' + content
            url='https://www.google.com/search?q=' + content
            webbrowser.open(url)
            break
        
        elif intent['tag'] == 'open javatpoint' and tag == 'open javatpoint':
            res = random.choice(intent['responses'])
            speak(res)
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.javatpoint.com')
            break

        
            
        
            

