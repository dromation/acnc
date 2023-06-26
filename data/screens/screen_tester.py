from kivymd.uix.screen import MDScreen
from kivymd.uix.widget import MDWidget
from kivymd.app import MDApp
from kivy.lang import Builder

class ComponentsScreen(MDScreen):
    pass

class ConnectionsScreen(MDScreen):
    pass

class ConnectorSettingsScreen(MDScreen):
    pass

class ControlScreen(MDScreen):
    pass

class HomeScreen(MDScreen):
    pass

class MachineInfoScreen(MDScreen): 
    pass

class SignalsScreen(MDScreen):
    pass

class Status(MDWidget):
    pass

class TestApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.material_style = "M3"
        return Builder.load_file('connectorst.kv')
    

TestApp().run()