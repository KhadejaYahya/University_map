##################################################################
# University Map Project - ThirdScreen
# Tools: Kivy and KV(kivymd) Languages Using Python Language
# Kivy and KV(kivymd) are GUI Language
##################################################################


from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog

# connect this screen(thirdScreen) with the previous screen(secondScreen)
import secondScreen
# connect this screen with the A star algorithm file
import A_Star_Algorithm

Window.size = (350, 600)

# KV code design the screen
KV = '''
<MySwiper@MDSwiperItem>
BoxLayout:
    id: BoxLayoutID
    orientation: "vertical"
    MDFloatLayout:
        #create the ToolBar 
        MDScreen:
            id: MDSCreenID
            MDToolbar:
                id: toolbar
                title: "University Map - Road"
                elevation: 10
                pos_hint: {"top": 1}
                md_bg_color: [0.54, 0.73, 0.93, 1]

            MDCard: 
                id: CardID_1
                size_hint: None, None
                size: "340dp", "200dp"
                pos_hint: {"center_x": 0.5, "center_y":0.65}
                radius: [15]
                padding: "10dp"
                Image:
                    id: MapImg
                    source:'imgs/map_ver9.png'
                    allow_stretch: True
                    anim_delay: 0.03
                    # anim_loop: 1
                    anim_reset: True
                    keep_ratio: True

            
            FloatLayout:
                MDLabel:
                    id: TripRoad
                    # size_hint: None, None
                    # size: "300dp", "50dp"
                    text: "Trip Road"
                    font_size: 20
                    pos_hint: None, None
                    pos_hint: {"center_x": .8, "center_y": .40}
                MDIconButton:
                    id: TripRoad_Button
                    icon: "map-search"
                    pos_hint: None, None
                    pos_hint: {"center_x": .2, "center_y": .40}
                    on_release: app.show_TripRoad_Dialog()


            # create the swipers for show the Directions
            MDCard:
                id: CardID_2
                size_hint: None, None
                size: "270dp", "100dp"
                pos_hint: {"center_x": 0.5, "center_y":0.25}
                radius: [15]
                # padding: 20
                # spacing: 20


                MDSwiper:
                    id: swiper1
                    # size_hint_y: None
                    pos_hint: {"center_x": 0.2, "center_y":0.5}


                    MySwiper:
                        id: MySwiper1
                        pos_hint: {"left_x": 1, "center_y":0.2}
                        # md_bg_color: [0.37, 0.63, 0.78, 1] 
                        padding: 10
                        MDLabel:
                            id : Label1
                            # text: self.root.Label1()
                            halign: "center"
                            text_color: 0, 0, 1, 1

                    MySwiper:
                        id: MySwiper2
                        padding: 10
                        MDLabel:
                            id: Label2
                            text: "You have reached your destination"
                            halign: "center"
                            text_color: 0, 0, 1, 1


                    MySwiper:
                        id: MySwiper3
                        # md_bg_color: [0.37, 0.63, 0.78, 1] 
                        padding: 10
                        # spacing: 40
                        size: None, None
                        size:[300,300]
                        MDLabel:
                            id: Label3
                            text: "You have reached your destination"
                            halign: "center"
                            text_color: 0, 0, 1, 1


                    MySwiper:
                        id: MySwiper4
                        # md_bg_color: [0.37, 0.63, 0.78, 1] 
                        padding: 10
                        # spacing: 40
                        size: None, None
                        size:[300,300]
                        MDLabel:
                            id: Label4
                            text: "You have reached your destination"
                            halign: "center"
                            text_color: 0, 0, 1, 1


                    MySwiper:
                        id: MySwiper5
                        # md_bg_color: [0.37, 0.63, 0.78, 1] 
                        padding: 10
                        # spacing: 40
                        size: None, None
                        size:[300,300]
                        MDLabel:
                            id: Label5
                            text: "You have reached your destination"
                            halign: "center"
                            text_color: 0, 0, 1, 1


                    MySwiper:
                        id: MySwiper6
                        # md_bg_color: [0.37, 0.63, 0.78, 1] 
                        padding: 10
                        # spacing: 40
                        size: None, None
                        size:[300,300]
                        MDLabel:
                            id: Label6
                            text: "You have reached your destination"
                            halign: "center"
                            text_color: 0, 0, 1, 1


            MDFillRoundFlatButton:
                id: Button
                md_bg_color: [0.37, 0.63, 0.78, 1]
                # print root
                text: "Next step"
                pos_hint: {"center_x": 0.5, "center_y":0.09}
                on_release: 
                    if(swiper1.get_current_index()+1 == (app.num())): app.show_alert_dialog()
                    elif swiper1.get_current_index() < len(swiper1.get_items())-1: swiper1.set_current(swiper1.get_current_index()+1) 
                    elif swiper1.get_current_index() == len(swiper1.get_items())-1: app.show_alert_dialog()


'''


# this method take the result of the A star algorthim file
def get_DirectionListLocally() -> str:
    strDirections = str(A_Star_Algorithm.get_DirectionList()).replace(
        '\'', " ").replace("\"", " ").replace("[", "").replace("]", "")

    print(strDirections)
    return str(strDirections)


