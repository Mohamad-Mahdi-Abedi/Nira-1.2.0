from kivy.core.clipboard import Clipboard
from bidi.algorithm import get_display
import arabic_reshaper 
from kivy.lang import Builder
from kivy.metrics import dp
from kivy_garden.mapview import MapView
from kivy.clock import Clock, mainthread
import base64
from kivymd.uix.relativelayout import MDRelativeLayout
import json
import datetime
import jdatetime
from websockets.sync.client import connect
import threading
from kivymd.uix.fitimage import FitImage
from kivymd.uix.list import MDList
from kivymd.app import MDApp
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.utils import asynckivy
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.button import Button
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.snackbar import MDSnackbar
import os
from kivy.core.audio import SoundLoader
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty, DictProperty, ObjectProperty, NumericProperty, BooleanProperty
from kivy.app import App
from kivy.uix.modalview import ModalView
import random
from kivymd.uix.filemanager import MDFileManager
import math
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import wikipedia
import threading
from kivy.clock import Clock
from googletrans import Translator
from arabic_reshaper import reshape
from bidi.algorithm import get_display
import speedtest
from kivy.lang import Builder
from kivy.app import App
from kivymd.uix.button import MDRaisedButton
from kivy.uix.label import Label
import random
import time
from threading import Thread

