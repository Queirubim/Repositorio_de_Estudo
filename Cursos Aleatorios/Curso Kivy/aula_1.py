from kivy.app import App
from kivy.uix.button import Button

class teste (App):
    def build(self):
        return Button (text='Botão!!!')

teste().run()