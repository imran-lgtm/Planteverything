from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.utils import platform
from kivy.core.window import Window
import time

# Dark Green Theme
Window.clearcolor = (0.02, 0.05, 0.02, 1)

def start_permissions():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

class ScannerScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        layout.add_widget(Label(text="🌿 PLANT ENCYCLOPEDIA AI 🌿", size_hint_y=0.1, font_size='22sp', bold=True, color=(0.4, 1, 0.4, 1)))
        
        # Camera (Bara Size)
        self.cam = Camera(play=True, resolution=(1280, 720), size_hint=(1, 0.6), allow_stretch=True)
        layout.add_widget(self.cam)
        
        # Result Label (Yahan History aur Bemari show hogi)
        self.info = Label(text="Ready to Scan...", size_hint_y=0.15, halign='center', font_size='14sp')
        layout.add_widget(self.info)
        
        # Scan Button logic
        btn = Button(text="📷 SCAN PLANT", size_hint_y=0.1, background_color=(0.1, 0.7, 0.1, 1), bold=True)
        btn.bind(on_press=self.analyze_plant)
        layout.add_widget(btn)
        
        self.add_widget(layout)

    def analyze_plant(self, instance):
        # Jab button dabayein toh error ki bajaye ye show ho
        self.info.text = "Searching in Encyclopedia...\nChecking for Diseases..."
        # Fake delay for AI feel
        print("Capturing Image...")
        # Future mein yahan AI API connect hogi

class CommunityScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(Label(text="👥 PLANT LOVERS COMMUNITY\nComing Soon for Imran(djz)", halign='center'))
        self.add_widget(layout)

class PlantEncyclopediaApp(App):
    def build(self):
        start_permissions()
        self.sm = ScreenManager()
        self.sm.add_widget(ScannerScreen(name='scanner'))
        self.sm.add_widget(CommunityScreen(name='community'))
        
        root = BoxLayout(orientation='vertical')
        root.add_widget(self.sm)
        
        # Navigation
        nav = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        btn1 = Button(text="Scan AI", background_color=(0.2, 0.4, 0.2, 1))
        btn1.bind(on_press=lambda x: setattr(self.sm, 'current', 'scanner'))
        btn2 = Button(text="Community", background_color=(0.2, 0.4, 0.2, 1))
        btn2.bind(on_press=lambda x: setattr(self.sm, 'current', 'community'))
        nav.add_widget(btn1)
        nav.add_widget(btn2)
        root.add_widget(nav)
        
        # SIGNATURE
        root.add_widget(Label(text="Developed by: Imran(djz)", size_hint_y=0.05, font_size='10sp', color=(0.6, 0.6, 0.6, 1)))
        
        return root

if __name__ == '__main__':
    PlantEncyclopediaApp().run()
