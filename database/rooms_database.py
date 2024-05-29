from tinydb import TinyDB, Query

class RoomsDatabase:
    def __init__(self):
        self.db = TinyDB('../rooms.json')
    
    def create_room(self, room_name, teacher):
        Room = Query()
        isRoomPresent = len(self.db.search(Room.room_name == room_name)) > 0
        if isRoomPresent:
            return False
        self.db.insert({'room_name': room_name, 'teacher': teacher, 'students': []})
        return True

    def add_student(self, room_name, student):
        Room = Query()
        isRoomPresent = len(self.db.search(Room.room_name == room_name)) > 0
        if not isRoomPresent:
            return False
        room = self.db.search(Room.room_name == room_name)[0]
        students = room['students']
        students.append(student)
        self.db.update({'students': students}, Room.room_name == room_name)
        return True
    
    def remove_student(self, room_name, student):
        Room = Query()
        isRoomPresent = len(self.db.search(Room.room_name == room_name)) > 0
        if not isRoomPresent:
            return False
        room = self.db.search(Room.room_name == room_name)[0]
        students = room['students']
        students.remove(student)
        self.db.update({'students': students}, Room.room_name == room_name)
        return True