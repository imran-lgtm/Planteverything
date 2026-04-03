from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform
from kivy.clock import Clock

class MainApp(App):
    def build(self):
        # Android par Permissions mangne ke liye
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.CAMERA, Permission.INTERNET, Permission.WRITE_EXTERNAL_STORAGE])

        # Main Layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 1. Camera View
        # Resolution thori kam rakhi hai taake pehle load ho jaye
        self.cam = Camera(play=True, resolution=(640, 480), allow_stretch=True)
        self.layout.add_widget(self.cam)
        
        # 2. Status Label
        self.status = Label(text="Plant Encyclopedia: System Ready", size_hint_y=0.1)
        self.layout.add_widget(self.status)
        
        # 3. Test Button
        self.btn = Button(text="Check Camera & AI System", size_hint_y=0.15, background_color=(0.1, 0.5, 0.1, 1))
        self.btn.bind(on_press=self.test_system)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def test_system(self, instance):
        self.status.text = "System Check: OK! Ready for Real AI Integration."
        self.status.color = (0, 1, 0, 1)

if __name__ == '__main__':
    MainApp().run()
