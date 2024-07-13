import kivy
from kivy.app import App
from kivy.lang import Builder

kivy.require('2.1.0')


class MyApp(App):

    def build(self):
        self.title = 'Label Properties'
        return Builder.load_file('gui_centering_AL.kv')


if __name__ == '__main__':
    MyApp().run()