# -------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     creates an app and calls menu class
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------


from guizero import App, Text, PushButton, Box, Window
from menu import *

#------------------------------Application Window------------------------------------#

app = App(title="Quiz Game", width=700, height=700, bg="#FFED7C")

menu = Menu(app)

app.display()
