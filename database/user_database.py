from tinydb import TinyDB, Query

class UserDatabase:
    def __init__(self):
        self.db = TinyDB('../users.json')
    
    def create_account(self, username, password, user_type):
        if user_type != "teacher" and user_type != "student":
            return False
        User = Query()
        isUserPresent = len(self.db.search(User.username == username)) > 0
        if isUserPresent:
            return False
        self.db.insert({'username': username, 'password': password, 'user_type': user_type})
        return True
    
    def check_account(self, username, password):
        User = Query()
        return len(self.db.search((User.username == username) & (User.password == password))) > 0
    
    def get_details(self, username):
        User = Query()
        return self.db.search(User.username == username)[0] if len(self.db.search(User.username == username)) > 0 else None