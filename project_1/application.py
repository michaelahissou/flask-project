from flask import Flask

app = Flask(__name__)

@app.route('/')             #main route
def hello_world():
    return 'Hello, World!'


@app.route('/hello') # another route to tell hello zorld to everyone
def hello():
    return 'Hello, World'



@app.route('/<string:name>')# route to tell hello visitor_name to visitor
def name(name):
    return f'hello, {name} '
