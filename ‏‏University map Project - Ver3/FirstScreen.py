###########################################################
# University Map Project - FirstScreen
# Tools: Kivy and KV(kivymd) Languages Using Python Language
# Kivy and KV(kivymd) are GUI Language
############################################################

from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.core.window import Window

# The size of the screen
Window.size = (350, 600)

# the KV(kivymd) code, its control the design
KV = '''
MDBoxLayout:
    MDFloatLayout:
        Image:
            source: 'imgs/splashScreen.gif'
            allow_stretch: True
            anim_delay: 0.05
            #anim_loop:1
            anim_reset: True
'''


# FirstClass: Use MDApp witch mean kivymd app
class FirstScreen(MDApp):
    def build(self):  # Build method connect between the KV code and python code
        self.title = "University Map"  # The name of the screen
        return Builder.load_string(KV)

    def on_start(self):  # on_start method start directly with starting the app, and it's scheduling 7 seconds
        # to close FirstScreen
        Clock.schedule_once(self.stop, 7)


FirstScreen().run()
