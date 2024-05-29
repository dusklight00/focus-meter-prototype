from flask import Flask, request
from database import Database
import json
import hashlib

app = Flask(__name__)
database = Database() 

@app.route('/register', methods=['GET'])
def register():
    username = request.args.get('username')
    password = request.args.get('password')
    user_type = request.args.get('user_type')

    if not database.create_account(username, password, user_type):
        return json.dumps({'status': 'failure'})

    return json.dumps({'status': 'success'})

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if database.check_account(username, password):
        account_details = database.get_details(username)
        return json.dumps({'status': 'success', 'details': account_details})
    else:
        return json.dumps({'status': 'failure'})

@app.route('/create_room')
def create_room():
    user_id = request.args.get('user_id')

    if not database.create_room(user_id):
        return json.dumps({'status': 'failure'})

    return json.dumps({'status': 'success'})

@app.route('/remove_room')
def remove_room():
    room_id = request.args.get('room_id')

    if not database.remove_room(room_id):
        return json.dumps({'status': 'failure'})

    return json.dumps({'status': 'success'})

@app.route('/add_student')
def add_student():
    room_id = request.args.get('room_id')
    user_id = request.args.get('user_id')

    if not database.add_student(room_id, user_id):
        return json.dumps({'status': 'failure'})

    return json.dumps({'status': 'success'})

@app.route('/remove_student')
def remove_student():
    room_id = request.args.get('room_id')
    user_id = request.args.get('student')

    if not database.remove_student(room_id, user_id):
        return json.dumps({'status': 'failure'})

    return json.dumps({'status': 'success'})

@app.route('/create_feed')
def create_feed():
    room_id = request.args.get('room_id')
    user_id = request.args.get('user_id')
    mix = room_id + user_id
    hash_object = hashlib.sha256()
    hash_object.update(mix.encode())
    feed_id = hash_object.hexdigest()
    return json.dumps({'feed_id': feed_id})

@app.route('/add_visual_feed')
def add_visual_feed():
    feed_id = request.args.get('feed_id')
    image_base64 = request.args.get('image_base64')
    return json.dumps({'status': 'success'})

# temp feed endpoint
@app.route('/get_feed'):
def get_feed():
    base64_image = request.args.get('image_base64')
    print(base64_image)
    return json.dumps({'status': 'success'})

if __name__ == '__main__':
    app.run()
