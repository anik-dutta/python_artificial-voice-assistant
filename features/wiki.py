import wikipedia
import webbrowser
from functions import *
import random
import json

intents = json.loads(open('intents.json').read())

def wiki(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'search in wikipedia about' and tag == 'search in wikipedia about':
            res = random.choice(intent['responses'])
            speak(res)
            results = wikipedia.summary(content, sentences = 3)
            speak(results)
            return results

        elif intent['tag'] == 'open wikipedia' and tag == 'open wikipedia':
            res = random.choice(intent['responses'])
            speak(res)
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.wikipedia.com')
            return res