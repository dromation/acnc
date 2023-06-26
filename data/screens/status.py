import kivy
from kivymd.uix.widget import MDWidget
from kivymd.uix.boxlayout import MDBoxLayout

class Status(MDWidget):
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

        
        if instance.icon == 'list-status':
            lang = "Status"
        elif instance.icon == 'check-outline':
            lang = "START"
        elif instance.icon == 'cancel':
            lang = "STOP"
        self.root.ids.templates.text = f'you pressed {lang}'

        #self.root.ids.my_label.text = f'you pressed {instance.icon}'

    def stmenuopen(self):
        self.root.ids.templates.text = f'Choose Template'

    def stmenuclose(self):
        self.root.ids.templates.text = f'Template'

class MachineStatus(MDBoxLayout):
    pass