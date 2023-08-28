from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


class MyGlobals:
    global_var = "12"


class MainInterface(BoxLayout):
    def __init__(self, **kwargs):
        super(MainInterface, self).__init__(**kwargs)
        self.my_globals = "test"


class MyApp(App):
    def build(self):
        Window.size = (2400, 1200)
        return MainInterface()
