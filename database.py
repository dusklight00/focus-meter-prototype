from tinydb import TinyDB, Query

class Database:
    def __init__(self):
        self.db = TinyDB('db.json')
    
    def create_account(self, username, password):
        self.db.insert({'username': username, 'password': password})