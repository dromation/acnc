import kivy
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
import sqlite3

class Machineinfo(MDScreen):
    statusmenu = {
            "C++": "language-cpp",
            "Ruby": "language-ruby",
            "Kivy": "language-kivy"
        }
    def stmenucallback(self, instance):
        """for keys,Values in data:
            if instance.icon == data(Values):
                lang = print("you pressed", instance.icon)
            else:
                pass"""

        
        if instance.icon == 'language-cpp':
            lang = "C++"
        elif instance.icon == 'language-ruby':
            lang = "Ruby"
        elif instance.icon == 'language-kivy':
            lang = "Kivy"
        self.root.ids.templates.text = f'you pressed {lang}'

        #self.root.ids.my_label.text = f'you pressed {instance.icon}'

    def stmenuopen(self):
        self.root.ids.templates.text = f'Choose Template'

    def stmenuclose(self):
        self.root.ids.templates.text = f'Template'

class machinename(MDCard):
    pass

class machinenumber(MDCard):
    pass

class machinehardware(MDCard):
    pass