from functions import *
import time
import ctypes
import json
import random
import winshell
import os

intents = json.loads(open('intents.json').read())

def syscoms(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'lock window' and tag == 'lock window':
            res = random.choice(intent['responses'])
            speak(res)
            time.sleep(2)
            ctypes.windll.user32.LockWorkStation()
            break
        
        elif intent['tag'] == 'shutdown system' and tag == 'shutdown system':
            res = random.choice(intent['responses'])
            speak(res)
            time.sleep(2)
            os.system('shutdown /s /t 1')
            break

        elif intent['tag'] == 'restart' and tag == 'restart':
            res = random.choice(intent['responses'])
            speak(res)
            time.sleep(2)
            os.system('shutdown /s /t 1')
            break

        elif intent['tag'] == 'log off' and tag == 'log off':
            res = random.choice(intent['responses'])
            speak(res)
            time.sleep(2)
            os.system('shutdown -l')
            break

        elif intent['tag'] == 'hibernate' and tag == 'hibernate':
            res = random.choice(intent['responses'])
            speak(res)
            time.sleep(2)
            os.system('shutdown /h')
            break

        elif intent['tag'] == 'empty recycle bin' and tag == 'empty recycle bin':
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            res = random.choice(intent['responses'])
            speak(res)
            break