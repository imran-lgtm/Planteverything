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

Window.clearcolor = (0.02, 0.05, 0.02, 1)

class ScannerScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.main_layout = FloatLayout() # Fullscreen ke liye FloatLayout behtar hai

        # 1. FULLSCREEN CAMERA
        self.cam = Camera(play=True, resolution=(1280, 720), size_hint=(1, 1), allow_stretch=True, keep_ratio=False)
        
        # Rotation Fix (Same as before)
        with self.cam.canvas.before:
            PushMatrix()
            self.rot = Rotate(angle=-90, origin=self.cam.center)
        with self.cam.canvas.after:
            PopMatrix()
        
        self.cam.bind(pos=self.update_rotate_origin, size=self.update_rotate_origin)
        self.main_layout.add_widget(self.cam)

        # 2. OVERLAY UI (Buttons and Labels on top of Camera)
        overlay = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Title at Top
        overlay.add_widget(Label(text="🌿 PLANT ENCYCLOPEDIA", size_hint_y=0.1, bold=True, font_size='24sp', outline_width=2))
        
        # Spacer to keep middle clear for camera view
        overlay.add_widget(Label(text="", size_hint_y=0.6))
        
        # Info Box (Result yahan dikhayega)
        self.info_label = Label(text="Point at a plant and tap Scan", size_hint_y=0.15, 
                                background_color=(0,0,0,0.5), font_size='16sp', halign='center')
        overlay.add_widget(self.info_label)
        
        # Scan Button
        self.scan_btn = Button(text="📷 START AI SCAN", size_hint_y=0.15, 
                               background_color=(0.1, 0.8, 0.1, 0.8), bold=True)
        self.scan_btn.bind(on_press=self.start_ai_scan)
        overlay.add_widget(self.scan_btn)

        self.main_layout.add_widget(overlay)
        self.add_widget(self.main_layout)

    def update_rotate_origin(self, instance, value):
        self.rot.origin = self.cam.center

    def start_ai_scan(self, instance):
        self.info_label.text = "🔍 ANALYZING... Please hold still."
        # Yahan hum AI ko call karenge (Next step mein)
        Clock.schedule_once(self.dummy_ai_logic, 3)

    def dummy_ai_logic(self, dt):
        # Abhi testing ke liye ye badal diya hai
        self.info_label.text = "Success! [Plant Identified]\nReady for Real API connection."
        self.info_label.color = (0.5, 1, 0.5, 1)

# Baki screens (Community/Market) waisi hi rahengi...
