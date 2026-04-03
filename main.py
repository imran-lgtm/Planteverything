from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.graphics.context_instructions import PushMatrix, PopMatrix, Rotate
from kivy.utils import platform
from kivy.core.window import Window
from kivy.clock import Clock

# Force Fullscreen Size
WIDTH = Window.width
HEIGHT = Window.height

class ScannerScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.main_layout = FloatLayout(size=(WIDTH, HEIGHT))

        # --- FORCE FULLSCREEN CAMERA ---
        # Hum size_hint ko None kar ke manual width/height de rahe hain
        self.cam = Camera(
            play=True, 
            resolution=(1280, 720), 
            size_hint=(None, None),
            size=(WIDTH, HEIGHT),
            pos=(0, 0),
            allow_stretch=True, 
            keep_ratio=False
        )
        
        # Rotation Fix
        with self.cam.canvas.before:
            PushMatrix()
            self.rot = Rotate(angle=-90, origin=(WIDTH/2, HEIGHT/2))
        with self.cam.canvas.after:
            PopMatrix()
        
        self.main_layout.add_widget(self.cam)

        # UI Overlay (Buttons etc)
        overlay = BoxLayout(orientation='vertical', padding=20, spacing=10)
        overlay.add_widget(Label(text="🌿 PLANT ENCYCLOPEDIA", size_hint_y=0.1, bold=True, font_size='22sp'))
        overlay.add_widget(Label(text="", size_hint_y=0.6)) # Center Space
        
        self.info_label = Label(
            text="Tap below to Identify Plant", 
            size_hint_y=0.1, 
            background_color=(0,0,0,0.6)
        )
        overlay.add_widget(self.info_label)
        
        self.scan_btn = Button(
            text="📷 SCAN NOW", 
            size_hint_y=0.15, 
            background_color=(0.1, 0.7, 0.1, 0.9), 
            bold=True
        )
        self.scan_btn.bind(on_press=self.start_scan)
        overlay.add_widget(self.scan_btn)

        self.main_layout.add_widget(overlay)
        self.add_widget(self.main_layout)

    def start_scan(self, instance):
        self.info_label.text = "🔍 AI is Analyzing... Please Wait"
        # 3 second baad result dikhayega
        Clock.schedule_once(self.show_result, 3)

    def show_result(self, dt):
        self.info_label.text = "✅ SUCCESS: Ready for Real AI API!"
        self.info_label.color = (0, 1, 0, 1)

class PlantEncyclopediaApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(ScannerScreen(name='scanner'))
        # Abhi sirf scanner check karte hain
        return self.sm

if __name__ == '__main__':
    PlantEncyclopediaApp().run()
