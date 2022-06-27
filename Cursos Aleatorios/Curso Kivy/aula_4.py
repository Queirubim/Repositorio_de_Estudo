from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Tarefas(BoxLayout):
    pass

class aula_5 (App):
    def build(self):
        return Tarefas()

    
    

aula_5().run()