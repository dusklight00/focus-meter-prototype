from flask import Flask, request
from database.user_database import UserDatabase
from database.rooms_database import RoomsDatabase
import json

app = Flask(__name__)
user_database = UserDatabase()
room_database = RoomsDatabase()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/register', methods=['GET'])
def register():
    username = request.args.get('username')
    password = request.args.get('password')
    user_type = request.args.get('user_type')

    if not user_database.create_account(username, password, user_type):
        return json.dumps({'status': 'failure'})

    return json.dumps({'status': 'success'})

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if user_database.check_account(username, password):
        account_details = user_database.get_details(username)
        return json.dumps({'status': 'success', 'details': account_details})
    else:
        return json.dumps({'status': 'failure'})

@app.route('/create_room')
def create_room():
    room_name = request.args.get('room_name')
    teacher = request.args.get('teacher')

    if not room_database.create_room(room_name, teacher):
        return json.dumps({'status': 'failure'})

    return json.dumps({'status': 'success'})

@app.route('/add_student')
def add_student():
    room_name = request.args.get('room_name')
    student = request.args.get('student')

    if not room_database.add_student(room_name, student):
        return json.dumps({'status': 'failure'})

    return json.dumps({'status': 'success'})

@app.route('/remove_student')
def remove_student():
    room_name = request.args.get('room_name')
    student = request.args.get('student')

    if not room_database.remove_student(room_name, student):
        return json.dumps({'status': 'failure'})

    return json.dumps({'status': 'success'})


if __name__ == '__main__':
    app.run()
