from functions import *
import json
import random
import pyscreenshot
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
intents = json.loads(open('intents.json').read())
  
def screenshot(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'take screenshot' and tag == 'take screenshot':
            res = random.choice(intent['responses'])
            image = pyscreenshot.grab()
            speak(res)
            
            img_path = os.getenv('USER_PATH') + '/Pictures/Screenshots/'
            time = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
            img_name = 'screenshot_'+time+'.png'
            image.save(img_path+img_name)
            image.show()
            return res