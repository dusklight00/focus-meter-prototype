from flask import Flask, request
from tinydb import TinyDB, Query

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/register', methods=['GET'])
def register():
    username = request.args.get('username')
    password = request.args.get('password')

    print(username, password)

    return 'Register page'

@app.route('/login')
def login():
    return 'Login page'

if __name__ == '__main__':
    app.run()
