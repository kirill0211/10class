"""

"""

from flask import Flask, render_template, request

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
    return {
        'messages': messages
    }


@server.route('/index')
def index():
    name = 'Дмитрий Валерьевич'
    return render_template('index.html')


server.run()