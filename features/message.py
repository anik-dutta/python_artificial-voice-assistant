from functions import *
import requests
import random
import json
import os
from dotenv import load_dotenv

load_dotenv()
intents = json.loads(open('intents.json').read())

def message(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'send message':
            url = 'https://www.fast2sms.com/dev/bulk'
            res =  random.choice(intent['responses'])
            speak(res)
            message = takeCommand()
            res1 =  random.choice(intent['numresponses'])
            speak(res1)
            number = takeCommand()
            number = number.replace(' ','')
            payload = 'sender_id=FSTSMS&message=' + message + '&language=english&route=p&numbers=' + number
            headers = {
                    'authorization': os.getenv('MESSAGE_API'),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Cache-Control': 'no-cache',
                    }
            response = requests.request('POST', url, data=payload, headers=headers)
            response_text = response.text
            speak('Message has been sent')
            return response_text