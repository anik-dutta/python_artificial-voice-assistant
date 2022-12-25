from functions import *
import json
import random
import requests
from geotext import GeoText
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
intents = json.loads(open('intents.json').read())

def weather(tag, content = '', current_user = ''):
    user_data = pd.read_csv('account.csv')
    user_city = user_data.loc[user_data['Username'] == current_user]['City'].values[0]

    for intent in intents['intents']:
        if intent['tag'] == 'weather' and tag == 'weather':
            api_key = os.getenv('WEATHER_API')
            base_url = 'http://api.openweathermap.org/data/2.5/weather?'

            if content == '':
                city_name = user_city                
            else:
                places = GeoText(content)
                city_name = places.cities[0]

            complete_url = base_url + 'q=' + city_name + '&appid=' + api_key
            response = requests.get(complete_url)       
            x = response.json()
            
            if x['cod'] != '401' and x['cod'] != '404': 
                y = x['main'] 
                current_temperature = y['temp'] 
                current_pressure = y['pressure'] 
                current_humidiy = y['humidity'] 
                z = x['weather'] 
                weather_description = z[0]['description']
                temp = random.choice(intent['responses1']).replace('#*#*#*', city_name) + str(current_temperature)
                atm = 'Atmospheric pressure is '+ str(current_pressure)
                hum = 'Humidity is' + str(current_humidiy)

                result = temp + atm + hum + 'Weather is ' + weather_description
                speak(result)

                f_response = ('Temperature (in kelvin unit) = ' + str(current_temperature) +
                ' Atmospheric pressure (in hPa unit) = '+str(current_pressure) +
                ' Humidity (in percentage) = ' + str(current_humidiy) +
                ' Weather = ' + str(weather_description))
                return  f_response                
            else: 
                responses2 = random.choice(intent['responses2'])
                speak(responses2)
                return responses2