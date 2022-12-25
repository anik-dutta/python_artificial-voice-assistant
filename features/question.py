from functions import *
import wolframalpha
import webbrowser
import json
import os
from dotenv import load_dotenv

load_dotenv()
intents = json.loads(open('intents.json').read())

def question(tag, content = '', current_user = ''):
    for intent in intents['intents']:
        if intent['tag'] == 'what is' and tag == 'what is':
            client = wolframalpha.Client(os.getenv('WOLFRAMALPHA_API'))
            response = client.query(content)
            try:
                res = next(response.results).text
                speak(res)
                return res

            except AttributeError:
                res = 'Sorry, I can\'t give any proper answer of your question, but I can search it in google for you'
                speak(res)
                content = content.replace(' ','+')
                url = 'http://www.google.com/search?q=' + content + '&oq=' + content
                webbrowser.open_new_tab(url)
                return res