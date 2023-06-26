import kivy
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.lang import Builder

class MachineinfoScreen(MDScreen):
    def build(self): return Builder.load_file('machineinfo.kv')

class machinename(MDCard):
    pass

class machinenumber(MDCard):
    pass

class machinehardware(MDCard):
    pass