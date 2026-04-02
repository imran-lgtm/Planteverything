from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.utils import platform
from kivy.core.window import Window

# Dark Green Theme
Window.clearcolor = (0.02, 0.05, 0.02, 1)

# --- Android Permissions Logic (Pixel 6 ke liye lazmi) ---
def start_permissions():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

class ScannerScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        layout.add_widget(Label(text="🌿 PLANT ENCYCLOPEDIA AI 🌿", size_hint_y=0.1, font_size='22sp', bold=True, color=(0.4, 1, 0.4, 1)))
        
        # Camera preview (Is baar hum "play=False" rakhenge start mein taake crash na ho)
        self.cam = Camera(play=True, resolution=(640, 480), size_hint_y=0.6)
        layout.add_widget(self.cam)
        
        self.info = Label(text="Scan plant for History & Diseases", size_hint_y=0.1)
        layout.add_widget(self.info)
        
        btn = Button(text="📷 SCAN NOW", size_hint_y=0.15, background_color=(0.1, 0.7, 0.1, 1), bold=True)
        layout.add_widget(btn)
        self.add_widget(layout)

class CommunityScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(Label(text="👥 GLOBAL COMMUNITY\n(Connecting soon...)", halign='center', font_size='20sp'))
        self.add_widget(layout)

class PlantEncyclopediaApp(App):
    def build(self):
        # Permissions mangna shuru mein hi
        start_permissions()
        
        self.sm = ScreenManager()
        self.sm.add_widget(ScannerScreen(name='scanner'))
        self.sm.add_widget(CommunityScreen(name='community'))
        
        root = BoxLayout(orientation='vertical')
        root.add_widget(self.sm)
        
        # Navigation
        nav = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=5)
        btn1 = Button(text="Scan AI", background_color=(0.2, 0.5, 0.2, 1))
        btn1.bind(on_press=lambda x: setattr(self.sm, 'current', 'scanner'))
        btn2 = Button(text="Community", background_color=(0.2, 0.5, 0.2, 1))
        btn2.bind(on_press=lambda x: setattr(self.sm, 'current', 'community'))
        nav.add_widget(btn1)
        nav.add_widget(btn2)
        root.add_widget(nav)
        
        # DEVELOPER NAME SIGNATURE
        root.add_widget(Label(text="Developed by: Imran(djz)", size_hint_y=0.05, font_size='12sp', color=(0.7, 0.7, 0.7, 1)))
        
        return root

if __name__ == '__main__':
    PlantEncyclopediaApp().run()
