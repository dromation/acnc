from kivymd.uix.screen import MDScreen
from kivymd.uix.tab  import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import 

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class FTAScreen(MDScreen, Tab):
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        instance_tab.ids.label.text = tab_text
    