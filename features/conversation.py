from functions import *
import pyjokes
import json
import random
import datetime
from datetime import date
import time

intents = json.loads(open('intents.json').read())

def conversation(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'hello' and tag == 'hello':
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == 'thank you' and tag == 'thank you':
            res = random.choice(intent['responses'])
            speak(res)
            return res
        
        elif intent['tag'] == 'good morning' and tag == 'good morning':
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == 'good afternoon' and tag == 'good afternoon':
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == 'good evening' and tag == 'good evening':
            res = random.choice(intent['responses'])
            speak(res)
            return res
        
        elif intent['tag'] == 'good night' and tag == 'good night':
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == 'how are you' and tag == 'how are you':
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == 'fine' and tag == 'fine':
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == 'not so good' and tag == 'not so good':
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == "what's your name" and tag == "what's your name":
            res = random.choice(intent['responses']) + ' AVA'
            speak(res)
            return res

        elif intent['tag'] == 'who made you' and tag == 'who made you':
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == 'joke' and tag == 'joke':
            joke = pyjokes.get_joke()
            speak(joke)
            return joke

        elif intent['tag'] == 'who am i' and tag == 'who am i':
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == 'who are you' and tag == 'who are you':
            res = random.choice(intent['responses'])
            speak(res)
            return res

        elif intent['tag'] == "what's the meaning of your name" and tag == "what's the meaning of your name":
            res = random.choice(intent['responses'])
            speak(res)
            return res
        
        elif intent['tag'] == 'exit' and tag == 'exit':
            res = random.choice(intent['responses'])
            speak(res)
            exit()

        elif intent['tag'] == 'what is the time' and tag == 'what is the time':
            strTime = datetime.datetime.now().strftime('%H:%M:%S')    
            res = random.choice(intent['responses']) + ' ' + strTime
            speak(res)
            return res        

        elif intent['tag'] == "don't listen" and tag == "don't listen":
            if content == '':
                speak('For how much time you want to stop me from listening you?')
                t = takeCommand()
            else:
                t = content
                t = t.replace('for', '')
            t = list(t.split())
            a = int(t[0])
            time.sleep(a)
            break

        elif intent['tag'] == 'what is the date' and tag == 'what is the date':
            today = date.today()
            _date = today.strftime('%B %d %A')
            res = random.choice(intent['responses']) + ' ' + _date 
            speak(res)
            return res