from functions import *
import webbrowser
import json
import random

intents = json.loads(open('intents.json').read())

def britannica(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'search in britannica about' and tag == 'search in britannica about':
            res = random.choice(intent['responses'])
            speak(res)
            url = 'https://www.britannica.com/search?query=' + content         
            webbrowser.open(url)
            return res
        
        elif intent['tag'] == 'open britannica' and tag == 'open britannica':
            res = random.choice(intent['responses'])
            speak(res)   
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.britannica.com')
            return res