from numpy.core.fromnumeric import take
from functions import *
import random
import json
import datetime

intents = json.loads(open('intents.json').read())

def notepad(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'write a note' and tag == 'write a note':
            if content == '':
                res = random.choice(intent['responses'])
                speak(res)
                note = takeCommand()
            else:
                note = content
                
            file = open('note.txt', 'w')
            strTime = datetime.datetime.now().strftime('%d %B,%Y %A %H:%M:%S \n')
            file.write(strTime)
            file.write(note)
            speak('Finished taking note.')
            return 'Finished taking note.'
         
        elif intent['tag'] == 'show note' and tag == 'show note':
            res = random.choice(intent['responses'])
            speak(res)
            file = open('note.txt', 'r')
            textContent = file.read()
            speak(textContent)
            return textContent