from features.functions import speak
import webbrowser
import json
import random
import pandas as pd

intents = json.loads(open('intents.json').read())

def location(tag, content = '', current_user = ''):
     user_data = pd.read_csv('account.csv')
     user_city = user_data.loc[user_data['Username'] == current_user]['City'].values[0]
     for intent in intents['intents']:
          if intent['tag'] == 'my location' and tag == 'my location':
               res = random.choice(intent['responses'])
               speak(res)
               url = 'https://www.google.com/maps/place/' + user_city
               webbrowser.open(url)
               return res

          elif intent['tag'] == 'where is' and tag == 'where is':
               city_name = content
               if city_name == '':
                    res = 'You haven\'t mentioned any location name!'
                    speak(res)
                    return res
               res = random.choice(intent['responses']).replace('#*#*#*', city_name)
               speak(res)
               url = 'https://www.google.com/maps/place/' + city_name
               webbrowser.open(url)
               return res