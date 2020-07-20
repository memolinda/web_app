from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob, random
from datetime import datetime
from pathlib import Path


Builder.load_file("design.kv")

class LoginScreen(Screen): #class with the same name as the rules in the .kv file
    def sign_up(self):
        self.manager.current ="sign_up_screen" #switch from the login screen to the sig up screen

    def login(self, uname,pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "loging_screen_success"
        else:
            self.ids.login_wrong.text="Wrong username or password!"

    def forget_password(self):
        # self.manager.transition.direction="right"
        self.manager.current = "forget_password_screen"


class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen): #any action in the sign up screen it is connected to this class
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users=json.load(file)
        users[uname]={'username': uname, 'password': pword,
                    'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current ="sign_up_screen_success"

class ForgottenPassword(Screen):
    def check_password(self, user):
        # self.manager.transition.direction="left"
        with open("users.json") as file:
            users=json.load(file)
        if user in users:
            passw = users[user]['password']
            self.ids.show_password.text=passw
        else:
            self.ids.show_password.text="Username invalid"
    def forgot_password_back(self):
        self.manager.transition.direction="right"
        self.manager.current="login_screen"


class SignUpScreenSuccess(Screen):
    def login_back(self):
        self.manager.transition.direction="right"
        self.manager.current="login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction="right"
        self.manager.current="login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feeeling = glob.glob("quotes/*txt")
        available_feeeling = [Path(filename).stem for filename
                                in available_feeeling]
        if feel in available_feeeling:
            with open(f"quotes/{feel}.txt") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Sorry, feeling not supportet yet!"

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ =="__main__":
    MainApp().run()
