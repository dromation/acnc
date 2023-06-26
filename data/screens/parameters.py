import kivy
from kivymd.uix.widget import MDWidget
import pandas as pd



class Parameters(MDWidget):
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
        
class paratable(pd):
    pass

class INPUTS(self):
    pass

class OUTPUTS(self):
    pass
