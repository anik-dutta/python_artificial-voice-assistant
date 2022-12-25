from functions import *
import json
import random
import wolframalpha
import os
from dotenv import load_dotenv

load_dotenv()
intents = json.loads(open('intents.json').read())

def calculate(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'calculate' and tag == 'calculate':
            app_id = os.getenv('WOLFRAMALPHA_API')
            client = wolframalpha.Client(app_id)
            content = 'calculate ' + content
            indx = content.lower().split().index('calculate')
            content = content.split()[indx + 1:] 
            response = client.query(' '.join(content))
            answer = next(response.results).text
            res = random.choice(intent['responses']) + answer
            speak(res)
            return res