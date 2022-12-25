from functions import *
import json
import random
import webbrowser
import urllib.request
import re

intents = json.loads(open('intents.json').read())

def music(tag, content = '', current_user = ''):
   for intent in intents['intents']:
      if intent['tag'] == 'play the music' and tag == 'play the music':
         res = random.choice(intent['responses']) 
         res = res.replace('#*#*#*', content)
         speak(res)
         content = content.replace(' ','+')
         html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + content)
         video_ids = re.findall(r'watch\?v=(\S{11})', html.read().decode())
         url = 'https://www.youtube.com/watch?v=' + video_ids[0]
         webbrowser.open_new_tab(url)
         return res