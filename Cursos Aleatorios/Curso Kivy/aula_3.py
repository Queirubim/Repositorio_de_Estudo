from turtle import onrelease
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class teste (App):
    def build(self):
        box = BoxLayout(orientation= 'vertical')
        button = Button (text='Botão  1 ', font_size=30,on_release=self.incrementar )
        self.label1 = Label(text = "1")
        box.add_widget(button)
        box.add_widget(self.label1)
        return box

    def incrementar(self,button):
        self.label1.text = str(int(self.label1.text)+1)
    
    

teste().run()