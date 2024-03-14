import requests
import pprint
import time
#Получаем инфу о боте
token = '6205811706:AAEyswQGCs1YqH8g0hRMumLmvpYbOsdyMmI'
main_url = f'https://api.telegram.org/bot{token}'
#url = f'{main_url}/getMe'
#print(url)
#result = requests.get(url)
#pprint.pprint(result.json())

#Проверка на обновления (события)
url = f'{main_url}/getUpdates'
result = requests.get(url)
pprint.pprint(result.json())




# Ответ на сообщение
messages = result.json()['result']
for message in messages:
        chat_id = message['message']['chat']['id']
        url = f'{main_url}/sendMessage'
        params = {
         'chat_id': chat_id,
         'text': 'Привет дорогой пользователь!'
        }
        result = requests.post(url, params=params)