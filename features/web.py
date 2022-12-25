from functions import *
import webbrowser
import json
import random

intents = json.loads(open('intents.json').read())

def web(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'search in web' and tag == 'search in web':
            res = random.choice(intent['responses'])
            speak(res)
            content = content.replace(' ','+')
            url = 'http://www.google.com/search?q=' + content + '&oq=' + content
            webbrowser.open_new_tab(url)
            return res

        elif intent['tag'] == 'open google' and tag == 'open google':
            res = random.choice(intent['responses'])
            speak(res)
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.google.com')
            return res