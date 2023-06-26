#Connector settings screen
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.selectioncontrol import MDCheckbox


    
ConnectorBase = ["CONNECTOR1" == '12',
                 "CONNECTOR2" == '8',
                 "CONNECTOR3" == '4',
                 "CONNECTOR4" == '20']


#pin is only on on a part of a connector
class pin(MDCheckbox):
    def signal(self, signc):
        signc = ""
        if self.signal is True: return signc
    
    def on_active(self, signc,  value):
        signc = value
        if value is True: return signc
        else: value is 0
        return value

class Connector():
    connector_type = [""]
    connector_pins = []

    def connector_type(self):
        connector_type = [""]
    def connector_pins(self):
        connector_pins = []

class FirstConnector(MDCard, Connector):
    pass

class SecondConnector(MDCard, Connector):
    pass


class ConnectorSettingsScreen(MDScreen, Connector):
    
    def load_pins(self, connector_pins, connector_type):
        self.load_pins = []
        for value in connector_type: connector_pins.append(value)
    #def select_connector(self):
     #   for keys, values in ConnectorBase
            
    pass