KV = '''
#:import MapSource kivy_garden.mapview.MapSource
#:import asynckivy kivymd.utils.asynckivy


<TypeMapElement>
    orientation: "vertical"
    adaptive_height: True
    spacing: "8dp"

    MDIconButton:
        id: icon
        icon: root.icon
        md_bg_color: "#EDF1F9" if not root.selected else app.theme_cls.primary_color
        pos_hint: {"center_x": .5}
        theme_icon_color: "Custom"
        icon_color: "white" if root.selected else "black"
        on_release: app.set_active_element(root, root.title.lower())

    MDLabel:
        font_size: "14sp"
        text: root.title
        pos_hint: {"center_x": .5}
        halign: "center"
        adaptive_height: True

<ContentNavigationDrawer>:
    padding: "5dp"
    spacing: "5dp"
    orientation: "vertical"
    MDCard:
        orientation: "vertical"
        padding: 0, 0, 0 ,0
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 2
        shadow_offset: 0, -2
        MDBoxLayout:
            orientation: "vertical"
            padding: 20
            spacing: 20
            FitImage:
                source: "DefaultAccountTile.png"
                radius: [10,]
                size_hint_x: 1
                size_hint_y: 1

            MDFillRoundFlatIconButton:
                text: "NiraGuide"
                size_hint_x: 1
                on_release: app.go_to_guide()
                pos_hint: {"center_x": .5}

            MDFillRoundFlatIconButton:
                text: "Help"
                size_hint_x: 1
                on_release: app.get_help()
                pos_hint: {"center_x": .5}

            MDFillRoundFlatIconButton:
                text: "More theme option"
                size_hint_x: 1
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release: app.chang_color_them()

<MagicButton@MagicBehavior+MDIconButton>

    MDRelativeLayout:

        FitImage:
            source: "pro.png"
            radius: [20,]

        MDBoxLayout:
            adaptive_height: True
            spacing: "12dp"

            MagicButton:
                id: icon
                icon: "eye-outline"

            MDLabel:
                text: "Drag to down for show"
                size_hint_y: None
                height: self.texture_size[1]
                pos_hint: {"center_y": .5}

<SwipeToDeleteItem>:
    size_hint_y: None

    MDCardSwipeFrontBox:
        size_hint_y: None
        MDBoxLayout:
            padding: "15dp"
            spacing: "10dp"
            MDIconButton:
                icon: 'cog'
                on_release: app.show_dialogpanel_for_message(root),app.on_item_release(root)
            MDLabel:
                text: root.text
                font_name:'tanha.ttf'

<YCToDeleteItem>:
    size_hint_y: None

    MDCardSwipeFrontBox:
        size_hint_y: None
        MDBoxLayout:
            padding: "15dp"
            spacing: "10dp"
            MDLabel:
                text: root.text
                font_name:'tanha.ttf'

<FileToDeleteItem>:
    size_hint_y: None

    MDCardSwipeFrontBox:
        size_hint_y: None
        MDBoxLayout:
            padding: "15dp"
            spacing: "10dp"
            MDIconButton:
                icon: 'eye'
                # on_release: app.show_file(root)
            MDLabel:
                text: root.text
                font_name:'tanha.ttf'

<ContactListItem>:
    size_hint_y: None
    MDCardSwipeFrontBox:
        on_release: app.go_to_messages_for_this_people(root)
        MDBoxLayout:
            padding: "15dp"
            spacing: "10dp"
            MDIconButton:
                icon: "contact-icon.png"
            MDLabel:
                id: content
                text: root.text
                font_name: 'tanha.ttf'


# <GroupListItem>:
#     size_hint_y: None

#     MDCardSwipeFrontBox:
#         MDList:
#             TwoLineAvatarListItem:
#                 id: content
#                 text: root.text
#                 secondary_text: "group"
#                 _no_ripple_effect: True
#                 on_release: app.go_to_messages_for_this_people(self.text, self.secondary_text)
#                 ImageLeftWidget:
#                     source: "group-icon.png"

# <ChanelListItem>:
#     size_hint_y: None

#     MDCardSwipeFrontBox:
#         MDList:
#             TwoLineAvatarListItem:
#                 id: content
#                 text: root.text
#                 secondary_text: "chanel"
#                 _no_ripple_effect: True
#                 on_release: app.go_to_messages_for_this_people(self.text, self.secondary_text)
#                 ImageLeftWidget:
#                     source: "chanel-icon.png"

ScreenManager:

    MDScreen:
        name: "welcom_screen"
        id: "welcom_screen"
        MDBoxLayout:
            spacing: 10
            padding: 10
            orientation: "vertical"
            FitImage:
                source: "icon_2.png"
        MDBoxLayout:
            spacing: 10
            padding: 10
            MDRectangleFlatIconButton:
                text: '  creat_account'
                icon: 'creat account.png'
                size_hint_x: 1
                text_color: "white"
                md_bg_color: 0.3176470588235294, 0.17647058823529413, 0.6588235294117647, 1
                on_release: app.go_to_nira('creat_account')
            MDRectangleFlatIconButton:
                text: '  login'
                icon: 'sign in.png'
                size_hint_x: 1
                text_color: "white"
                md_bg_color: 0.3176470588235294, 0.17647058823529413, 0.6588235294117647, 1
                on_release: app.go_to_nira('login')

    MDScreen:
        name: 'main_login'
        MDBoxLayout:
            padding: "10dp"
            orientation: "vertical"
            height: "48dp"
            FitImage:
                source: 'login_img_2.png'

            MDTextFieldPersian:
                font_name: "tanha.ttf"
                id: user_name_login
                hint_text: "User name"
                size_hint_x: 1

            MDBoxLayout:
                size_hint_y: None

                MDTextField:
                    id: password_login
                    hint_text: "Password"
                    password: True
                    size_hint_x: 0.9
                    font_name: "tanha.ttf"

                MDIconButton:
                    icon: "eye-off"
                    _no_ripple_effect: True
                    size_hint_x: 0.1
                    # pos_hint: {"center_y": .5}
                    # pos: password_login.width - self.width + dp(8), 0
                    on_release:
                        self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                        password_login.password = False if password_login.password is True else True
                
            MDFlatButton:
                text: "login"
                md_bg_color: 0.3176470588235294, 0.17647058823529413, 0.6588235294117647, 1
                size_hint_x: 1
                on_release: app.login()

    MDScreen:
        name: 'main_creat_account'
        id: main_creat_account
        MDBoxLayout:
            padding: "10dp"
            orientation: "vertical"
            height: "48dp"
            FitImage:
                source: 'creat_account_img_2.png'

            MDTextFieldPersian:
                font_name: "tanha.ttf"
                id: user_name_creat
                hint_text: "User name"
                size_hint_x: 

            MDBoxLayout:
                size_hint_y: None

                MDTextField:
                    id: password_creat
                    hint_text: "Password"
                    password: True
                    size_hint_x: 0.9
                    font_name: "tanha.ttf"

                MDIconButton:
                    icon: "eye-off"
                    _no_ripple_effect: True
                    size_hint_x: 0.1
                    # pos_hint: {"center_y": .5}
                    # pos: password_creat.width - self.width + dp(8), 0
                    on_release:
                        self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                        password_creat.password = False if password_creat.password is True else True
                
            MDFlatButton:
                text: "creat"
                md_bg_color: 0.3176470588235294, 0.17647058823529413, 0.6588235294117647, 1
                size_hint_x: 1
                on_release: app.creat()

    MDScreen:
        name: "main"
        id: "main"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                id: toolbar
                pos_hint: {"top": 1}
                elevation: 5
                title: "Nira"
                left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                right_action_items: [["pencil", lambda x: app.creat_contact()]]

            MDBoxLayout:
                orientation:'vertical'

                MDBottomNavigation:
                    panel_color: 0.07, 0.07, 0.07

                    MDBottomNavigationItem:
                        name: 'screen 2'
                        text: 'chat'
                        icon: 'chat4.png'
                        MDBoxLayout:
                            orientation:'vertical'
                            spacing: 10
                            MDScrollView:
                                id: contacts_list_view
                                scroll_timeout: 0
                                MDList:
                                    id: contacts_list
                                    spacing: 10
                                    padding: 10

                    MDBottomNavigationItem:
                        name: 'screen 1'
                        text: 'extensions'
                        icon: 'extensions.png'
                        MDBoxLayout:
                            orientation:'vertical'
                            MDScrollView:
                                id: apps_view
                                scroll_timeout: 0
                                MDList:
                                    id: apps_list
                                    spacing: 10
                                    padding: 10
                                    MDCardSwipeFrontBox:
                                        size_hint_y: None
                                        on_release: app.start_game()
                                        MDBoxLayout:
                                            padding: "15dp"
                                            spacing: "10dp"
                                            MDIconButton:
                                                icon: 'mine_sweeper.png'
                                            MDLabel:
                                                text: "Mine Sweeper"

                                    MDCardSwipeFrontBox:
                                        size_hint_y: None
                                        on_release: app.start_calculator()
                                        MDBoxLayout:
                                            padding: "15dp"
                                            spacing: "10dp"
                                            MDIconButton:
                                                icon: 'calculator.png'
                                            MDLabel:
                                                text: "Calculator"

                                    MDCardSwipeFrontBox:
                                        size_hint_y: None
                                        on_release: app.start_maps()
                                        MDBoxLayout:
                                            padding: "15dp"
                                            spacing: "10dp"
                                            MDIconButton:
                                                icon: 'maps.png'
                                            MDLabel:
                                                text: "Nira map viewer"

                                    MDCardSwipeFrontBox:
                                        size_hint_y: None
                                        on_release: app.start_translating()
                                        MDBoxLayout:
                                            padding: "15dp"
                                            spacing: "10dp"
                                            MDIconButton:
                                                icon: 'translate.png'
                                            MDLabel:
                                                text: "Nira translator"

                                    MDCardSwipeFrontBox:
                                        size_hint_y: None
                                        on_release: app.start_math_chat()
                                        MDBoxLayout:
                                            padding: "15dp"
                                            spacing: "10dp"
                                            MDIconButton:
                                                icon: 'math_chat.png'
                                            MDLabel:
                                                text: "Nira AI"

                                    MDCardSwipeFrontBox:
                                        size_hint_y: None
                                        on_release: app.start_nira_wiki()
                                        MDBoxLayout:
                                            padding: "15dp"
                                            spacing: "10dp"
                                            MDIconButton:
                                                icon: 'W.png'
                                            MDLabel:
                                                text: "Nira Wiki Pedia"

                                    MDCardSwipeFrontBox:
                                        size_hint_y: None
                                        on_release: app.start_nira_internet_speed()
                                        MDBoxLayout:
                                            padding: "15dp"
                                            spacing: "10dp"
                                            MDIconButton:
                                                icon: 'internet speed.png'
                                            MDLabel:
                                                text: "Nira Internet Speed"

                                    MDCardSwipeFrontBox:
                                        size_hint_y: None
                                        on_release: app.start_nira_touch_speed()
                                        MDBoxLayout:
                                            padding: "15dp"
                                            spacing: "10dp"
                                            MDIconButton:
                                                icon: 'klick_speed.png'
                                            MDLabel:
                                                text: "Nira Touch Speed Cecker"

                                    MDCardSwipeFrontBox:
                                        size_hint_y: None
                                        on_release: app.start_reaction_speed_test()
                                        MDBoxLayout:
                                            padding: "15dp"
                                            spacing: "10dp"
                                            MDIconButton:
                                                icon: 'reaction_speed.png'
                                            MDLabel:
                                                text: "Nira Reaction Tester"
                    
        MDNavigationLayout:
            orientation: "horizontal"
            MDNavigationDrawer:
                id: nav_drawer

                ContentNavigationDrawer:

                    nav_drawer: nav_drawer

    MDScreen:
        name: "chat"
        id: "chat"
        FitImage:
            id: backgrand

        MDBoxLayout:
            orientation: "vertical"

            MDTopAppBar:
                title: "Chat"
                font_name: "tanha.ttf"
                id: chat_app_bar
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
                right_action_items: [["dots-vertical", lambda x: app.callback(x)]]

            MDScrollView:
                id: scroll
                scroll_timeout: 0
                MDList:
                    id: md_list
                    spacing: 10
                    padding: 10

            MDTopAppBar:
                id: paiin
                md_bg_color: [0, 0, 0, 1]
                MDBoxLayout:
                    padding: 5
                    spacing: 10
                    orientation: "horizontal"
                    size_hint_y: None
                    height: "48dp"
                    MDFloatingActionButton:
                        id: add
                        # icon: "attachment"
                        icon: "add.png"
                        on_release: app.show_example_grid_bottom_sheet()
                    MDTextFieldPersian:
                        font_name: "tanha.ttf"
                        id: message
                        hint_text: " Chat"
                        # multiline: True
                        # mode: "rectangle"
                        # mode: "fill"
                        max_text_length: 100
                    MDFloatingActionButton:
                        id: send
                        icon: "send.png"
                        on_release: app.change_send_mode(), app.send_message()

    MDScreen:
        name: 'creat_contact'
        id: 'creat_contact'
        FitImage:
            source: "creat.png"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "Add A Item"
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
                right_action_items: [["empty.png",]]
            MDBoxLayout:
                spacing: "20dp"
                padding: "20dp"
                orientation: "vertical"
                MDRaisedButton:
                    text: 'Add Contact'
                    size_hint_x: 1
                    on_release: app.creat_contact_on_list()
                # MDRaisedButton:
                #     text: 'Add Group'
                #     size_hint_x: 1
                #     on_release: app.creat_group_on_list()
                # MDRaisedButton:
                #     text: 'Add Chanel'
                #     size_hint_x: 1
                #     on_release: app.creat_chanel_on_list()

    MDScreen:
        name: "empty"
        id: "empty"

    MDScreen:
        name: 'empty_for_game'
        id: 'empty_for_game'
        MDTopAppBar:
            id: toolbar
            pos_hint: {"top": 1}
            elevation: 5
            title: "Mine Sweeper"
            left_action_items: [["chevron-left", lambda x: app.back_to_main_from_game()]]

    MDScreen:
        name: 'file'
        id: 'file'
        MDBoxLayout:
            orientation: 'vertical'

            MDTopAppBar:
                title: "NiraFileManager"
                left_action_items: [["chevron-left", lambda x: app.home_chat()]]


            MDFloatLayout:

                MDFloatingActionButton:
                    icon: "folder"
                    pos_hint: {'center_x': .5, 'center_y': .6}
                    on_release: app.file_manager_open()

    MDScreen:
        name: "chang_color_them"
        id: "chang_color_them"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "Color them"
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]

            MDScrollView:
                id: scroll
                scroll_timeout: 0
                MDList:
                    spacing: 10
                    padding: 10
                    size_hint_y: None
                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text: "Red"
                            on_release: app.on_click_red()
                            md_bg_color: 0.8274509803921568, 0.1843137254901961, 0.1843137254901961, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text: "Purple"
                            on_release: app.on_click_purple()
                            md_bg_color: 0.4823529411764706, 0.12156862745098039, 0.6352941176470588, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None   
                        MDFlatButton:
                            text:"Indigo"
                            on_release:app.on_click_indigo()
                            md_bg_color: 0.18823529411764706, 0.24705882352941178, 0.6235294117647059, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"LightBlue"
                            on_release:app.on_click_light_blue()
                            md_bg_color: 0.00784313725490196, 0.5333333333333333, 0.8196078431372549, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"Teal"
                            on_release:app.on_click_teal()
                            md_bg_color: 0, 0.5882352941176471, 0.5333333333333333
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"LightGreen"
                            on_release:app.on_click_light_green()
                            md_bg_color: 0.40784313725490196, 0.6235294117647059, 0.2196078431372549, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"Yellow"
                            on_release:app.on_click_yellow()
                            md_bg_color: 0.984313725490196, 0.7529411764705882, 0.17647058823529413, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"Orange"
                            on_release:app.on_click_orange()
                            md_bg_color: 0.9607843137254902, 0.48627450980392156, 0.0, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"Brown"
                            on_release:app.on_click_brown()
                            md_bg_color: 0.36470588235294116, 0.25098039215686274, 0.21568627450980393, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"BlueGray"
                            on_release:app.on_click_blue_gray()
                            md_bg_color: 0.27058823529411763, 0.35294117647058826, 0.39215686274509803, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text: "Pink"
                            on_release: app.on_click_pink()
                            md_bg_color: 0.7607843137254902, 0.09411764705882353, 0.3568627450980392, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text: "DeepPurple"
                            on_release: app.on_click_deep_purple()
                            md_bg_color: 0.3176470588235294, 0.17647058823529413, 0.6588235294117647, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"Blue"
                            on_release:app.on_click_blue()
                            md_bg_color: 0.09803921568627451, 0.4627450980392157, 0.8235294117647058, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"Cyan"
                            on_release:app.on_click_cyan()
                            md_bg_color: 0, 0.7372549019607843, 0.8313725490196078
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"Green"
                            on_release:app.on_click_green()
                            md_bg_color: 0.2196078431372549, 0.5568627450980392, 0.23529411764705882, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"Lime"
                            on_release:app.on_click_lime()
                            md_bg_color: 0.6862745098039216, 0.7058823529411765, 0.16862745098039217, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"Amber"
                            on_release:app.on_click_amber()
                            md_bg_color: 1.0, 0.6274509803921569, 0.0, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"DeepOrange"
                            on_release:app.on_click_deep_orange()
                            md_bg_color: 0.9019607843137255, 0.2901960784313726, 0.09803921568627451, 1
                            size_hint_x: 1
                            size_hint_y: 1

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        MDFlatButton:
                            text:"Gray"
                            on_release:app.on_click_gray()
                            md_bg_color: 0.3803921568627451, 0.3803921568627451, 0.3803921568627451, 1
                            size_hint_x: 1
                            size_hint_y: 1

    MDScreen:
        name: 'maps'
        id: 'maps'
        CustomMapView:
            bottom_sheet: bottom_sheet
            map_source: MapSource(url=app.map_sources[app.current_map])
            lat: 46.5124
            lon: 47.9812
            zoom: 12

        MDTopAppBar:
            title: "Nira map viewer"
            left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
            right_action_items: [['menu', lambda x: bottom_sheet.open()]]

        MDBottomSheet:
            id: bottom_sheet
            elevation: 2
            shadow_softness: 6
            # bg_color: "white"
            type: "standard"
            max_opening_height: self.height
            default_opening_height: self.max_opening_height
            adaptive_height: True
            on_open: asynckivy.start(app.generate_content())

            MDBottomSheetDragHandle:

                MDBottomSheetDragHandleTitle:
                    text: "Select type map"
                    drag_handle_color: "grey"
                    adaptive_height: True
                    bold: True
                    pos_hint: {"center_y": .5}

                MDBottomSheetDragHandleButton:
                    drag_handle_color: "grey"
                    icon: "close"
                    _no_ripple_effect: True
                    on_release: bottom_sheet.dismiss()

            MDBottomSheetContent:
                id: content_container
                padding: 0, 0, 0, "16dp"

    MDScreen:
        name: "add_contact"
        id: "add_contact"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "Add contact"
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
                right_action_items: [["empty.png",]]
            MDBoxLayout:
                spacing: "20dp"
                padding: "20dp"
                orientation: "vertical"
                MDTextFieldPersian:
                    font_name: "tanha.ttf"
                    id: name_contact
                    hint_text: "User Name"
                MDRaisedButton:
                    text: 'Add Contact'
                    size_hint_x: 1
                    on_release: app.creat_contact_on_list_app()

    # MDScreen:
    #     name: "add_group"
    #     id: "add_group"
    #     MDBoxLayout:
    #         orientation: "vertical"
    #         MDTopAppBar:
    #             title: "Add group"
    #             left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
    #             right_action_items: [["empty.png",]]
    #         MDBoxLayout:
    #             spacing: "20dp"
    #             padding: "20dp"
    #             orientation: "vertical"
    #             MDTextFieldPersian:
    #                 font_name: "tanha.ttf"
    #                 id: name_group
    #                 hint_text: "group"
    #             MDRaisedButton:
    #                 text: 'Add Group'
    #                 size_hint_x: 1
    #                 on_release: app.creat_group_on_list_app()

    # MDScreen:
    #     name: "add_chanel"
    #     id: "add_chanel"
    #     MDBoxLayout:
    #         orientation: "vertical"
    #         MDTopAppBar:
    #             title: "Add chanel"
    #             left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
    #             right_action_items: [["empty.png",]]
    #         MDBoxLayout:
    #             spacing: "20dp"
    #             padding: "20dp"
    #             orientation: "vertical"
    #             MDTextFieldPersian:
    #                 font_name: "tanha.ttf"
    #                 id: name_chanel
    #                 hint_text: "name"
    #             MDRaisedButton:
    #                 text: 'Add Chanel'
    #                 size_hint_x: 1
    #                 on_release: app.creat_chanel_on_list_app()

    MDScreen:
        name: "tran_scr"
        id: "tran_scr"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "translate"
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
                right_action_items: [["cached", lambda x: app.chang_mode_translating()]]
            MDBoxLayout:
                orientation: "vertical"
                spacing: 10
                padding: 10
                MDLabel:
                    id: tran_lab
                    text: 'english to persian'
                    halign: 'center'
                    font_style: 'H5'
                MDSpinner:
                    id: rc_spin_tr
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': .5}
                    active: False
                MDTextFieldPersian:
                    id: input
                    hint_text: "  Enter text"
                    font_name: 'tanha.ttf'
                MDTextFieldPersian:
                    id: output
                    hint_text: "  Translation"
                    readonly: True
                    font_name: 'tanha.ttf'
                MDRaisedButton
                    text: "Translate"
                    size_hint_x: 1
                    on_release: app.translate()

    MDScreen:
        name: 'math_chat'
        id: 'math_chat'
        MDBoxLayout:
            orientation: "vertical"

            MDTopAppBar:
                title: "Chat"
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
                right_action_items: [["empty.png",]]

            MDScrollView:
                id: scroll_to_but
                scroll_timeout: 0
                MDList:
                    id: md_list_to_but
                    spacing: 10
                    padding: 10

            MDBoxLayout:
                padding: 10
                spacing: 10
                orientation: "horizontal"
                size_hint_y: None
                height: "48dp"
                MDTextFieldPersian:
                    font_name: "tanha.ttf"
                    id: message_to_bot
                    hint_text: " Chat"
                    multiline: True
                    max_text_length: 128
                MDFloatingActionButton:
                    id: send
                    icon: "send.png"
                    on_release: app.send_message_to_nira_math_bot()

    MDScreen:
        name: 'login_failed'
        id: 'login_failed'
        MDBoxLayout:
            spacing: 10
            padding: 10
            orientation: "vertical"
            MDBoxLayout:
                padding: 40
                FitImage:
                    source: "no_internet.png"
            MDRaisedButton:
                text: 'try again'
                size_hint_x: 1
                on_release: app.back_to_wel()

    MDScreen:
        name: 'show_image'
        id: show_png
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "Photo Viewer"
                left_action_items: [["chevron-left", lambda x: app.exit_from_file()]]
            FitImage:
                id: pic
    
    MDScreen:
        name: 'show_video'
        id: 'show_video'
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "Video Player"
                left_action_items: [["chevron-left", lambda x: app.exit_from_file()]]
            VideoPlayer:
                id: vid
                allow_stretch: True

    MDScreen:
        name: 'show_sound'
        id: 'show_sound'
        MDTopAppBar:
            title: "Music Player"
            left_action_items: [["chevron-left", lambda x: app.exit_from_file()]]
            right_action_items: [["play", lambda x: app.play_music(root)]]

    MDScreen:
        name: 'calculator'
        id: calculator
        MDBoxLayout:
            orientation: "vertical"

            MDTopAppBar:
                title: 'Calculator'
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
                right_action_items: [["content-copy", lambda x: app.copy_text()]]

            MDTextFieldPersian:
                font_name: "tanha.ttf"
                id: cal_field
                mode: 'fill'
                multiline: False
                readonly: True
                font_size: 30
                size_hint_y: None
                halign: 'left'

            MDBoxLayout:
                orientation: "vertical"
                MDBoxLayout:
                    spacing: 10
                    padding: 5
                    orientation: "horizontal"

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'lep.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('(')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'rip.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number(')')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'pi.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('π')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'ei.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('e')
                        
                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'cle.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('CE')

            MDBoxLayout:
                orientation: "vertical"
                MDBoxLayout:
                    spacing: 10
                    padding: 5
                    orientation: "horizontal"

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'rad.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('sqrt')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'pow.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('pow')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'fac.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('fact')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'cam.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number(',')
                        
                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'tcl.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('C')

            MDBoxLayout:
                orientation: "vertical"
                MDBoxLayout:
                    spacing: 10
                    padding: 5
                    orientation: "horizontal"

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'sin.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('sin')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'cos.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('cos')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'tan.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('tan')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'cot.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('cot')
                        
                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'log.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('log')

            MDBoxLayout:
                orientation: "vertical"
                MDBoxLayout:
                    spacing: 10
                    padding: 5
                    orientation: "horizontal"

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'sec.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('sec')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'csc.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('csc')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'cas.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('1/x')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'dar.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('%')
                        
                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'tagh.png'
                        #_no_ripple_effect: True
                        md_bg_color: app.theme_cls.primary_color
                        on_release: app.add_number('/')
            
            MDBoxLayout:
                orientation: "vertical"
                MDBoxLayout:
                    spacing: 10
                    padding: 5
                    orientation: "horizontal"

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'fac.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('factor')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: '7.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('7')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: '8.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('8')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: '9.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('9')
                        
                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'zar.png'
                        #_no_ripple_effect: True
                        md_bg_color: app.theme_cls.primary_color
                        on_release: app.add_number('*')

            MDBoxLayout:
                orientation: "vertical"
                MDBoxLayout:
                    spacing: 10
                    padding: 5
                    orientation: "horizontal"

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'kmm.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('lcm')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: '4.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('4')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: '5.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('5')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: '6.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('6')
                        
                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'men.png'
                        #_no_ripple_effect: True
                        md_bg_color: app.theme_cls.primary_color
                        on_release: app.add_number('-')

            MDBoxLayout:
                orientation: "vertical"
                MDBoxLayout:
                    spacing: 10
                    padding: 5
                    orientation: "horizontal"

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'bmm.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('gcd')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: '1.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('1')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: '2.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('2')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: '3.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('3')
                        
                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'gam.png'
                        #_no_ripple_effect: True
                        md_bg_color: app.theme_cls.primary_color
                        on_release: app.add_number('+')

            MDBoxLayout:
                orientation: "vertical"
                MDBoxLayout:
                    spacing: 10
                    padding: 5
                    orientation: "horizontal"

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'pri.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('prime')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'cha.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('+/-')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: '0.png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('0')

                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: '..png'
                        #_no_ripple_effect: True
                        on_release: app.add_number('.')
                        
                    MDIconButton:
                        size_hint_x: 1
                        size_hint_y: 1
                        icon: 'mos.png'
                        #_no_ripple_effect: True
                        md_bg_color: app.theme_cls.primary_color
                        on_release: app.add_number('=')

    MDScreen:
        name: 'xyz_mine'
        id: xyz_mine
        MDBoxLayout:
            padding: "10dp"
            orientation: "vertical"
            height: "48dp"
            FitImage:
                source: 'mine_sweeper_2.png'

            MDTextFieldPersian:
                font_name: "tanha.ttf"
                id: x
                hint_text: "X (please enter a number between 5 and 15)"
                size_hint_x: 1

            MDTextFieldPersian:
                font_name: "tanha.ttf"
                id: y
                hint_text: "Y (please enter a number between 5 and 15)"
                size_hint_x: 1

            MDTextFieldPersian:
                font_name: "tanha.ttf"
                id: z
                hint_text: "Mines (please enter a number between 20 and 100)"
                size_hint_x: 1
                
            MDRaisedButton:
                text: "Start"
                size_hint_x: 1
                on_release: app.go_to_mine_sweeper()

    MDScreen:
        name: 'help'
        id: help
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: 'Help'
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]

            MDScrollView:
                MDList:
                    padding: 20
                    spacing: 20
                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        TwoLineListItem:
                            text: "Abedi (if you have a graphical bug call me)"
                            secondary_text: "09369152046"
                            _no_ripple_effect: True
                            on_release: app.copy_help_number('09369152046')

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        TwoLineListItem:
                            text: "Vatani (if you have a network bug call me)"
                            secondary_text: "09044991280"
                            _no_ripple_effect: True
                            on_release: app.copy_help_number('09044991280')

                    MDCardSwipeFrontBox:
                        size_hint_y: None
                        TwoLineListItem:
                            text: "ZamaniNezhad (if you have a webapp bug call me)"
                            secondary_text: "09383781471"
                            _no_ripple_effect: True
                            on_release: app.copy_help_number('09383781471')

    MDScreen:
        name: 'VidHelp'
        id: VidHelp
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "Video Player"
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
            VideoPlayer:
                id: video
                source: "help.mp4"
                allow_stretch: True

    MDScreen:
        name: 'Wikipedia App'
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: 'Wikipedia App'
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
                right_action_items: [["magnify", lambda x: app.wiki_search()]]
            MDScrollView:
                MDBoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    padding: 10
                    spacing: 10
                    height: self.minimum_height

                    MDTextField:
                        id: your_query
                        hint_text: "Your Query"
                        color_mode: 'custom'
                        helper_text_mode: "on_focus"
                        size_hint_x: None
                        width: 300
                        pos_hint: {"center_x": .5}

                    MDTextField:
                        id: result
                        hint_text: "Result"
                        multiline: True
                        icon_right_color: app.theme_cls.primary_color
                        readonly: True
                        color_mode: 'custom'
                        helper_text_mode: "on_focus"
                        icon_right: 'wikipedia'
                        font_name: 'Tanha.ttf'

                    MDLabel:
                        pos_hint: {'center_y':0.85}
                        color:'#1675f7'

                    MDSpinner:
                        id: rc_spin_wiki
                        size_hint: None, None
                        size: dp(46), dp(46)
                        pos_hint: {'center_x': .5}
                        active: False

                    MDLabel:
                        pos_hint: {'center_y':0.85}
                        color:'#1675f7'

    MDScreen:
        name: 'internet_speed'
        id: internet_speed
        MDBoxLayout:
            orientation: 'vertical'
            MDTopAppBar:
                title: 'Internet Speed'
                left_action_items: [["chevron-left", lambda x: app.back_to_main_from_speed_cheker()]]
            MDBoxLayout:
                orientation: 'vertical'
                spacing: 10
                padding: 10
                MDLabel:
                    id: speed_label
                    text: 'speed : -'
                    halign: 'center'
                    font_style: 'H5'

                MDSpinner:
                    id: rc_spin
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': .5}
                    active: False

                MDLabel:
                    id: rc_spin_lab
                    text: '-'
                    font_style: 'H5'
                    halign: 'center'

                MDRaisedButton:
                    text: 'Test Speed'
                    pos_hint: {'center_x': 0.5}
                    size_hint_x: 1
                    size_hint_y: 1
                    on_release: app.test_speed()

    MDScreen:
        name: 'speed_toch_tester'
        id: speed_toch_tester
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                id: speed
                title: 'Touch Speed Cecker : -'
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
                right_action_items: [["refresh", lambda x: app.reset_counter_manually()]]
            MDBoxLayout:
                spacing: 10
                padding: 10
                orientation: "vertical"
                MDLabel:
                    id: counter
                    text: '0'
                    halign: 'center'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    size_hint_x: 1
                    size_hint_y: 1
                    font_style: 'H5'

                MDRaisedButton:
                    text: 'Click Me'
                    id: button
                    pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                    size_hint_x: 1
                    size_hint_y: 1
                    on_press: app.increment_counter()

    MDScreen:
        name: 'reaction_speed_test'
        id: reaction_speed_test
        MDBoxLayout:
            orientation: 'vertical'
            MDTopAppBar:
                title: 'Reaction Speed Test'
                left_action_items: [["chevron-left", lambda x: app.back_to_main()]]
                right_action_items: [["chevron-right", lambda x: app.change_color()]]
            MDBoxLayout:
                orientation: 'vertical'
                spacing: 10
                padding: 10
                MDLabel:
                    id: label
                    text: 'Click on the chevron right after ==> Click on the button when it turns green'
                    halign: 'center'
                    font_style: 'H5'

                MDRaisedButton:
                    id: reaction_button
                    text: 'Click Me'
                    size_hint_x: 1
                    size_hint_y: 1
                    md_bg_color: 1, 0, 0, 1
                    on_release: app.check_reaction()

    MDScreen:
        name: 'repetitious_acount'
        id: 'repetitious_acount'
        MDBoxLayout:
            spacing: 10
            padding: 10
            orientation: "vertical"
            MDBoxLayout:
                padding: 40
                FitImage:
                    source: "repetitious_acount_img.png"
            MDLabel:
                size_hint_y: None
                halign: 'center'
                text: 'The username you selected is duplicate'
            MDRaisedButton:
                text: 'try again'
                size_hint_x: 1
                on_release: app.back_to_wel()

    MDScreen:
        name: 'another_device'
        id: 'another_device'
        MDBoxLayout:
            spacing: 10
            padding: 10
            orientation: "vertical"
            MDBoxLayout:
                padding: 40
                FitImage:
                    source: "another_device_img.png"
            MDLabel:
                size_hint_y: None
                halign: 'center'
                text: 'This account is active on another device'
            MDRaisedButton:
                text: 'try again'
                size_hint_x: 1
                on_release: app.back_to_wel()

    MDScreen:
        name: 'false_password'
        id: 'false_password'
        MDBoxLayout:
            spacing: 10
            padding: 10
            orientation: "vertical"
            MDBoxLayout:
                padding: 40
                FitImage:
                    source: "false_password_img.png"
            MDLabel:
                size_hint_y: None
                halign: 'center'
                text: 'The password is incorrect'
            MDRaisedButton:
                text: 'try again'
                size_hint_x: 1
                on_release: app.back_to_wel()
'''

