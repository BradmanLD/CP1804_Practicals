from kivy.app import App
from kivy.app import Builder

MILES_TO_KM = 1.60934


class ConvertMilesToKilometresApp(App):
    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_increment(self, increment):
        incremented_number = self.get_miles() + increment
        self.root.ids.number_of_miles.text = str(incremented_number)
        self.calculate_miles_to_kilometres()

    def get_miles(self):
        try:
            miles = float(self.root.ids.number_of_miles.text)
            return miles

        except ValueError:
            return 0

    def calculate_miles_to_kilometres(self):
        number_of_miles = self.get_miles()
        number_of_kilometres = number_of_miles * MILES_TO_KM
        self.root.ids.output_label.text = str(number_of_kilometres) + " kilometres"


ConvertMilesToKilometresApp().run()
