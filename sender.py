import requests


username = input('tvoe ime:')
text = input('vvedi text soobcheniya')

requests.get(
     'http://127.0.0.1:5000/get_messages'
    json = {'username' : username, 'text' : text}
)