login = False
x = 10 
y = 5 
z = 5 
bem = 0
kem = 1
mode_translating = True
port_contact = '-'
mode_port = '-'
fg=dict()
websocket = ''
username = ''
pin = ''
port_contact = ''
user_contacts = []
all_data = {}
type_mes = ''
m_send = ''
last_my_massege = ''
selfroot = ''
selfsound = ''
idofsound = ''
selfmain = ''
message_number = 0
gself = ''
select_file_path = ''
selg = ''
scores = []
average_score = 0

def receive():
    global websocket
    global user_contacts
    global username
    global type_mes
    global m_send
    global fg
    global all_data
    global port_contact
    global last_my_massege
    nra = Nira()
    fg={}
    try:
        selfroot.ids.paiin.bg_color=[0,0,0,1]
    except:
        pass
    while True:
        message = websocket.recv()
        all_data=json.loads(message)
        mtype = all_data['type']
        if mtype == 'sent':
            if all_data ['data']['sender'] == username:
                user_contacts.append(all_data['data']['recipient'])
            else :
                user_contacts.append(all_data['data']['sender'])
            nra.refresh_contacts()
            if port_contact ==  all_data ['data']['sender']:
                type_mes = 'sender'
                m_send = all_data ['data']['message']
                fg[f"{m_send}////{all_data['id']}"]='sender'
                nra.recieve_message()
            if port_contact ==  all_data ['data']['recipient']:
                m_send = all_data ['data']['message']
                type_mes = 'recipient'
                fg[f"{m_send}////{all_data['id']}"]='recipient'
                nra.recieve_message()
        if mtype == 'contacts':
            user_contacts = all_data['contacts'].split(',')
            nra.refresh_contacts()
        if mtype == 'del':
            keys = list(fg)
            for massege in keys:
                if all_data['id'] in massege:
                    del fg[massege]
            websocket.send(json.dumps({'type':'want_user_masseges','user':port_contact}))
            nra.recieve_message() 
        if mtype == 'vir':  
            keys = list(fg)
            vals = list(fg.values())
            for i in range(len(keys)):
                if all_data['id'] in keys[i]:
                    data=dict(all_data)
                    keys[i]=data['data'] + '////' + all_data['id']
            fg={}
            for i in range(len(keys)):
                fg[keys[i]]=vals[i]
            
            nra.recieve_message()
        if mtype == 'get_id':

            fg[(all_data['message'])+'////'+all_data['id']]='recipient'
            nra.recieve_message()


