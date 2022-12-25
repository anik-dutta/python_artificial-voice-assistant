from functions import *
import ctypes
import json
import random
import os
from dotenv import load_dotenv

load_dotenv()
intents = json.loads(open('intents.json').read())

# wallpaper path must be selected by user manually for that in FRONT-END path location must be typed in the text and that value will be stored in'wallpaper_path' variable or wallpaper should be selected the corresponding path should be stored in 'wallpaper_path' variable.

def background(tag, content = '', current_user = ''): 
    for intent in intents['intents']:
        if intent['tag'] == 'change background' and tag == 'change background':
            wallpaper_path = os.getenv('USER_PATH') + '/Pictures/Wallpapers/34908.jpg'
            ctypes.windll.user32.SystemParametersInfoW(20,0,wallpaper_path,0)
            res =  random.choice(intent['responses'])
            speak(res)
            return res