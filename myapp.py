from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

from Config import parse_rgb

class MyGlobals:
    global_var = "12"


class MainInterface(BoxLayout):
    global_red = parse_rgb.parse_rgb(255, 0, 0, 1)
    global_green = parse_rgb.parse_rgb(0, 255, 0, 1)
    global_blue = parse_rgb.parse_rgb(0, 0, 255, 1)
    global_orange = parse_rgb.parse_rgb(153, 76, 0, 1)
    global_white = parse_rgb.parse_rgb(255, 255, 255, 0.5)

    def __init__(self, **kwargs):
        super(MainInterface, self).__init__(**kwargs)


    def button_pressed(self):
        #open popup a window with some stuff to wirte in

        pass



class MyApp(App):
    def build(self):
        Window.size = (2400, 1200)
        return MainInterface()
