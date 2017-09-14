"""Do it from Scratch exercise for CP1404 prac_06
Converts Miles to Kilometers
Created by Christopher Ryan
Started 14/9/17"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Christopher Ryan'

class MilesConverterApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = 'Miles to Kilometers'
        self.root = Builder.load_file('from_scratch.kv')
        return self.root

    def increment_input(self, increment, user_input):
        new_value = user_input + increment
        self.root.ids.input_number.text = str(new_value)

    def convert_miles_to_kilometers(self, miles):
        try:
            kilometers = miles * 1.61
            self.root.ids.converted_km.text = str(kilometers)
        except ValueError:
            self.root.ids.converted_km.text = 0

MilesConverterApp().run()
