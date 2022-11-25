import requests
from requests.structures import CaseInsensitiveDict
import time
#import os
#from google.cloud import pubsub_v1

url = "https://api.telegram.org/bot5960321871:AAF-MiS07aKNj_ktcUB6qiKsnWy6TISjjlY/getUpdates"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
last_query = 0

while True:
    resp = requests.get(url, headers=headers)
    data = resp.json()
    if data['result'][-1]['message']['from']['is_bot'] == False:
        message = data['result'][-1]['message']['text'].lower()
        words = message.split()
        if words[0] == 'grabar':
            query = data['result'][-1]['update_id'] 
            user = data['result'][-1]['message']['from']['first_name']
            x = int(words[1])
            data_time = words[2][:3]
            if last_query != query:
                print(f'Usuario: {user} \nTiempo: {x} \nFormato {data_time}')
                last_query = query
    time.sleep(1)