class TypeMapElement(MDBoxLayout):
    selected = BooleanProperty(False)
    icon = StringProperty()
    title = StringProperty()

class PinTextField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class MDTextFieldPersian(MDTextField):
    max_chars = NumericProperty(100) 
    str = StringProperty()

    def __init__(self, **kwargs):
        super(MDTextFieldPersian, self).__init__(**kwargs)
        self.text = get_display(arabic_reshaper.reshape(""))

    def insert_text(self, substring, from_undo=False):
        global gself
        global bem
        if bem==0:
            self.str=substring
            self.text = get_display(arabic_reshaper.reshape(substring))
            if bem==len(self.text) + len(substring):
                self.str = self.str+substring
                self.text = get_display(arabic_reshaper.reshape(self.str))
            else:
                self.str = substring
                bem = 1
                self.text = get_display(arabic_reshaper.reshape(self.str))
            substring = ""
            super(MDTextFieldPersian, self).insert_text(substring, from_undo)
        else:
            bem+=1
            self.text = get_display(arabic_reshaper.reshape(self.str))
            self.str = self.str+substring
            self.text = get_display(arabic_reshaper.reshape(self.str))
            substring = ""
            super(MDTextFieldPersian, self).insert_text(substring, from_undo)
            if not from_undo and (len(self.text) + len(substring) > self.max_chars):
                return
            self.str = self.str+substring
            self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(MDTextFieldPersian, self).insert_text(substring, from_undo)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = get_display(arabic_reshaper.reshape(self.str))
    

