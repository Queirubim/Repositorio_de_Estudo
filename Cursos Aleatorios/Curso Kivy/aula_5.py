from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tarefas (BoxLayout):
    def __init__ (self,tarefas,**kwargs): 
        #keyword arguments exemplo "letras = a"
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa))

class aula_5(App):
    def build(self):
        return Tarefas (['Fazer compras','Buscar carro','Molhar Plantas'],orientation='horizontal')

aula_5().run()