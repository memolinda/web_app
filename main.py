from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file("design.kv")

class LoginScreen(Screen): #class with the same name as the rules in the .kv file
    def sign_up(self):
        self.manager.current ="sign_up_screen" #switch from the login screen to the sig up screen

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
class SignUpScreenSuccess(Screen):
    pass 
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ =="__main__":
    MainApp().run()
