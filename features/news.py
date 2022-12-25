from functions import *
from bs4 import BeautifulSoup
from urllib.request import urlopen
import feedparser
import json
import random
import os
from dotenv import load_dotenv

load_dotenv()
intents = json.loads(open('intents.json').read())

def news(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'news' and tag == 'news':
            try: 
                url = 'https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=' + os.getenv('NEWS_API')
                jsonObj = urlopen(url)
                data = json.load(jsonObj)

                i = 1
                res = random.choice(intent['responses'])
                speak(res)
                news_text = '''TIMES OF INDIA\n=============\n'''
                for item in data['articles']:                    
                    news_text += str(i) + '. ' + item['title'] + '\n'
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                return news_text

            except Exception as e:
                res = 'Sorry, there is a problem in finding news'
                speak(res)
                return res
            break