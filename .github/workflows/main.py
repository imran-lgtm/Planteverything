
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class PlanteverythingApp(App):
    def build(self):
        return Label(text="🌿 Planteverything V2 Ready! 🌿\n(Encyclopedia & AI Chat)")

if __name__ == '__main__':
    PlanteverythingApp().run()
