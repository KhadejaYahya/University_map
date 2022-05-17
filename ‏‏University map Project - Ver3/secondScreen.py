##################################################################
# University Map Project - SecondScreen
# Tools: Kivy and KV(kivymd) Languages Using Python Language
# Kivy and KV(kivymd) are GUI Language
##################################################################

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

# connect this screen(SecondScreen) with the previous screen(FirstScreen)
import FirstScreen

Window.size = (350, 600)


# the KV(kivymd) code
KV = '''

#:import MDFillRoundFlatButton kivymd.uix.button.MDFillRoundFlatButton

<IconListItem>
BoxLayout:
    MDFloatLayout:
    
    
        # Add image the background
        Image:
            id: img
            source:'imgs/secondScreen.png'
            allow_stretch: True
            anim_delay: 0.03
            # anim_loop: 1
            anim_reset: True
            padding: "10dp"


        # add textField (Starting Point)
        MDScreen
            MDTextField:
                id: Starting_point
                pos_hint: {'center_x': .5, 'center_y': .6}
                size_hint_x: None
                width: "250dp"
                hint_text: "Starting Point"
                icon_right: "map-search"
                on_focus: if self.focus: app.menu1.open()


        # add TextField (Destination)
        MDScreen
            MDTextField:
                id: Destination
                pos_hint: {'center_x': .5, 'center_y': .45}
                size_hint_x: None
                width: "250dp"
                hint_text: "Destination"
                icon_right: "map-search"
                on_focus: if self.focus: app.menu2.open()
        
        # add button (Start)
        # to move to next screen (thirdScreen) by closing this screen(secondScreen)
        MDFillRoundFlatButton:
            text: "Start"
            # icon: "map-marker-check"
            # text_color: 
            md_bg_color: [0.37, 0.63, 0.78, 1]       
            pos_hint: {'center_x': .5, 'center_y': .30}
            on_release: 
                app.close_application()
            
'''

global start
global end

# secondScreen class connect KV codes with python code and add logic features
class secondScreen(MDApp):
    print("secondScreen")

    # this method is creating the dropdown menu items
    def __init__(self, **kwargs):
        print("secondScreen/--int--")
        super().__init__(**kwargs)
        self.title = "University Map"
        self.screen = Builder.load_string(KV)
        menu_items1 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "Gate 2",
                "on_release": lambda x="Gate 2": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "Gate 3",
                "on_release": lambda x="Gate 3": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "(1) College of Humanities",
                "on_release": lambda x="(1) College of Humanities": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "(3) College of Sport",
                "on_release": lambda x="(3) College of Sport": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "(5) College of Science",
                "on_release": lambda x="(5) College of Science": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "(11) College of Computer",
                "on_release": lambda x="(11) College of Computer": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "Kindergarten building",
                "on_release": lambda x="Kindergarten building": self.set_item1(x),
            }
        ]
        menu_items2 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "Gate 2",
                "on_release": lambda x="Gate 2": self.set_item2(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "Gate 3",
                "on_release": lambda x="Gate 3": self.set_item2(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "(1) College of Humanities",
                "on_release": lambda x="(1) College of Humanities": self.set_item2(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "(3) College of Sport",
                "on_release": lambda x="(3) College of Sport": self.set_item2(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "(5) College of Science",
                "on_release": lambda x="(5) College of Science": self.set_item2(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "(11) College of Computer",
                "on_release": lambda x="(11) College of Computer": self.set_item2(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": "Kindergarten building",
                "on_release": lambda x="Kindergarten building": self.set_item2(x),
            }
        ]
        self.menu1 = MDDropdownMenu(
            caller=self.screen.ids.Starting_point,
            max_height=dp(200),
            items=menu_items1,
            position="bottom",
            ver_growth="down",
            width_mult=4,
        )

        self.menu2 = MDDropdownMenu(
            caller=self.screen.ids.Destination,
            max_height=dp(200),
            items=menu_items2,
            position="bottom",
            ver_growth="down",
            width_mult=4,
        )

    # this method is read the user's choice for the starting point menu
    def set_item1(self, text__item):
        print("secondScreen/set_item1")
        self.screen.ids.Starting_point.text = text__item
        print("Starting Point :" + self.screen.ids.Starting_point.text)
        self.menu1.dismiss()
        global start
        start = self.screen.ids.Starting_point.text

    # this method is read the user's choice from the Destination menu
    def set_item2(self, text__item):
        print("secondScreen/set_item2")
        self.screen.ids.Destination.text = text__item
        print("Destination :" + self.screen.ids.Destination.text)
        self.menu2.dismiss()
        global end
        end = self.screen.ids.Destination.text

    # this method is stop showing the screen when the user press button start
    # it's stop this screen to show the next screen(ThirdScreen)
    def close_application(self):
        # closing application
        App.get_running_app().stop()

    def build(self):
        print("secondScreen/build")
        return self.screen


secondScreen().run()
