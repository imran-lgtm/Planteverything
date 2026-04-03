# main.py - Yeh main file hai
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.camera import Camera
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.clock import Clock
import requests
import json
from datetime import datetime

# API Keys - Yahan apni keys daalna
PLANTNET_API_KEY = 'YOUR_PLANTNET_API_KEY_HERE'
UNSPLASH_ACCESS_KEY = 'YOUR_UNSPLASH_KEY_HERE'

class PlantDoctorApp(App):
    def build(self):
        self.title = 'Plant Doctor'
        Window.clearcolor = (0.9, 0.95, 0.9, 1)  # Light green background
        
        # Main layout
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Title
        title_label = Label(
            text='[b]🌿 Plant Doctor[/b]',
            markup=True,
            font_size='24sp',
            size_hint_y=0.1,
            color=(0.2, 0.5, 0.2, 1)
        )
        self.main_layout.add_widget(title_label)
        
        # Subtitle
        subtitle = Label(
            text='Pauday ki photo lo, pehchano aur ilaj paao',
            font_size='14sp',
            size_hint_y=0.05,
            color=(0.3, 0.3, 0.3, 1)
        )
        self.main_layout.add_widget(subtitle)
        
        # Camera widget
        self.camera = Camera(
            play=False,
            resolution=(640, 480),
            size_hint_y=0.5
        )
        self.main_layout.add_widget(self.camera)
        
        # Buttons layout
        buttons_layout = BoxLayout(size_hint_y=0.15, spacing=10)
        
        # Start Camera button
        self.camera_btn = Button(
            text='📷 Camera On',
            background_color=(0.2, 0.6, 0.2, 1),
            color=(1, 1, 1, 1),
            font_size='16sp'
        )
        self.camera_btn.bind(on_press=self.toggle_camera)
        buttons_layout.add_widget(self.camera_btn)
        
        # Capture button
        self.capture_btn = Button(
            text='📸 Photo Lo',
            background_color=(0.2, 0.4, 0.8, 1),
            color=(1, 1, 1, 1),
            font_size='16sp',
            disabled=True
        )
        self.capture_btn.bind(on_press=self.capture_photo)
        buttons_layout.add_widget(self.capture_btn)
        
        self.main_layout.add_widget(buttons_layout)
        
        # Status label
        self.status_label = Label(
            text='Camera start karo',
            font_size='14sp',
            size_hint_y=0.05,
            color=(0.5, 0.5, 0.5, 1)
        )
        self.main_layout.add_widget(self.status_label)
        
        # Result area (scrollable)
        self.result_scroll = ScrollView(size_hint_y=0.3)
        self.result_label = Label(
            text='Yahan result ayega...',
            font_size='14sp',
            size_hint_y=None,
            text_size=(Window.width - 40, None),
            color=(0.2, 0.2, 0.2, 1),
            markup=True
        )
        self.result_label.bind(texture_size=self.result_label.setter('size'))
        self.result_scroll.add_widget(self.result_label)
        self.main_layout.add_widget(self.result_scroll)
        
        return self.main_layout
    
    def toggle_camera(self, instance):
        if self.camera.play:
            self.camera.play = False
            self.camera_btn.text = '📷 Camera On'
            self.capture_btn.disabled = True
            self.status_label.text = 'Camera band hai'
        else:
            self.camera.play = True
            self.camera_btn.text = '⏹️ Camera Off'
            self.capture_btn.disabled = False
            self.status_label.text = 'Camera chal raha hai - Photo lo!'
    
    def capture_photo(self, instance):
        self.status_label.text = 'Photo capture ho rahi hai...'
        # Export texture to image
        self.camera.export_to_png('captured_plant.png')
        self.status_label.text = 'Photo save ho gayi, ab identify kar raha hoon...'
        
        # Identify plant
        Clock.schedule_once(self.identify_plant, 0.5)
    
    def identify_plant(self, dt):
        try:
            # Read image
            image_path = 'captured_plant.png'
            
            # Call PlantNet API
            result = self.call_plantnet_api(image_path)
            
            if result and 'results' in result and len(result['results']) > 0:
                plant_data = result['results'][0]
                species = plant_data.get('species', {})
                
                name = species.get('scientificNameWithoutAuthor', 'Unknown')
                common_names = species.get('commonNames', ['Unknown'])
                family = species.get('family', {}).get('scientificName', 'Unknown')
                confidence = plant_data.get('score', 0) * 100
                
                # Get more info from Wikipedia
                wiki_info = self.get_wikipedia_info(name)
                
                # Get images
                images = self.get_plant_images(name)
                
                # Display result in Roman Urdu
                result_text = f"""
[b]🌱 Pauday ka Naam:[/b] {name}
[b]Aam Naam:[/b] {', '.join(common_names)}
[b]Khandan:[/b] {family}
[b]Yaqeen:[/b] {confidence:.1f}%

[b]📍 Maloomat:[/b]
{wiki_info}

[b]💡 Dekh Bhaal:[/b]
• Pani: Regular do, zyada mat do
• Dhoop: Thodi se zyada chahiye
• Garmi: Normal room temperature

[b]🖼️ Tasveer:[/b] {len(images)} images mili hain
                """
                
                self.result_label.text = result_text
                self.status_label.text = 'Ready! - Agli photo lo'
                
                # Show popup with full info
                self.show_result_popup(name, common_names[0], family, wiki_info, images)
                
            else:
                self.result_label.text = 'Pauda pehchan nahi paya. Dobara try karo.'
                self.status_label.text = 'Error - Dobara try karo'
                
        except Exception as e:
            self.result_label.text = f'Error: {str(e)}'
            self.status_label.text = 'Error hua'
    
    def call_plantnet_api(self, image_path):
        """PlantNet API call"""
        url = f'https://my-api.plantnet.org/v2/identify/all?api-key={PLANTNET_API_KEY}'
        
        try:
            with open(image_path, 'rb') as img:
                files = {'images': img}
                data = {'organs': 'auto'}
                
                response = requests.post(url, files=files, data=data, timeout=30)
                
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f'API Error: {response.status_code}')
                    return None
        except Exception as e:
            print(f'Error: {e}')
            return None
    
    def get_wikipedia_info(self, plant_name):
        """Get info from Wikipedia"""
        try:
            url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{plant_name.replace(" ", "_")}'
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                extract = data.get('extract', 'No information available')
                # Convert to simple Roman Urdu style
                return extract[:300] + '...' if len(extract) > 300 else extract
            else:
                return 'Maloomat dastiyab nahi'
        except:
            return 'Internet masla hai'
    
    def get_plant_images(self, plant_name):
        """Get images from Unsplash"""
        try:
            url = f'https://api.unsplash.com/search/photos?query={plant_name}+plant&per_page=3&client_id={UNSPLASH_ACCESS_KEY}'
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return [img['urls']['small'] for img in data.get('results', [])]
            return []
        except:
            return []
    
    def show_result_popup(self, scientific_name, common_name, family, info, images):
        """Show detailed result popup"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add text info
        info_label = Label(
            text=f'[b]{scientific_name}[/b]\n({common_name})\n\n[b]Khandan:[/b] {family}\n\n{info[:200]}...',
            markup=True,
            text_size=(400, None),
            size_hint_y=None
        )
        info_label.bind(texture_size=info_label.setter('size'))
        content.add_widget(info_label)
        
        # Close button
        close_btn = Button(
            text='Band Karein',
            size_hint_y=0.2,
            background_color=(0.8, 0.2, 0.2, 1)
        )
        
        popup = Popup(
            title='Pauday ki Maloomat',
            content=content,
            size_hint=(0.9, 0.8),
            auto_dismiss=False
        )
        
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        
        popup.open()

# App start
if __name__ == '__main__':
    PlantDoctorApp().run()
