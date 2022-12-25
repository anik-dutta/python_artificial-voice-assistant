import urllib
import webbrowser
from functions import *
import random
import json

intents = json.loads(open('intents.json').read())

def youtube(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'search in youtube about' and tag == 'search in youtube about':
            res = random.choice(intent['responses'])
            speak(res)
            url = 'https://www.youtube.com/results?search_query=' + content.replace(' ','+')
            webbrowser.open(url)
            return res
            
        elif intent['tag'] == 'open youtube' and tag == 'open youtube':
            res = random.choice(intent['responses'])
            speak(res)
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.youtube.com')
            return res