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
import os

# Permissions for Android
def start_permissions():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE, Permission.INTERNET])

class ScannerScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.layout = BoxLayout(orientation='vertical')

        # Camera Section (75%)
        self.cam_container = BoxLayout(size_hint=(1, 0.75))
        self.cam = Camera(play=True, resolution=(1280, 720), allow_stretch=True, keep_ratio=False)
        
        with self.cam.canvas.before:
            PushMatrix()
            self.rot = Rotate(angle=-90, origin=self.cam.center)
        with self.cam.canvas.after:
            PopMatrix()
        self.cam.bind(pos=self.update_rotate_origin, size=self.update_rotate_origin)
        
        self.cam_container.add_widget(self.cam)
        self.layout.add_widget(self.cam_container)

        # UI Section (25%)
        self.ui_panel = BoxLayout(orientation='vertical', size_hint=(1, 0.25), padding=10, spacing=5)
        self.info_label = Label(text="🌿 Ready to Scan\n(Ensure Internet is ON)", font_size='14sp', halign='center')
        self.ui_panel.add_widget(self.info_label)
        
        self.scan_btn = Button(text="📷 IDENTIFY PLANT (AI)", background_color=(0.1, 0.6, 0.1, 1), bold=True)
        self.scan_btn.bind(on_press=self.capture_photo)
        self.ui_panel.add_widget(self.scan_btn)

        self.layout.add_widget(self.ui_panel)
        self.add_widget(self.layout)

    def update_rotate_origin(self, instance, value):
        self.rot.origin = self.cam.center

    def capture_photo(self, instance):
        self.info_label.text = "🔍 Capturing Photo..."
        # Photo path
        self.photo_path = os.path.join(App.get_running_app().user_data_dir, "plant_scan.png")
        self.cam.export_to_png(self.photo_path)
        Clock.schedule_once(self.identify_via_ai, 1)

    def identify_via_ai(self, dt):
        self.info_label.text = "📡 Sending to AI Server..."
        
        # --- API SETTINGS ---
        API_KEY = "2GvI... (Demo Key)" # Yahan asli key chahiye
        URL = "https://api.plant.id/v2/identify"

        try:
            with open(self.photo_path, "rb") as file:
                image_64 = base64.b64encode(file.read()).decode("ascii")

            payload = {
                "images": [image_64],
                "modifiers": ["crops_fast", "similar_images"],
                "plant_details": ["common_names", "taxonomy"]
            }
            headers = {"Content-Type": "application/json", "Api-Key": API_KEY}

            # Timeout set kiya hai taake app hang na ho
            response = requests.post(URL, json=payload, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                plant_name = data['suggestions'][0]['plant_name']
                confidence = int(data['suggestions'][0]['probability'] * 100)
                self.info_label.text = f"✅ FOUND: {plant_name}\nConfidence: {confidence}%\nDev: Imran(djz)"
                self.info_label.color = (0.3, 1, 0.3, 1)
            else:
                self.info_label.text = f"⚠️ Server Busy (Error {response.status_code})\nTry Again Later."
        
        except Exception as e:
            self.info_label.text = "❌ Connection Failed!\nCheck WiFi/Data or API Key."
            print(f"Error: {e}")

class PlantEncyclopediaApp(App):
    def build(self):
        start_permissions()
        sm = ScreenManager()
        sm.add_widget(ScannerScreen(name='scanner'))
        return sm

if __name__ == '__main__':
    PlantEncyclopediaApp().run()