# thirdScreen class connect KV codes with python code and add logic features
class thirdScreen(MDApp):
    print("thirdScreen")
    dialog = None

    def __init__(self, **kwargs):
        print("secondScreen/--int--")
        super().__init__(**kwargs)
        self.root = Builder.load_string(KV)

        # create a x variable save start and end  points
        x = secondScreen.start + " , " + secondScreen.end


        # the data of the directions
        # This data is incomplete
        Directions = {
            "Gate 2 , (5) College of Science": ["Turn left ", "Head Straight",
                                                "Turn right to the (5) College of Science"],
            "(5) College of Science , Gate 2": ["Head forward", "Turn left", "Head straight", "Turn right to Gate 2"],

            "Gate 2 , (3) College of Sport": ["Head Straight to (3) College of Sport"],
            "(3) College of Sport , Gate 2": ["Head straight to Gate 2"],

            "Gate 2 , (1) College of Humanities": ["Head straight", "Turn right to (1) College of Humanities"],
            "(1) College of Humanities , Gate 2": ["Turn left", "Heading forword to Gate 2"],

            "(1) College of Humanities , (5) College of Science": ["Head straight to (5) College of Science"],
            "(5) College of Science , (1) College of Humanities": ["Head straight to (1) College of Humanities"],

            "(1) College of Humanities , (3) College of Sport": ["Head straight", "Turn right to (3) College of Sport"],
            "(3) College of Sport , (1) College of Humanities": ["Turn left",
                                                                 "Heading forword to (1) College of Humanities"],

            "(3) College of Sport , (5) College of Science": ["Head straight", "Turn right to (5) College of Science "],
            "(5) College of Science , (3) College of Sport": ["Head straight", "turn left to (3) College of Sport"],

            "(11) College of Computer , Gate 3": ["Heading forward to (gate 3)", "Turn right "],
            "Gate 3 , (11) College of Computer": ["Turn left ", "Heading forward to ( (11) College of Computer)"],

            "Gate 3 , Kindergarten building": ["Turn left ", "Heading forward to ( Kindergarten building )",
                                               " Turn right "],
            "Kindergarten building , Gate 3": ["Turn left ", "Heading forward to ( Gate 3 )", " Turn right "],

            "Gate 3 , (5) College of Science": ["Heading forward to ( (5) College of Science )", " Turn right "],
            "(5) College of Science , Gate 3": ["Turn left", " Turn right ", "Turn left ",
                                                " Heading forward to ( Gate 3 )"],

            "Kindergarten building , (5) College of Science ": ["Heading forward to ( (5) College of Science ) ",
                                                                " Turn left "],
            "(5) College of Science , Kindergarten building": ["Turn left ", " Turn right ",
                                                               "Heading forward to ( Kindergarten building )"],

            "(11) College of Computer , Kindergarten building": ["Heading forward to (Kindergarten building)",
                                                                 "Turn left "],
            "Kindergarten building , (11) College of Computer": ["Turn right ",
                                                                 "Heading forward to ( (11) College of  Computer)"],

            "(5) College of Science , (11) College of Computer": ["Turn left", " Turn right ", "Turn left ",
                                                                  " Heading forward to ( Gate 3 ) ", " Turn right ",
                                                                  "Heading forward to ( (11) College of Computer)"],
            "(11) College of Computer , (5) College of Science": [" Heading forward to ( Gate 3 ) ", " Turn left ",
                                                                  " Heading forward to ( (5) College of Science ) ",
                                                                  " Turn right ", " Turn left "],

            "Gate 3 , Gate 2": [" Turn right ", " Heading forward to ( Gate 2)", " Turn right "],
            "Gate 2 , Gate 3": ["Turn Left", "Go Straight North"],

            "Gate 2 , (11) College of Computer": ["Turn left", " Passing through ( Gate 3 ) ",
                                                  " Heading forward to (11) College of  Computer "],
            "(11) College of Computer , Gate 2": [" Heading forward to (Gate 2)", " Passing through (Gate 3)",
                                                  "Turn right"],
        }

        print(x)
        global num_directione
        # calculate the numbers of the directions we have and use this variable to control how much swiper is view
        num_directione = len(Directions[x])
        print(num_directione)

        # these conditions check if the numbers of the directions is greater than or equal (number of current swiper)
        if num_directione >= 1:
            # if true , make label1 form swiper1 show the direction 0 from the list
            self.root.ids.Label1.text = "From " + secondScreen.start + " " + Directions[x][0]

        if num_directione >= 2:
            self.root.ids.Label2.text = Directions[x][1]

        if num_directione >= 3:
            self.root.ids.Label3.text = Directions[x][2]

        if num_directione >= 4:
            self.root.ids.Label4.text = Directions[x][3]

        if num_directione >= 5:
            self.root.ids.Label5.text = Directions[x][4]


    def num(self):
        return num_directione + 1

    # this method is open the dialog (popper) screen
    def show_alert_dialog(self):
        # if not self.dialog:
        self.dialog = MDDialog(
            title="Your Trip Ends Here",
            text="Thank you for using 'University Map' app",
            buttons=[
                MDFlatButton(
                    text="Close The App", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                )
            ]
        )
        self.dialog.open()

    # close the dialog
    def close_dialog(self, obj):
        App.get_running_app().stop()

    # dialog for show the Trip Road from the A star Algorithm
    def show_TripRoad_Dialog(self):
        self.dialog = MDDialog(
            title="Trip Road :",
            text=get_DirectionListLocally(),
        )
        self.dialog.open()


    def build(self):
        return self.root


thirdScreen().run()
