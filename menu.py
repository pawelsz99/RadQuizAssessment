# -------------------------------------------------------------------------------
# Name:        menu.py
# Purpose:     creates the menu screen, after clicking a button a quiz class is called
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------

from guizero import App, Text, PushButton, Box, Window
from mathematics import *
from chemistry import *
from geography import *
from english import *
from ultimate import *


class Menu:
    def __init__(self, app):
        self.app = app
        #------------------------------ Main Menu Window ------------------------------#
        # Menu containers from top to botton e.g container 1, 2, 3, 4, 5, 6, 7
        menu_container_1 = Box(self.app, width=700, height=100)
        menu_container_2 = Box(self.app, width=700, height=100)
        menu_container_3 = Box(self.app, width=700, height=100)
        menu_container_4 = Box(self.app, width=700, height=100)
        menu_container_5 = Box(self.app, width=700, height=100)
        menu_container_6 = Box(self.app, width=700, height=100)
        menu_container_7 = Box(self.app, width=700, height=100)

        # button container number 1
        filler_box_1 = Box(menu_container_2,
                           align="top", width=700, height=20)
        button_1_container = Box(menu_container_2,
                                 align="bottom",
                                 width=170,
                                 height=55)
        filler_box_2 = Box(menu_container_2,
                           align="bottom", width=700, height=20)

        # button  container number 2
        filler_box_3 = Box(menu_container_3,
                           align="top", width=700, height=20)
        button_2_container = Box(menu_container_3,
                                 align="bottom",
                                 width=170,
                                 height=55)
        filler_box_4 = Box(menu_container_3,
                           align="bottom", width=700, height=20)

        # button  container number 3
        filler_box_5 = Box(menu_container_4,
                           align="top", width=700, height=20)
        button_3_container = Box(menu_container_4,
                                 align="bottom",
                                 width=170,
                                 height=55)
        filler_box_6 = Box(menu_container_4,
                           align="bottom", width=700, height=20)

        # button  container number 4
        filler_box_7 = Box(menu_container_5,
                           align="top", width=700, height=20)
        button_4_container = Box(menu_container_5,
                                 align="bottom",
                                 width=170,
                                 height=55)
        filler_box_8 = Box(menu_container_5,
                           align="bottom", width=700, height=20)

        # button  container number 5
        filler_box_9 = Box(menu_container_6,
                           align="top", width=700, height=20)
        button_5_container = Box(menu_container_6,
                                 align="bottom",
                                 width=170,
                                 height=55)
        filler_box_10 = Box(
            menu_container_6, align="bottom", width=700, height=20)

        #-------------------------------Main Menu Buttons----------------------------------#

        Mathematics = PushButton(button_1_container,
                                 text="Mathematics",
                                 width=100,
                                 height=60,
                                 align="bottom",
                                 command=self.mathematics)
        Mathematics.bg = "#7D7268"
        Mathematics.font = "sans-serif"

        Chemistry = PushButton(button_2_container,
                               text="Chemistry",
                               width=100,
                               height=60,
                               align="bottom",
                               command=self.chemistry)
        Chemistry.bg = "#54C03D"
        Chemistry.font = "sans-serif"

        Geography = PushButton(button_3_container,
                               text="Geography",
                               width=100,
                               height=60,
                               align="bottom",
                               command=self.geography)
        Geography.bg = "#449BB0"
        Geography.font = "sans-serif"

        English = PushButton(button_4_container,
                             text="English",
                             width=100,
                             height=60,
                             align="bottom",
                             command=self.english)
        English.bg = "#FEAD5F"
        English.font = "sans-serif"

        UltimateTest = PushButton(button_5_container,
                                  text="Ultimate Test",
                                  width=100,
                                  height=60,
                                  align="bottom",
                                  command=self.ultimate)
        UltimateTest.bg = "#DB4692"
        UltimateTest.font = "sans-serif"

    def mathematics(self):
        mathematics = Mathematics(self.app)

    def chemistry(self):
        chemistry = Chemistry(self.app)

    def geography(self):
        geography = Geography(self.app)

    def english(self):
        english = English(self.app)

    def ultimate(self):
        ultimate = Ultimate(self.app)
