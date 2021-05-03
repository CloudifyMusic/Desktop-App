import json
import smtplib

from user import User



class Operations(User):
    
    def __init__(self, username):
        self.username = username

    # Not taken care of, yet.
    def send_verification_email(self, email):
        pass

    def change_password(self, new_password):
        if val in self.space:
            return "This field is required."

        if len(val) < 8:
            return "Your password must be at least 8 characters long!"

        self.user_data[self.username]["general"]["password"] = new_password

    def change_username(self, new_username):
        if val in self.space:
            return "This field is required."

        for x in val:
            self.characters.append(x)
        
        for x in self.characters:
            if x in self.forbidden_characters:
                return "Your username must only include letters A - Z!"

        self.characters.clear()

        self.user_data[self.username]["general"]["username"] = new_username

    def set_profile_picture(self, new_pfp):
        if val in self.space:
            return "This field is required."

        self.user_data[self.username]["general"]["profile picture"] = new_pfp

    def login_username(self, username):
        if val in self.space:
            return "This field is required."

        if username != self.username:
            return "Your username is incorrect."

    def login_password(self, password):
        if password in self.space:
            return "This field is required."

        if password != self.user_data[self.username]["general"]["password"]:
            return "Your password is incorrect."

    def delete_account(self):
        self.user_data[self.username] = None
