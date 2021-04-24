import json

from user import User



class Operations(User):
    
    def __init__(self, user):
        # The user parameter must be an instance of the class User defined in the user.py file, I haven't yet figured out a way to hook this up to any specific user and user data.
        self.user = user
