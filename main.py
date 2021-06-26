# código python
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from plyer import notification, vibrator

class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tarefas(Screen):
    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ""
        notification.notify('Tarefas','Descrição: {}'.format(texto))
        vibrator.vibrate(1)

    def on_pre_enter(self,*args):
        Window.bind(on_keyboard=self.voltar)

    def on_pre_leave(self,*args):
        Window.unbind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = "menu"
            return True

class Tarefa(BoxLayout):
    def __init__(self,text="",**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Test(App):
    def build(self):
        return Manager()

Test().run()
