from kivy.app import App


from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class my_root(BoxLayout):
    def generate_number(self):
        self.label1.text = str(random.randint(0,1000))
class testapp(App):
    def build(self):
        return my_root()
        # return Button(text='hello, Kivy')
testapp().run()