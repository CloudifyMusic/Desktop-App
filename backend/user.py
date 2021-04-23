import json


class User:

    def __init__(self):
        self.fname = None
        self.lname = None
        self.username = None
        self.email = None
        self.password = None
        self.phonenumber = None
        self.profile_picture = None
        self.all_users = []

        with open("backend/datafiles/user_data.json", "r") as f:
            self.user_data = json.loads(f.read())

    # Only for writing dicts to files (and in the process converting them to JSON Data).
    def save(self, file, data):
        with open(file, "w") as f:
            f.write(json.dumps(data, indent=4))

    def set_fname(self, val):
        self.fname = val
    
    def set_lname(self, val):
        self.lname = val

    # ON SIGN - UP, THIS MUST BE THE FIRST DATA TO BE COLLECTED FROM A NEW USER. KEEP THAT IN MIND. DO NOT FORGET. :)
    def set_username(self, val):
        self.username = val

    def set_email(self, val):
        self.email = val

    def set_password(self, val):
        self.password = val

    def set_phonenumber(self, val):
        self.phonenumber = val
    
    def set_profile_picture(self, url):
        self.profile_picture = url # I guess we'll just have this as a URL for the moment until we figure out how to open the file explorer so that the user can actually upload their pfp

    def declare_user(self):
        self.all_users.append(self.username)

        self.user_data = {
            "general statistics": {
                "first name": self.fname,
                "last name": self.lname,
                "username": self.username,
                "email": self.email,
                "password": self.password,
                "phonenumber": self.phonenumber,
                "profile picture": self.profile_picture
            }
        }
        self.save("backend/datafiles/user_data.json", self.user_data)
