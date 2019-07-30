from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route("/michael")
def index():
    return "Hello, michael , how are you ! "


@app.route('/<string:name>')
def name(name):
    return f'hello, {name} '

#@app.route('/user/<username>')
#def profile(username):
#   return '{}\'s profile'.format(escape(username))
