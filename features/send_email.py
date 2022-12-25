from re import sub
from functions import *
import smtplib
import json
import random
import pandas as pd
from text_analyzer import *
import os
from dotenv import load_dotenv

load_dotenv()
intents = json.loads(open('intents.json').read())

to_response = ['Whom should I send?','What is the email id of receiver?','Tell the email id, where I have to send.']
user = ''
to_email = ''
subject = ''
message = ''
ava_email = os.getenv('EMAIL_ID')
ava_email_password = os.getenv('EMAIL_PASSWORD')

def set_email_user(usr):
    global user
    user = usr

def send_email(tag, content = '', current_user = ''):
    user_data = pd.read_csv('account.csv')
    user_email = user_data.loc[user_data['Username'] == current_user]['Email'].values[0]
    for intent in intents['intents']:
        if intent['tag'] == 'send email' and tag == 'send email':
            speak(random.choice(to_response))
            
            while(True):  
                speak('Tell the first part of email id before @ symbol')
                first = takeCommand()
                speak('Tell the last part of email id after @')
                second = takeCommand()
                to_email = first + '@' + second
                if to_email.isspace():
                    speak('There are some spaces in the email id, would you like to re-enter? Tell me yes or no, if no then I will modify it by myself')
                    check = takeCommand()
                    if check == 'No' or check == 'no':
                        to_email = to_email.replace(' ', '')
                        break                    
                else:
                    break
            
            speak('Do you want to add subject?')
            ans = takeCommand()
            ans = analyzer(ans)
            if ans == 'yes':
                speak('Tell me the subject')
                subject = takeCommand()
            else:
                speak('Ok then I am adding default subject')
    
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()

                server.login(ava_email, ava_email_password)
                speak('What do you want me to write?')
                message = takeCommand()
                
                message = 'Subject: ON BEHALF OF {} -- {}\n\n{}'.format(user_email, subject, message)
                message = message + '\nThis is an A.V.A. generated email. If you want to reply to this email then send an email to ' + user_email
                server.sendmail(ava_email, to_email, message)
                server.close()

                ifresponse = random.choice(intent['ifresponse'])
                speak(ifresponse)
                return ifresponse

            except Exception as e:
                elseresponse = random.choice(intent['elseresponse'])
                speak(elseresponse)
                return elseresponse

            break

def ask_email(tag):
    res = random.choice(to_response)
    speak(res)
    return res

def add_email(tag, msg):
    global to_email
    to_email = msg

def ask_subject_permission(tag):
    res = 'Do you want to add subject?'
    speak(res)
    return res

def ask_subject(tag, msg):
    ans = analyzer(msg)

    if(ans == 'yes'):
        res = 'Tell me the subject you want me to add'
        speak(res)
        ans = '//*' + ans + '//*'
        return [res, ans]
    elif(ans == 'no'):
        res = 'Ok then, I am adding a default subject only'
        speak(res)
        ans = '//*' + ans + '//*'
        return [res, ans]
    else:
        res = 'Sorry I can\'t understand what you have said so I am assuming it as NO'
        speak(res)
        ans = 'no'
        ans = '//*' + ans + '//*'
        return [res, ans]

def add_subject(tag, msg):
    global subject
    subject = msg

def ask_message(tag):
    res = 'What do you want to write in message?'
    speak(res)
    return res

def add_message(tag, msg):
    global message
    message = msg

def send_email_audio(tag):
    user_data = pd.read_csv('account.csv')
    user_email = user_data.loc[user_data['Username'] == user]['Email'].values[0]
    for intent in intents['intents']:
        if intent['tag'] == 'send email' and tag == 'send email':
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()

                global message
                server.login(ava_email, ava_email_password)
                message = 'Subject: ON BEHALF OF {} -- {}\n\n{}'.format(user_email, subject, message)
                message = message + '\nThis is an A.V.A. generated email. If you want to reply to this email then send an email to ' + user_email

                server.sendmail(ava_email, to_email, message)
                server.close()
                res = random.choice(intent['responses1'])
                speak(res)
                return res

            except Exception as e:
                res = random.choice(intent['responses2'])
                speak(res)
                return res
            
            break