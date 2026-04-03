import requests
import base64
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.utils import platform

# --- YOUR API KEY LOADED ---
API_KEY = "j3WHHjd9qztf9exl6JsJt3G2NWX7otMlnJ3d6yAJ0ZGxkmDwlb"
API_URL = "https://api.plant.id/v3/identification"

class PlantScanner(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        
        # Header with your name
        self.add_widget(Label(text="🌿 IMRAN(DJZ) AI SCANNER 🌿", size_hint_y=0.1, font_size='22sp', bold=True, color=(0.4, 1, 0.4, 1)))
        
        # Camera (Optimized for Pixel 6)
        self.cam = Camera(play=True, resolution=(1280, 720), size_hint=(1, 0.6), allow_stretch=True)
        self.add_widget(self.cam)
        
        # Result Area
        self.result_label = Label(text="Focus on plant & tap Analyze", size_hint_y=0.2, halign='center', font_size='16sp', color=(1, 1, 1, 1))
        self.add_widget(self.result_label)
        
        # Action Button
        self.btn = Button(text="📷 ANALYZE PLANT & HEALTH", size_hint_y=0.1, background_color=(0.1, 0.6, 0.1, 1), bold=True)
        self.btn.bind(on_press=self.scan_now)
        self.add_widget(self.btn)

    def scan_now(self, instance):
        self.result_label.text = "AI is thinking... (Sending to Server)"
        self.cam.export_to_png("plant_image.png")
        self.call_api()

    def call_api(self):
        try:
            with open("plant_image.png", "rb") as file:
                image_64 = base64.b64encode(file.read()).decode('ascii')

            payload = {
                "images": [image_64],
                "health": "all",
                "similar_images": True
            }
            
            headers = {"Api-Key": API_KEY, "Content-Type": "application/json"}
            
            # Sending request to Plant.id v3
            response = requests.post(API_URL, json=payload, headers=headers)
            res_data = response.json()

            if response.status_code in [200, 201]:
                # Extraction
                suggestion = res_data['result']['classification']['suggestions'][0]
                name = suggestion['name']
                prob = int(suggestion['probability'] * 100)
                
                # Health Check
                is_healthy = res_data['result']['is_plant']['binary']
                health_status = "Healthy ✅" if is_healthy else "Check for Disease ⚠️"
                
                self.result_label.text = f"Result: {name}\nAccuracy: {prob}%\nStatus: {health_status}"
            else:
                self.result_label.text = f"Error: {response.status_code}\nCheck API Quota"
        except Exception as e:
            self.result_label.text = "Connection Error! Check Internet"

class MainApp(App):
    def build(self):
        return PlantScanner()

if __name__ == '__main__':
    MainApp().run()
