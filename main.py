from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("design.kv")

class LoginScreen(Screen): #class with the same name as the rules in the .kv file
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ =="__main__":
    MainApp().run()
