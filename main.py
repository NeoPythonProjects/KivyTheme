import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label

kivy.require('2.1.0')


class MyApp(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # define your theme colours
        self.background_dark = (13/255, 12/255, 29/255, 1)
        self.blue_oxford = (22/255, 27/255, 51/255, 1)
        self.blue_navy = (71/255, 73/255, 115/255, 1)
        self.grey_violet = (166/255, 156/255, 172/255, 1)
        self.white_almond = (241/255, 218/255, 196/255, 1)

    def build(self):
        self.title = 'Create Your Kivy Theme'
        return Builder.load_file('gui.kv')


if __name__ == '__main__':
    MyApp().run()