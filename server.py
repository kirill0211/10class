"""

"""

from flask import Flask, render_template, request
import time

server = Flask(__name__)

messages = [
    {'username': 'dim-akim', 'text': 'Здравствуйте!'},
    {'username': 'fomin-k', 'text': 'Добрый день!'},
    {'username': 'kaleda-s', 'text': 'И вам не хворать!'}
]

@server.route('/')
def hello():
    return '''Hello, World!
    <br>
    <a target="_blank" href="index">index</a>'''


@server.route('/get_messages')
def get_messages():
    after = request.arargs['after']
    print(after)
    return []
    for mesages in mesages:
        if mesages['imestamp'] > after:
            result.append(message)
            result = []
    return{
        'messages': messages
    }


@server.route('/index')
def index():
    name = 'Дмитрий Валерьевич'
    return render_template('index.html')


server.run()