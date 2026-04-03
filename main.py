from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.uix.scrollview import ScrollView
from kivy.utils import platform
from kivy.core.window import Window
import time

Window.clearcolor = (0.02, 0.05, 0.02, 1)

def start_permissions():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

class ScannerScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.layout.add_widget(Label(text="🌿 PLANT AI SCANNER", size_hint_y=0.1, font_size='20sp', bold=True, color=(0.4, 1, 0.4, 1)))
        
        # Large Camera
        self.cam = Camera(play=True, resolution=(1280, 720), size_hint_y=0.6, allow_stretch=True)
        self.layout.add_widget(self.cam)
        
        self.info_label = Label(text="Align plant in center and tap Scan", size_hint_y=0.1, halign='center')
        self.layout.add_widget(self.info_label)
        
        # Scan Button logic
        btn = Button(text="📷 ANALYZE PLANT", size_hint_y=0.15, background_color=(0.1, 0.8, 0.1, 1), bold=True)
        btn.bind(on_press=self.analyze_plant)
        self.layout.add_widget(btn)
        
        self.add_widget(self.layout)

    def analyze_plant(self, instance):
        self.info_label.text = "Scanning... Analyzing DNA & Species..."
        # Asli AI connect hone tak ye testing text dikhayega
        def update_info(dt):
            self.info_label.text = "RESULT: Healthy Rose (Rosa)\nHistory: Origin Persia, 5000 years old.\nDisease: None Detected."
            self.info_label.color = (0, 1, 0, 1)
        
        from kivy.clock import Clock
        Clock.schedule_once(update_info, 2)

class CommunityScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=10)
        layout.add_widget(Label(text="👥 GLOBAL COMMUNITY", size_hint_y=0.1, bold=True))
        
        scroll = ScrollView()
        list_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        list_layout.bind(minimum_height=list_layout.setter('height'))
        
        # Dummy Community Posts
        posts = [
            "Ali (Lahore): My Aloe Vera is growing fast! 🌱",
            "Sara (Dubai): Help! My Rose leaves are turning yellow. 🥀",
            "Imran(djz): Just scanned a rare Cactus! 🌵",
            "John: Beautiful Sunflower in my garden. 🌻"
        ]
        
        for p in posts:
            list_layout.add_widget(Label(text=p, size_hint_y=None, height=100, color=(0.8, 0.8, 0.8, 1)))
        
        scroll.add_widget(list_layout)
        layout.add_widget(scroll)
        self.add_widget(layout)

class PlantEncyclopediaApp(App):
    def build(self):
        start_permissions()
        self.sm = ScreenManager()
        self.sm.add_widget(ScannerScreen(name='scanner'))
        self.sm.add_widget(CommunityScreen(name='community'))
        
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.sm)
        
        nav = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=2)
        btn1 = Button(text="Scan AI", background_color=(0.1, 0.4, 0.1, 1))
        btn1.bind(on_press=lambda x: setattr(self.sm, 'current', 'scanner'))
        btn2 = Button(text="Community", background_color=(0.1, 0.4, 0.1, 1))
        btn2.bind(on_press=lambda x: setattr(self.sm, 'current', 'community'))
        
        nav.add_widget(btn1)
        nav.add_widget(btn2)
        main_layout.add_widget(nav)
        
        main_layout.add_widget(Label(text="Developed by: Imran(djz)", size_hint_y=0.05, font_size='10sp'))
        
        return main_layout

if __name__ == '__main__':
    PlantEncyclopediaApp().run()
