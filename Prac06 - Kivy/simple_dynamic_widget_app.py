from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class SimpleDynamicWidgetApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.simple_list = ['String One', 'String Two', 'String Three', 'Four', 'Five', 'Six']

    def build(self):
        self.title = "Simple Dynamic Widget App"
        self.root = Builder.load_file('simple_dynamic_widget_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for element in self.simple_list:
            temp_button = Button(text=element)
            # print(temp_button.text)
            self.root.add_widget(temp_button)


SimpleDynamicWidgetApp().run()
