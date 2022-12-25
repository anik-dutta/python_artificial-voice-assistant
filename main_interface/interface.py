from contextlib import suppress
import eel
import time
import random
import os
from mainframe import *
from credentials import *
from functions import takeCommand
from send_email import *
port = random.randint(8000,8999)

eel.init(os.path.join(os.path.dirname(__file__))+'/interface', allowed_extensions=['.html','.js'])

#exposing python function to javascript
@eel.expose
def initialResponse():
    response = initial_response()
    return response

@eel.expose  
def sendResponse(msg, swap):
    output = generateOutput(msg, swap)
    return output

@eel.expose
def sendResponse_audio():
    time.sleep(1)
    input = takeCommand()
    return input

@eel.expose
def audio_mode_on():
    speak('Audio mode is on. You can now communicate with AVA through voice. To turn it off press the microphone button again and it will turn white')

@eel.expose
def audio_mode_off():
    speak('Audio mode has turned off. Type in message box to ask something.')

@eel.expose
def reg(name, email, password, city, number):
    return register(name, email, password, city, number)

@eel.expose
def log(name, password):
    return login(name, password)

#Email
@eel.expose
def askEmail(tag):
    return ask_email(tag)

@eel.expose
def addEmail(tag, msg):
    return add_email(tag, msg)

@eel.expose
def askSubjectPermission(tag):
    return ask_subject_permission(tag)

@eel.expose
def askSubject(tag, msg):
    return ask_subject(tag, msg)

@eel.expose
def addSubject(tag, msg):
    return add_subject(tag, msg)

@eel.expose
def askText(tag):
    return ask_message(tag)

@eel.expose
def addText(tag, msg):
    return add_message(tag, msg)

@eel.expose
def sendEmail(tag):
    return send_email_audio(tag)

eel.start('start.html',  port = port, size = (1024,900), mode = 'chrome')