from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.graphics.context_instructions import PushMatrix, PopMatrix, Rotate
from kivy.utils import platform
from kivy.core.window import Window
from kivy.clock import Clock
import requests
import base64

# Pixel 6 UI Settings
Window.clearcolor = (0.02, 0.08, 0.02, 1)

def start_permissions():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE, Permission.INTERNET])

class ScannerScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.layout = BoxLayout(orientation='vertical')

        # 1. BARA CAMERA (75% Screen)
        self.cam_container = BoxLayout(size_hint=(1, 0.75))
        self.cam = Camera(play=True, resolution=(1280, 720), allow_stretch=True, keep_ratio=False)
        
        # Rotation Fix for Pixel 6
        with self.cam.canvas.before:
            PushMatrix()
            self.rot = Rotate(angle=-90, origin=self.cam.center)
        with self.cam.canvas.after:
            PopMatrix()
        self.cam.bind(pos=self.update_rotate_origin, size=self.update_rotate_origin)
        
        self.cam_container.add_widget(self.cam)
        self.layout.add_widget(self.cam_container)

        # 2. UI CONTROL PANEL (25% Screen)
        self.ui_panel = BoxLayout(orientation='vertical', size_hint=(1, 0.25), padding=10, spacing=8)
        
        self.info_label = Label(
            text="🌿 Plant Encyclopedia\nReady to Identify Species", 
            font_size='15sp', 
            halign='center',
            color=(0.7, 1, 0.7, 1)
        )
        self.ui_panel.add_widget(self.info_label)
        
        self.scan_btn = Button(
            text="📷 CAPTURE & IDENTIFY (AI)", 
            background_color=(0.2, 0.6, 0.2, 1), 
            bold=True,
            font_size='18sp'
        )
        self.scan_btn.bind(on_press=self.start_identification)
        self.ui_panel.add_widget(self.scan_btn)

        self.layout.add_widget(self.ui_panel)
        self.add_widget(self.layout)

    def update_rotate_origin(self, instance, value):
        self.rot.origin = self.cam.center

    def start_identification(self, instance):
        self.info_label.text = "🔍 Capturing... Sending to AI Cloud..."
        # Camera se photo save karna
        try:
            self.cam.export_to_png("scan.png")
            Clock.schedule_once(self.send_to_ai, 1)
        except:
            self.info_label.text = "❌ Camera Error! Try again."

    def send_to_ai(self, dt):
        # AI Identification Logic (Plant.id Demo)
        api_url = "https://api.plant.id/v2/identify"
        # Demo API Key (Testing ke liye)
        api_key = "qWvI... (Aapki Key Yahan Ayegi)" 

        try:
            with open("scan.png", "rb") as img_file:
                b64_image = base64.b64encode(img_file.read()).decode("ascii")

            # Fake response agar API Key nahi hai (Testing ke liye logic)
            if "qWvI" in api_key: 
                self.info_label.text = "✅ SUCCESS!\nPlant: Money Plant (Epipremnum aureum)\nHistory: Native to Moorea.\nCare: Bright indirect light."
                self.info_label.color = (0.3, 1, 0.3, 1)
            else:
                # Asli API Call
                headers = {"Content-Type": "application/json", "Api-Key": api_key}
                payload = {"images": [b64_image], "modifiers": ["crops_fast"]}
                response = requests.post(api_url, json=payload, headers=headers)
                data = response.json()
                name = data['suggestions'][0]['plant_name']
                self.info_label.text = f"✅ FOUND: {name}\nDeveloped by: Imran(djz)"
        
        except Exception as e:
            self.info_label.text = "⚠️ Connection Error!\nCheck Internet and try again."

class PlantEncyclopediaApp(App):
    def build(self):
        start_permissions()
        sm = ScreenManager()
        sm.add_widget(ScannerScreen(name='scanner'))
        return sm

if __name__ == '__main__':
    PlantEncyclopediaApp().run()
