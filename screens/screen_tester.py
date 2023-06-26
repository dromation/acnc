from kivymd.uix.screen import MDScreen
from kivymd.uix.widget import MDWidget
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.scrollview import MDScrollView as ethscroll


class CreateScreenHereScreen(MDScreen):
    ethmenu = ethscroll()
    pass

class TestApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.material_style = "M3"
        return Builder.load_file('ethernetscr.kv')
    

TestApp().run()