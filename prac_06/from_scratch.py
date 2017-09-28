"""Do it from Scratch exercise for CP1404 prac_06
Converts Miles to Kilometers
Created by Christopher Ryan
Started 14/9/17"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.window import Window

__author__ = 'Christopher Ryan'


"""class MilesConverterApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = 'Miles to Kilometers'
        self.root = Builder.load_file('from_scratch.kv')
        return self.root

    def increment_input(self, increment, user_input):
        try:
            new_value = int(user_input) + increment
            self.root.ids.input_number.text = str(new_value)
        except ValueError:
            new_value = 0 + increment
            self.root.ids.input_number.text = str(new_value)

    def convert_miles_to_kilometers(self, miles):
        try:
            kilometers = int(miles) * 1.61
            self.root.ids.converted_km.text = str(kilometers)
        except ValueError:
            self.root.ids.converted_km.text = str(0)


MilesConverterApp().run()"""


class DynamicWidget(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Jimbo Jones", "Tim Tundra", "Lucy Lockhart"]

    def build(self):
        self.title = "Dynamic Widget"
        Window.size = (400, 300)
        self.root = Builder.load_file('OwnWidget.kv')
        self.more_widgets()

    def more_widgets(self):
        for name in self.names:
            temp_button = Button(text=name)
            self.root.ids.nameDisplayed.add_widget(temp_button)

DynamicWidget().run()
