from kivy.app import App
from kivy.app import Builder


class ConvertMilesToKilometresApp(App):
    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root


ConvertMilesToKilometresApp().run()
