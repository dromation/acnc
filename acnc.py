# SMOTO VERSION 0.1

#IMPORT BASICS
import sys, os, pathlib
from typing import Union
import socket
from time import time
from datetime import datetime
from os.path import dirname, join
import cv2 as cv
import numpy as np
import glob
#from root.ModelPrep import validate_params, change_koatuu, prep_params, load_regression

#IMPORT PANDAS
#import pandas as pd
#import sqlite3

#IMPORT SCIKITLEARN FOR MACHINE LEARNING
#import scikitlearn as sct

#IMPORT KIVY FOR GUI
import kivy
#from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.widget import MDWidget
from kivymd.uix import *
from kivy.properties import ObjectProperty, NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
from kivy.metrics import dp
from kivy.lang import Builder
#from kivymd.app import Builder
from kivy.core.window import Window
from kivy.uix.slider import Slider
#from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.label import MDLabel
from optparse import Values
from kivy.uix.screenmanager import SwapTransition
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.scrollview import MDScrollView as mdsw1
from kivymd.uix.scrollview import MDScrollView as mdsw2
import ctypes
from data.screens.machineinfo import MachineinfoScreen

#image class 

class FirstNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    one_drawer = nav_drawer

class SecondNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    two_drawer = nav_drawer

class ThirdNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    three_drawer = nav_drawer


class ACNCScreen(MDScreen):
    pass

class MachineInfoScreen(MachineinfoScreen):
    pass


class ACNCApp(MDApp):
    title = 'ANALYZE CNC'
    #sm = ScreenManager()

    def build(self):
        file_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"File {i}": self.home_callback(x),
                
             } for i in range(2)
        ]
        self.home = MDDropdownMenu(
            items=file_items,
            width_mult=3
        )

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
             } for i in range(5)
        ]
        
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.material_style = "M3"
        return Builder.load_file('ACNC.kv')
    #def on_start(self):
     #   self.fps_monitor_start()
        
    def on_save(self, instance, value):
        print(instance, value)

    def on_cancel(self, instance, value):
        print(instance, value)

    def homescreen(self): self.sm.switch_to(screen='home')

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def home_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()


    def on_pause(self):
        return True

    def on_resume(self):
        pass
    

if __name__ == '__main__':
    ACNCApp().run()
    
    
"""MDBoxLayout:
    screen_manager: sm
    toolbar: toolbar
    MDTopAppBar:
        id: toolbar
        use_overflow: True
        left_action_items: [["home", lambda x: sm.current = 'home'],[["camera", lambda x: sm.current = 'camera']]
    ScreenManager:
        id: sm
        MDScreen:
            id: home
            name: "home"
        MDScreen:
            id: camera
            name: "camera"        

"""