class CustomMapView(MapView, TouchBehavior):
    bottom_sheet = ObjectProperty()

    def on_double_tap(self, touch, *args):
        if self.bottom_sheet:
            self.bottom_sheet.open()

class TopAppBar(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = 0.125
        self.height = 50

class MinesweeperCell(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_mine = False
        self.is_revealed = False
        self.adjacent_mines = 0
        self.border_radius = [675]

class MinesweeperGrid(GridLayout):
    def __init__(self, rows, cols, mines, **kwargs):
        super().__init__(**kwargs)
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.cells = {}
        self.create_grid()
        self.place_mines()
        self.calculate_adjacent_mines()

    def create_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = MinesweeperCell()
                self.cells[(row, col)] = cell
                self.add_widget(cell)
                cell.bind(on_release=self.cell_released)

    def place_mines(self):
        global selg
        selg = self
        placed_mines = 0
        while placed_mines < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            cell = self.cells[(row, col)]
            if not cell.is_mine:
                cell.is_mine = True
                placed_mines += 1

    def calculate_adjacent_mines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[(row, col)]
                if cell.is_mine:
                    continue
                adjacent_cells = self.get_adjacent_cells(row, col)
                cell.adjacent_mines = sum(1 for c in adjacent_cells if c.is_mine)

    def get_adjacent_cells(self, row, col):
        adjacent_cells = []
        for r in range(max(0, row - 1), min(self.rows, row + 2)):
            for c in range(max(0, col - 1), min(self.cols, col + 2)):
                if (r, c) != (row, col):
                    adjacent_cells.append(self.cells[(r, c)])
        return adjacent_cells

    def cell_released(self, instance):
        if instance.is_mine:
            self.reveal_all_mines()
            self.show_game_over()
        else:
            self.reveal_cell(instance)
            if self.check_win_condition():
                self.show_victory()

    def reveal_all_mines(self):
        for cell in self.cells.values():
            if cell.is_mine:
                cell.text = 'M'

    def reveal_cell(self, cell):
        if cell.is_revealed:
            return
        cell.is_revealed = True
        cell.text = str(cell.adjacent_mines) if cell.adjacent_mines > 0 else ''
        if cell.adjacent_mines == 0:
            for adjacent_cell in self.get_adjacent_cells(*self.get_cell_position(cell)):
                self.reveal_cell(adjacent_cell)

    def get_cell_position(self, cell):
        for position, c in self.cells.items():
            if c == cell:
                return position

    def check_win_condition(self):
        return all(cell.is_revealed or cell.is_mine for cell in self.cells.values())

    def show_game_over(self):
        view = ModalView(size_hint=(0.75, 0.5))
        view.add_widget(MDLabel(text='Game Over!'))
        view.bind(on_dismiss=self.restart_game)
        view.open()

    def show_victory(self):
        view = ModalView(size_hint=(0.75, 0.5))
        view.add_widget(MDLabel(text='Victory!'))
        view.bind(on_dismiss=self.restart_game)
        view.open()

    def restart_game(self, *args):
        self.clear_widgets()
        self.cells = {}
        self.create_grid()
        self.place_mines()
        self.calculate_adjacent_mines()

class MinesweeperApp(App):
    def build(self):
        layout = MDBoxLayout(orientation='vertical')
        layout.add_widget(TopAppBar())
        layout.add_widget(MinesweeperGrid(rows=x, cols=y, mines=z))
        return layout
    
class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()

class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()

class YCToDeleteItem(MDCardSwipe):
    text = StringProperty()

class FileToDeleteItem(FitImage):
    text = StringProperty()

class ContactListItem(MDCardSwipe):
    text = StringProperty()

# class GroupListItem(CardSwipe):
#     text = StringProperty()

# class ChanelListItem(CardSwipe):
    # text = StringProperty()

class Nira(MDApp):

    data = DictProperty()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        # self.theme_cls.theme_style_switch_animation = True
        # self.theme_cls.theme_style_switch_animation_duration = 0.5
        self.icon = "icon.png"
        menu_items = [
            {"text": f"Item {i}",
                "left_icon": "edit.png",
                "viewclass": "Item",
                "height": dp(54),
            } for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )

        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )
        return Builder.load_string(KV)

    def login(self):
        try:
            global loop
            global username
            global pin
            global websocket
            global selfmain
            websocket=connect("ws://localhost:6789", max_size=565656655545)
            self.theme_cls.theme_style = "Dark"
            pin = self.root.ids.password_login.text
            username = self.root.ids.user_name_login.text
            print(username)
            print(pin)
            websocket.send(username+'////'+pin)
            message=websocket.recv()
            if message == "ورود موفقیت‌آمیز":
                self.root.current = "main"
                selfmain=self.root
                receive_thread = threading.Thread(target=receive)
                receive_thread.start()
            elif message == "این نام کاربری وارد شده است.":
                self.root.current = "another_device"
            elif message == "رمز عبور اشتباه است.":
                self.root.current = "false_password"

        except:
            self.root.current = "login_failed"

    def creat(self):
        try:
            global loop
            global username
            global pin
            global websocket
            global selfmain
            websocket=connect("ws://localhost:6789", max_size=565656655545)
            self.theme_cls.theme_style = "Dark"
            pin = self.root.ids.password_creat.text
            username = self.root.ids.user_name_creat.text
            websocket.send(username+'////'+pin)
            message=websocket.recv()
            if message == "ورود موفقیت‌آمیز":
                self.root.current = "main"
                selfmain=self.root
                receive_thread = threading.Thread(target=receive)
                receive_thread.start()
            elif message == "این نام کاربری وارد شده است.":
                self.root.current = "repetitious_acount"
            elif message == "رمز عبور اشتباه است.":
                self.root.current = "repetitious_acount"
            
        except:
            self.root.current = "login_failed"

    @mainthread
    def refresh_contacts(self):
        global user_contacts
        global selfmain
        self.theme_cls.theme_style = "Dark"
        is_added = []
        selfmain.ids.contacts_list.clear_widgets()
        for i in user_contacts:
            if i not in is_added:
                is_added.append(i)
                text = i
                if text:
                    new_message = ContactListItem(text=text)
                    new_list = MDList(id=text)
                    selfmain.ids.contacts_list.add_widget(new_message)
                    selfmain.ids.scroll.scroll_to(new_message)

    def go_to_nira(self, mode):
        global login
        global selfmain
        print(mode)
        self.theme_cls.theme_style = "Dark"
        if mode == 'creat_account':
            login = True
            self.root.current = "main_creat_account"
        elif mode == 'login':
            self.root.current = "main_login"

    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def change_send_mode(self):
        global text_mes
        text_mes = 'recipient'

    @mainthread
    def recieve_message(self):
        try:
            global m_send
            global type_mes
            global fg
            global selfroot
            global all_data
            selfroot.ids.md_list.clear_widgets()
            for massege in list(fg):
                if massege != "":
                    if 'f8etnworjboifhoidjc2rpg;;rejgoihtrg78yihv984etgr97yhgirhvefnvbuio4rgui4rg9fjhmrji0cgfbrn3oiuf,riugbrhvfmiyufihvokeqrpkgophbuifnpoiewrjbuihebprofbhref9w0g925t7ur89iguj58tyh7iuG^%#WQG32o4vgyi3rgr.' in massege:
                        massege=massege.split('////')[0]
                        name_file = massege.split('f8etnworjboifhoidjc2rpg;;rejgoihtrg78yihv984etgr97yhgirhvefnvbuio4rgui4rg9fjhmrji0cgfbrn3oiuf,riugbrhvfmiyufihvokeqrpkgophbuifnpoiewrjbuihebprofbhref9w0g925t7ur89iguj58tyh7iuG^%#WQG32o4vgyi3rgr.')[1]
                        binary = massege.split('f8etnworjboifhoidjc2rpg;;rejgoihtrg78yihv984etgr97yhgirhvefnvbuio4rgui4rg9fjhmrji0cgfbrn3oiuf,riugbrhvfmiyufihvokeqrpkgophbuifnpoiewrjbuihebprofbhref9w0g925t7ur89iguj58tyh7iuG^%#WQG32o4vgyi3rgr.')[0]
                        imgstring = binary[2:-1]

                        sentences = name_file.split('.')
                        last_sentence = sentences[-1].strip()
                        imgdata = base64.b64encode(imgstring.encode('utf-8'))
                        print(imgdata,5)
                        filename = f'{name_file.split(".")[0]}.{last_sentence}'
                        with open(filename, 'wb') as f:
                            f.write(imgdata)

                        text = name_file

                        if text:
                            new_message = FileToDeleteItem(text=name_file)
                            selfroot.ids.md_list.add_widget(new_message)
                            selfroot.ids.scroll.scroll_to(new_message)
                            selfroot.ids.message.text = ""
                    else:
                        reshaped_text = arabic_reshaper.reshape(massege.split('////')[0])
                        bidi_text = get_display(reshaped_text)
                        if fg[massege]=='sender':
                            if selfroot!="":
                                new_message = YCToDeleteItem(text=massege.split('////')[0])
                                selfroot.ids.md_list.add_widget(new_message)
                                selfroot.ids.scroll.scroll_to(new_message)
                        elif fg[massege]=="recipient":
                            if selfroot!="":
                                new_message = SwipeToDeleteItem(text=massege.split('////')[0])
                                selfroot.ids.md_list.add_widget(new_message)
                                selfroot.ids.scroll.scroll_to(new_message)
        except:
            pass

    def send_message(self):
        try:
            global m_send
            global last_my_massege
            global type_mes
            global fg
            global websocket
            global port_contact
            global gself
            global bem
            global all_data
            text = self.root.ids.message.text
            if text:
                now = datetime.datetime.now()
                persian_now = jdatetime.datetime.fromgregorian(datetime=now)
                persian_now2 = persian_now.strftime("%Y/%m/%d")
                time = persian_now.strftime("%H:%M:%S")
                reshaped_text = arabic_reshaper.reshape(text)
                bidi_text = get_display(reshaped_text)
                websocket.send(json.dumps({'type':'send','data':{'message':text,'recipient': port_contact},'date':persian_now2,'time':time}))
                new_message = SwipeToDeleteItem(text=text)
                last_my_massege = text
                self.root.ids.md_list.add_widget(new_message)
                self.root.ids.scroll.scroll_to(new_message)
                self.root.ids.message.text = ""
                bem=0

        except:
            pass    

    def show_dialogpanel_for_message(self, instance):
        self.dialog = MDDialog(
            title="Edit item",
            type="custom",
            content_cls=MDTextFieldPersian(text=instance.text, multiline='true', max_text_length=100,  font_name= "Tanha.ttf"),
            buttons=[
                MDRaisedButton(text="DELETE", on_release=lambda x: self.remove_item(instance)),
                MDRaisedButton(text="CANCEL", on_release=self.close_dialog),
                MDRaisedButton(text="OK", on_release=lambda x: self.update_item(instance))
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def update_item(self, instance):
        global fg
        global message_number
        global websocket
        global bem
        global port_contact
        n = 0
        id = ''
        for message in fg:
            if n == message_number-1:
                id = message.split('////')[1]
                keys = list(fg)
                vals = list(fg.values())
                for i in range(len(keys)):
                    if id in keys[i]:
                        keys[i] = self.dialog.content_cls.text + '////' + id
                fg={}
                for i in range(len(keys)):
                    fg[keys[i]]=vals[i]     
            n+=1
        instance.text = self.dialog.content_cls.text
        bem=0
        websocket.send(json.dumps({'type':'vir','data':{'newm':self.dialog.content_cls.text,'recipient':port_contact},'id':id}))
        self.close_dialog()

    def remove_item(self, instance):
        global fg
        global message_number
        global websocket
        global port_contact
        n = 0
        id = ''
        keys = list(fg)
        for massege in keys:
            if n == message_number-1:
                id = massege.split('////')[1]
                del fg[massege]
            n+=1
        n = 0
        websocket.send(json.dumps({'type':'del','data':{'recipient': port_contact},'id':id}))
        self.root.ids.md_list.remove_widget(instance)
        self.dialog.dismiss()
        self.root.current = "chat"
    def remove_file(self, instance):
        self.root.ids.md_list.remove_widget(
            instance
        )

    def show_example_grid_bottom_sheet(self):
        self.root.current = "file"

    def home_chat(self):
        self.root.current = "chat"

    def start_game(self):
        self.root.current = "xyz_mine"
        
    def creat_contact(self):
        self.root.current = "creat_contact"

    def creat_contact_on_list_app(self):
        global bem
        global user_contacts
        text = self.root.ids.name_contact.text
        if text:
            new_message = ContactListItem(text=text)
            new_list = MDList(id=text)
            user_contacts.append(text)
            self.root.ids.contacts_list.add_widget(new_message)
            self.root.ids.scroll.scroll_to(new_message)
            self.root.ids.name_contact.text = ""
            bem=0
            self.root.current = "main"

    # def creat_group_on_list_app(self):
    #     text = self.root.ids.name_group.text
    #     if text:
    #         new_message = GroupListItem(text=text)
    #         new_list = List(id=text)
    #         self.root.ids.contacts_list.add_widget(new_message)
    #         self.root.ids.scroll.scroll_to(new_message)
    #         self.root.ids.name_group.text = ""
    #         self.root.current = "main"

    # def creat_chanel_on_list_app(self):
    #     text = self.root.ids.name_chanel.text
    #     if text:
    #         new_message = ChanelListItem(text=text)
    #         new_list = List(id=text)
    #         self.root.ids.contacts_list.add_widget(new_message)
    #         self.root.ids.scroll.scroll_to(new_message)
    #         self.root.ids.name_chanel.text = ""
    #         self.root.current = "main"

    def creat_contact_on_list(self):
        self.root.current = "add_contact"
    
    # def creat_group_on_list(self):
    #     self.root.current = "add_group"
    
    # def creat_chanel_on_list(self):
    #     self.root.current = "add_chanel"
    
    def go_to_messages_for_this_people(self, instance):
        global port_contact
        global selfroot
        global websocket
        global fg
        self.root.ids.paiin.md_bg_color=[0,0,0,1]
        fg={}
        self.root.ids.md_list.clear_widgets()
        self.root.current = "chat"
        selfroot=self.root
        text = instance.text
        port_contact=f'{text}'
        self.root.ids.chat_app_bar.title = port_contact
        back = f'backgrand_on_contact.png'
        self.root.ids.backgrand.source = back
        websocket.send(json.dumps({'type':'want_user_masseges','user':port_contact}))
        Clock.schedule_once(self.set_toolbar_font_name)

    def set_toolbar_font_name(self, *args):
        self.root.ids.chat_app_bar.ids.label_title.font_name = "Tanha.ttf"

    def back_to_main(self):
        global selfsound
        global idofsound
        global fg
        fg={}
        if idofsound:
            idofsound=False
            selfsound.stop()
        self.root.current = "main"
        port_contact='-'
        self.root.ids.md_list.clear_widgets()

    def start_calculator(self):
        self.root.current = "calculator"

    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def select_path(self, path: str):
        global all_data
        global websocket
        global port_contact
        global last_my_massege
        global selfroot
        fpath = path

        self.exit_manager()
        # try:
        MDSnackbar(
            MDLabel(
                text= path,
                theme_text_color="Custom",
                text_color="#393231",
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
            md_bg_color="#E8D8D7",
        ).open()
        with open(path, 'rb') as input_file:
            binary_data = input_file.read()
            base64_data = base64.b64encode(binary_data)
            a = base64_data
        input_text = path
        sentences = input_text.split('\'')
        name_file = sentences[-1].strip()
        print(a,9)
        a = str(a)
        # print(a)
        # a = ''.join(chr(int(a[i*8:i*8+8], 2)) for i in range(len(a)//8))
        last_my_massege = a + 'f8etnworjboifhoidjc2rpg;;rejgoihtrg78yihv984etgr97yhgirhvefnvbuio4rgui4rg9fjhmrji0cgfbrn3oiuf,riugbrhvfmiyufihvokeqrpkgophbuifnpoiewrjbuihebprofbhref9w0g925t7ur89iguj58tyh7iuG^%#WQG32o4vgyi3rgr.'+name_file
        now = datetime.datetime.now()
        persian_now = jdatetime.datetime.fromgregorian(datetime=now)
        persian_now2 = persian_now.strftime("%Y/%m/%d")
        time = persian_now.strftime("%H:%M:%S")
        websocket.send(json.dumps({'type':'send','data':{'recipient':port_contact,'message':a +'f8etnworjboifhoidjc2rpg;;rejgoihtrg78yihv984etgr97yhgirhvefnvbuio4rgui4rg9fjhmrji0cgfbrn3oiuf,riugbrhvfmiyufihvokeqrpkgophbuifnpoiewrjbuihebprofbhref9w0g925t7ur89iguj58tyh7iuG^%#WQG32o4vgyi3rgr.'+name_file},'date':persian_now2,'time':time}))
        new_message = FileToDeleteItem(text=fpath)
        selfroot.ids.md_list.add_widget(new_message)
        selfroot.ids.scroll.scroll_to(new_message)
        selfroot.ids.message.text = ""
        # except:
        #     pass

    def show_file(self, instance):
        input_text = instance.text
        sentences = input_text.split('.')
        last_sentence = sentences[-1].strip()
        if last_sentence == 'png':
            self.root.current = "show_image"
            self.root.ids.pic.source = input_text
        if last_sentence == 'mp4':
            self.root.current = "show_video"
            self.root.ids.vid.source = input_text
        if last_sentence == 'mp3':
            self.root.current = "show_sound"
            global selfsound
            selfsound = input_text

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def chang_color_them(self):
        self.root.current = "chang_color_them"

    def on_click_red(self, *args):
        self.theme_cls.primary_palette =   "Red"

    def on_click_pink(self, *args):
        self.theme_cls.primary_palette =   "Pink"

    def on_click_purple(self, *args):
        self.theme_cls.primary_palette =   "Purple"

    def on_click_deep_purple(self, *args):
        self.theme_cls.primary_palette =   "DeepPurple"   

    def on_click_indigo(self, *args):
        self.theme_cls.primary_palette =   "Indigo"   

    def on_click_blue(self, *args):
        self.theme_cls.primary_palette =   "Blue"   

    def on_click_light_blue(self, *args):
        self.theme_cls.primary_palette =   "LightBlue"   

    def on_click_cyan(self, *args):
        self.theme_cls.primary_palette =   "Cyan"   

    def on_click_teal(self, *args):
        self.theme_cls.primary_palette =   "Teal"   

    def on_click_green(self, *args):
        self.theme_cls.primary_palette =   "Green"   

    def on_click_light_green(self, *args):
        self.theme_cls.primary_palette =   "LightGreen"   

    def on_click_lime(self, *args):
        self.theme_cls.primary_palette =   "Lime"   

    def on_click_yellow(self, *args):
        self.theme_cls.primary_palette =   "Yellow"   

    def on_click_amber(self, *args):
        self.theme_cls.primary_palette =   "Amber"   

    def on_click_orange(self, *args):
        self.theme_cls.primary_palette =   "Orange"   

    def on_click_deep_orange(self, *args):
        self.theme_cls.primary_palette =   "DeepOrange"   

    def on_click_brown(self, *args):
        self.theme_cls.primary_palette =   "Brown"  

    def on_click_gray(self, *args):
        self.theme_cls.primary_palette =   "Gray"   

    def on_click_blue_gray(self, *args):
        self.theme_cls.primary_palette = "BlueGray"
        
    map_sources = {
        "street": "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
        "sputnik": "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
        "hybrid": "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    }
    current_map = StringProperty("street")

    async def generate_content(self):
        icons = {
            "street": "google-street-view",
            "sputnik": "space-station",
            "hybrid": "map-legend",
        }
        if not self.root.ids.content_container.children:
            for i, title in enumerate(self.map_sources.keys()):
                await asynckivy.sleep(0)
                self.root.ids.content_container.add_widget(
                    TypeMapElement(
                        title=title.capitalize(),
                        icon=icons[title],
                        selected=not i,
                    )
                )

    def set_active_element(self, instance, type_map):
        for element in self.root.ids.content_container.children:
            if instance == element:
                element.selected = True
                self.current_map = type_map
            else:
                element.selected = False

    def start_maps(self):
        self.root.current = "maps"

    def start_translating(self):
        self.root.current = "tran_scr"

    def chang_mode_translating(self):
        global mode_translating
        if mode_translating == True:
            mode_translating = False
            self.root.ids.tran_lab.text = 'persian to english'
        elif mode_translating == False:
            mode_translating = True
            self.root.ids.tran_lab.text = 'english to persian'
        text1 = self.root.ids.input.text
        text2 = self.root.ids.output.text
        self.root.ids.input.text = text2
        self.root.ids.output.text = text1

    def translate(self):
        global selfroot
        try:
            global mode_translating
            from translators import translate_text
            import translators as ts
            text = self.root.ids.input.text
            text = text[::-1]
            if mode_translating == False:
                translation = translate_text(text, from_language="fa", to_language="en")
            elif mode_translating == True:
                translation = translate_text(text, from_language="en", to_language="fa")
            translation = get_display(arabic_reshaper.reshape(translation))
            self.root.ids.output.text = translation
        except:
            self.root.ids.output.text = 'No Internet Conection'
        
    def start_math_chat(self):
        self.root.current = "math_chat"

    def send_message_to_nira_math_bot(self):
        try:
            import wolframalpha
            text = self.root.ids.message_to_bot.text
            if text:
                new_question = YCToDeleteItem(text=text)
                self.root.ids.md_list_to_but.add_widget(new_question)
                self.root.ids.scroll_to_but.scroll_to(new_question)
                self.root.ids.message_to_bot.text = ""
            question = text
            app_id = 'YW444T-XQVYT54843'
            client = wolframalpha.Client(app_id) 
            res = client.query(question) 
            answer = next(res.results).text 
            answer = answer[0:125]
            if answer:
                new_answer = YCToDeleteItem(text=answer)
                self.root.ids.md_list_to_but.add_widget(new_answer)
                self.root.ids.scroll_to_but.scroll_to(new_answer)
                self.root.ids.message_to_bot.text = ""
        except:
            pass

    def failed(self):
        self.root.current = "login_failed"

    def play_music(self, instance):
        global selfsound
        global idofsound
        self.sound = SoundLoader.load(selfsound)
        self.sound.volume = 0.5
        selfsound=self.sound
        idofsound=True
        if self.sound.state == "play":
            self.sound.stop()
        else:
            self.sound.play()

    def exit_from_file(self):
        self.root.current = "chat"

    def add_number(self, number):
        value = number
        if value == 'C':
            self.root.ids.cal_field.text = ''

        elif value == 'CE':
            if self.root.ids.cal_field.text == 'Error':
                self.root.ids.cal_field.text = ''
            else:
                try:
                    self.root.ids.cal_field.text = self.root.ids.cal_field.text[0:len(self.root.ids.cal_field.text)-1]   
                except:
                    pass

        elif value == '+/-':
            if self.root.ids.cal_field.text:
                self.root.ids.cal_field.text = str(-float(self.root.ids.cal_field.text))

        elif value == '%':
            if self.root.ids.cal_field.text:
                try:
                    self.root.ids.cal_field.text = str(float(self.root.ids.cal_field.text) / 100)
                except:
                    self.root.ids.cal_field.text = 'Error'

        elif value == '1/x':
            if self.root.ids.cal_field.text:
                try:
                    self.root.ids.cal_field.text = str(1 / float(self.root.ids.cal_field.text))
                except ZeroDivisionError:
                    self.root.ids.cal_field.text = 'Error'

        elif value == '=':
            if self.root.ids.cal_field.text:
                try:
                    answer = str(eval(self.root.ids.cal_field.text))
                except Exception as e:
                    answer = 'Error'
                self.root.ids.cal_field.text = answer

        elif value == 'gcd':
            numbers = self.root.ids.cal_field.text.split(',')
            if len(numbers) == 2:
                try:
                    self.root.ids.cal_field.text = str(math.gcd(int(numbers[0]), int(numbers[1])))
                except ValueError:
                    self.root.ids.cal_field.text = 'Error'
        
        elif value == ',':
            self.root.ids.cal_field.text += value

        elif value == 'lcm':
            numbers = self.root.ids.cal_field.text.split(',')
            if len(numbers) == 2:
                try:
                    num1, num2 = int(numbers[0]), int(numbers[1])
                    self.root.ids.cal_field.text = str(math.lcm(num1, num2))
                except ValueError:
                    self.root.ids.cal_field.text = 'Error'

        elif value == 'prime':
            try:
                number = int(self.root.ids.cal_field.text)
                if number > 1:
                    for i in range(2, int(math.sqrt(number)) + 1):
                        if (number % i) == 0:
                            self.root.ids.cal_field.text = 'Not Prime'
                            break
                    else:
                        self.root.ids.cal_field.text = 'Prime'
                else:
                    self.root.ids.cal_field.text = 'Not Prime'
            except ValueError:
                self.root.ids.cal_field.text = 'Error'

        elif value == 'factor':
            try:
                number = int(self.root.ids.cal_field.text)
                factors = self.prime_factors(number)
                self.root.ids.cal_field.text = '*'.join(str(factor) for factor in factors)
            except ValueError:
                self.root.ids.cal_field.text = 'Error'

        elif value == 'sqrt':
            try:
                self.root.ids.cal_field.text = str(math.sqrt(float(self.root.ids.cal_field.text)))
            except ValueError:
                self.root.ids.cal_field.text = 'Error'

        elif value == 'pow':
            self.root.ids.cal_field.text += '**'

        elif value == 'fact':
            try:
                self.root.ids.cal_field.text = str(math.factorial(int(self.root.ids.cal_field.text)))
            except ValueError:
                self.root.ids.cal_field.text = 'Error'

        elif value == 'sec':
            try:
                self.root.ids.cal_field.text = str(1/math.cos(float(self.root.ids.cal_field.text)))
            except ValueError:
                self.root.ids.cal_field.text = 'Error'

        elif value == 'csc':
            try:
                self.root.ids.cal_field.text = str(1/math.sin(float(self.root.ids.cal_field.text)))
            except ValueError:
                self.root.ids.cal_field.text = 'Error'

        elif value == 'sin':
            try:
                self.root.ids.cal_field.text = str(math.sin(float(self.root.ids.cal_field.text)))
            except ValueError:
                self.root.ids.cal_field.text = 'Error'

        elif value == 'cos':
            try:
                self.root.ids.cal_field.text = str(math.cos(float(self.root.ids.cal_field.text)))
            except ValueError:
                self.root.ids.cal_field.text = 'Error'

        elif value == 'tan':
            try:
                self.root.ids.cal_field.text = str(math.tan(float(self.root.ids.cal_field.text)))
            except ValueError:
                self.root.ids.cal_field.text = 'Error'

        elif value == 'cot':
            try:
                self.root.ids.cal_field.text = str(1/math.tan(float(self.root.ids.cal_field.text)))
            except ValueError:
                self.root.ids.cal_field.text = 'Error'

        elif value == 'log':
            try:
                self.root.ids.cal_field.text = str(math.log(float(self.root.ids.cal_field.text)))
            except ValueError:
                self.root.ids.cal_field.text = 'Error'

        elif value == 'π':
            if self.root.ids.cal_field.text != '':
                try:
                    self.root.ids.cal_field.text += str(3.1415926535897932384626433832795)
                except:
                    self.root.ids.cal_field.text = 'Error'
            else:
                self.root.ids.cal_field.text = '3.1415926535897932384626433832795'

        elif value == 'e':
            if self.root.ids.cal_field.text != '':
                try:
                    self.root.ids.cal_field.text += str(2.7182818284590452353602874713527)
                except:
                    self.root.ids.cal_field.text = 'Error'
            else:
                self.root.ids.cal_field.text = '2.7182818284590452353602874713527'

        else:
            self.root.ids.cal_field.text += value

    def prime_factors(self, n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    def evaluate(self, expression):
        try:
            self.root.ids.cal_field.text = str(eval(expression))
        except Exception:
            self.root.ids.cal_field.text = 'Error'

    def copy_text(self):
        Clipboard.copy(self.root.ids.cal_field.text)
        MDSnackbar(
            MDLabel(
                text="Copyed to clipboard",
            ),
            pos=((10), (10)),
            size_hint_x=0.98,
        ).open()

    def on_item_release(self, list_item):
        global message_number
        index = self.root.ids.md_list.children.index(list_item)
        message_number = len(self.root.ids.md_list.children) - index

    def go_to_mine_sweeper(self):
        try:
            global x
            global y
            global z
            x = int(self.root.ids.x.text)
            y = int(self.root.ids.y.text)
            z = int(self.root.ids.z.text)
        except:
            pass
        Nira().stop()
        self.root.current = "empty_for_game"
        MinesweeperApp().run()

    def get_help (self):
        self.root.current = "help"
        
    def copy_help_number(self, phone_number):
        Clipboard.copy(phone_number)
        MDSnackbar(
            MDLabel(
                text="Copyed to clipboard",
            ),
            pos=((10), (10)),
            size_hint_x=0.98,
        ).open()

    def go_to_guide(self):
        self.root.current = "VidHelp"

    def back_to_main_from_game(self):
        global selg
        selg.clear_widgets()
        self.root.current = "main"

    def wiki_search(self):
        self.root.ids.rc_spin_wiki.active = True
        threading.Thread(target=self.perform_search).start()

    def perform_search(self):
        query = self.root.ids.your_query.text
        translator = Translator()
        try:
            result = wikipedia.summary(query, sentences=6)
            # ترجمه به فارسی
            result = translator.translate(result, dest='fa').text
            # ریشیپ کردن و راست‌چین کردن متن
            reshaped_text = reshape(result)
            bidi_text = get_display(reshaped_text)
            result = bidi_text.strip()
        except Exception as e:
            result = str(e)
        def update_result(dt):
            self.root.ids.result.text = result
            self.root.ids.rc_spin_wiki.active = False
        Clock.schedule_once(update_result, 0)

    def start_nira_wiki(self):
        self.root.current = 'Wikipedia App'

    def start_nira_internet_speed(self):
        self.root.current = 'internet_speed'

    def display_speed(self, dt):
        download_speed = self.st.results.download / 1_000_000
        upload_speed = self.st.results.upload / 1_000_000
        self.root.ids.speed_label.text = f'Download: {download_speed:.2f} Mbps \n Upload: {upload_speed:.2f} Mbps'
        self.root.ids.rc_spin.active = False
        self.root.ids.rc_spin_lab.text = '-'

    def test_speed(self):
        self.root.ids.rc_spin.active = True
        self.root.ids.rc_spin_lab.text = 'Cheking'
        threading.Thread(target=self.starting_test_speed).start()

    def starting_test_speed(self):
        try:
            self.st = speedtest.Speedtest()
            self.st.download()
            self.st.upload()
            Clock.schedule_once(self.display_speed, 10)
        except:
            self.root.ids.speed_label.text = f'No Internet Conection'

    def back_to_main_from_speed_cheker(self):
        self.root.ids.rc_spin.active = False
        self.root.ids.speed_label.text = f'Speed: -'
        self.root.ids.rc_spin_lab.text = '-'
        self.root.current = "main"

    def start_nira_touch_speed(self):
        self.root.current = "speed_toch_tester"
        Clock.schedule_once(self.reset_counter, 10)

    def increment_counter(self):
        current_count = int(self.root.ids.counter.text)
        self.root.ids.counter.text = str(current_count + 1)

    def reset_counter(self, dt):
        final_count = self.root.ids.counter.text
        self.root.ids.speed.title = f'Toch Speed Cecker : {final_count}'
        self.root.ids.button.disabled = True
        self.root.ids.counter.text = '0'

    def reset_counter_manually(self):
        self.root.ids.counter.text = '0'
        self.root.ids.button.disabled = False
        self.root.ids.speed.title = 'Toch Speed Checker : -'
        Clock.schedule_once(self.reset_counter, 10)

    def start_reaction_speed_test(self):
        self.root.current = "reaction_speed_test"

    def change_color(self):
        time.sleep(random.randint(1, 5))
        self.start_time = time.time()
        self.root.ids.reaction_button.md_bg_color = (0, 1, 0, 1)

    def check_reaction(self):
        try:
            if self.root.ids.reaction_button.md_bg_color == (1, 0, 0, 1):
                self.root.ids.label.text = 'The button was not blue yet!'
            else:
                reaction_time = time.time() - self.start_time
                scores.append(reaction_time)
                average_score = sum(scores) / len(scores) if scores else 0 
                self.root.ids.label.text = f'Your reaction time was: {reaction_time:.4f} seconds \n Average your scores: {average_score:.4f}'
                self.root.ids.reaction_button.md_bg_color = (1, 0, 0, 1)
        except:
            self.root.ids.label.text = 'Error'

    def back_to_wel(self):
        self.root.current = "welcom_screen"

Nira().run()