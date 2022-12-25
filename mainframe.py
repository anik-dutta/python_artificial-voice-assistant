from functions import *
from background import *
from britannica import *
from calculate import *
from conversation import *
from encyclopedia import *
from geeksforgeeks import *
from javatpoint import *
from location import *
from message import *
from music import *
from news import *
from notepad import *
from open_app import *
from question import *
from send_email import *
from stackoverflow import *
from syscoms import *
from tutorialspoint import *
from weather import *
from web import *
from wiki import *
from youtube import *
from text_analyzer import *
from location import *
from music import *
from screenshot import *
import json
import random

greet = ['Hi #*#*#*, I am AVA at your service.','Hello #*#*#*, my name is AVA.','Hello #*#*#*, I am AVA.']
initial = ['What can I do for you?','How can I help you?','What do you want me to do?','Tell me something','Tell me something, I will do that']
intents = json.loads(open('intents.json').read())

callFunctions = {'background' : background, 'calculate' : calculate, 'conversation' : conversation, 'location' : location, 'message' : message, 'music' : music, 'news' : news, 'notepad' : notepad, 'open_app' : open_app, 'question' : question, 'send_email' : send_email, 'syscoms' : syscoms, 'weather' : weather, 'web' : web, 'wiki' : wiki, 'youtube' : youtube, 'britannica': britannica, 'encyclopedia' : encyclopedia, 'geeksforgeeks': geeksforgeeks, 'javatpoint' : javatpoint, 'stackoverflow': stackoverflow, 'tutorialspoint': tutorialspoint, 'screenshot': screenshot }

current_user = 'SS'

def set_current_user(name):
    global current_user
    current_user = str(name)

def initial_response():
    res = random.choice(greet).replace('#*#*#*', current_user) + ' ' + random.choice(initial)
    speak(res)
    return res

# Content extraction applied is not accurate, it could be improved by using NAMED ENTITY RECOGNITION....which will be implemented later

def content_extraction(input, tag = ''):
    input = list(input.split())
    content = []

    for intent in intents['intents']:
        if intent['tag'] == tag:
            elem_words = []

            for item in intent['patterns']:
                for i in item.split():
                    elem_words.append(i)

            for word in input:
                if word in input and word not in elem_words:
                    content.append(word)

    content = ' '.join(content)
    content = content.strip()
    return content

def generateOutput(input, swap):
    tag = analyzer(input)
    if tag[-1] == '$':
        tag = tag[0]
        return tag
    
    if tag == 'send email' and swap == False:
        set_email_user(current_user)
        return tag

    content = content_extraction(input, tag)
    for intent in intents['intents']:
        if intent['tag'] == tag:
            output = callFunctions[intent['context'][0]](tag, content, current_user)
            return output