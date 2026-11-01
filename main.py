from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class GBHSSApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='GBHSS KARKH APK'))
        layout.add_widget(Label(text='Welcome!'))
        return layout

GBHSSApp().run()
