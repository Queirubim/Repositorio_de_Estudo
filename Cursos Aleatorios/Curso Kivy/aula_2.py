from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class teste (App):
    def build(self):
        box = BoxLayout(orientation= 'vertical')
        button = Button (text='Botão  1 ')
        label1 = Label(text = "Label 1 ")
        box.add_widget(button)
        box.add_widget(label1)
        
        box2 = BoxLayout()
        button2 = Button (text='Botão  2 ')
        label2 = Label(text = "Label 2 ")
        box2.add_widget(button2)
        box2.add_widget(label2)

        box.add_widget(box2)
        return box

teste().run()