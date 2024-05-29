from tinydb import TinyDB, Query
from util import generate_uuid

class Database:
    def __init__(self):
        self.user_db = TinyDB('users.json')
        self.room_db = TinyDB('rooms.json')
    
    def create_teacher(self, username, password):
        User = Query()
        isUserPresent = len(self.user_db.search(User.username == username)) > 0
        if isUserPresent:
            return False
        user_id = generate_uuid()
        self.user_db.insert({'id': user_id, 'username': username, 'password': password, 'user_type': 'teacher'})
        return True
    
    def create_student(self, username, password):
        User = Query()
        isUserPresent = len(self.user_db.search(User.username == username)) > 0
        if isUserPresent:
            return False
        user_id = generate_uuid()
        self.user_db.insert({'id': user_id, 'username': username, 'password': password, 'user_type': 'student'})
        return True
    
    def create_room(self, master):
        Room = Query()
        isRoomPresent = len(self.room_db.search(Room.master == master)) > 0
        if isRoomPresent:
            return False
        room_id = generate_uuid()
        self.room_db.insert({'id': room_id, 'master': master, 'students': []})
        return True
    
    def add_student(self, room_id, user_id):
        Room = Query()
        isRoomPresent = len(self.room_db.search(Room.id == room_id)) > 0
        if not isRoomPresent:
            return False
        room = self.room_db.search(Room.id == room_id)[0]
        students = room['students']
        students.append(user_id)
        self.room_db.update({'students': students}, Room.id == room_id)
        return True
    
    def remove_student(self, room_id, user_id):
        Room = Query()
        isRoomPresent = len(self.room_db.search(Room.id == room_id)) > 0
        if not isRoomPresent:
            return False
        room = self.room_db.search(Room.id == room_id)[0]
        students = room['students']
        students.remove(user_id)
        self.room_db.update({'students': students}, Room.id == room_id)
        return True
    
    