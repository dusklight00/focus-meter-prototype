from flask import Flask, request
from database import Database

app = Flask(__name__)
database = Database()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/register', methods=['GET'])
def register():
    username = request.args.get('username')
    password = request.args.get('password')

    database.create_account(username, password)

    return 'Register page'

@app.route('/login')
def login():
    return 'Login page'

if __name__ == '__main__':
    app.run()
