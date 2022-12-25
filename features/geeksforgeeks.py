from functions import *
import webbrowser
import json
import random

intents = json.loads(open('intents.json').read())

def geeksforgeeks(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'search in geeksforgeeks about' and tag == 'search in geeksforgeeks about':
            res = random.choice(intent['responses'])
            speak(res)
            content = 'geeksforgeeks ' + content
            url='https://www.google.com/search?q=' + content
            webbrowser.open(url)
            break
        
        elif intent['tag'] == 'open geeksforgeeks' and tag == 'open geeksforgeeks':
            res = random.choice(intent['responses'])
            speak(res)
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('www.geeksforgeeks.org')
            break