#-------------------------------------------------------------------------------
# Name:        chemistry.py
# Purpose:     responsible for chemistry quiz
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
#-------------------------------------------------------------------------------

from guizero import App, Text, PushButton, Box, Window

class Chemistry:
    def __init__(self, app):
        self.app = app

        #-----------------------------Chemistry Window--------------------------------#

        chemistry_window = Window(self.app, width=700, height=700, bg="#FFED7C")


        #once chemistry button is clicked, shows a new window of a quiz
        def show_chemistry():
            chemistry_window.show()


        #Quiz contantainers from top to bottom; chemistry_container_1 = Image container, chemistry_container_2 = Question container, chemistry_container_3 = filler container, chemistry_container_4 = upper answer button container, chemistry_container_5 = filler container, chemistry_container_6 = lower answer button container, chemistry_container_7 = bottom container with score and question
        chemistry_container_1 = Box(chemistry_window, width=700, height=250, border=2)
        chemistry_container_2 = Box(chemistry_window, width=700, height=100, border=2)
        chemistry_container_3 = Box(chemistry_window, width=700, height=25, border=2)
        chemistry_container_4 = Box(chemistry_window, width=700, height=100, border=2)
        chemistry_container_5 = Box(chemistry_window, width=700, height=25, border=2)
        chemistry_container_6 = Box(chemistry_window, width=700, height=100, border=2)
        chemistry_container_7 = Box(chemistry_window, width=700, height=100, border=2)

        #containers where the upper buttons are positioned
        chemistry_filler_box_1 = Box(chemistry_container_4,
                                    align="left",
                                    width=150,
                                    height=100)
        chemistry_filler_box_2 = Box(chemistry_container_4,
                                    align="right",
                                    width=150,
                                    height=100)
        chemistry_button_1 = Box(chemistry_container_4,
                                align="left",
                                width=180,
                                height=80)
        chemistry_button_2 = Box(chemistry_container_4,
                                align="right",
                                width=180,
                                height=80)

        #containers where the lower buttons are positioned
        chemistry_filler_box_3 = Box(chemistry_container_6,
                                    align="left",
                                    width=150,
                                    height=100)
        chemistry_filler_box_4 = Box(chemistry_container_6,
                                    align="right",
                                    width=150,
                                    height=100)
        chemistry_button_3 = Box(chemistry_container_6,
                                align="left",
                                width=180,
                                height=80)
        chemistry_button_4 = Box(chemistry_container_6,
                                align="right",
                                width=180,
                                height=80)

        #bottom section with score and questions
        chemistry_bottom = Box(chemistry_container_7,
                            align="bottom",
                            width=700,
                            height=50)
        chemistry_bottom_question = Box(chemistry_bottom,
                                        align="right",
                                        width=200,
                                        height=25)
        chemistry_bottom_score = Box(chemistry_bottom,
                                    align="left",
                                    width=100,
                                    height=25)

        #-----------------------------Chemistry Widgets------------------------------#

        #Question Text
        chemistry_question = Text(chemistry_container_2,
                                text="Question",
                                width=100,
                                height=100)
        chemistry_question.bg = "#FF8108"

        #Score & Question Num
        chemistry_question_number = Text(chemistry_bottom_question,
                                        text="Question Num: 1/10")
        chemistry_question_score = Text(chemistry_bottom_score, text="Score: 0")

        #Answer Buttons
        chemistry_answer_1 = PushButton(chemistry_button_1,
                                        align="left",
                                        width=100,
                                        height=70)
        chemistry_answer_1.bg = "#54C03D"
        chemistry_answer_1.font = "sans-serif"
        chemistry_answer_2 = PushButton(chemistry_button_2,
                                        align="right",
                                        width=100,
                                        height=70)
        chemistry_answer_2.bg = "#2D73A9"
        chemistry_answer_2.font = "sans-serif"
        chemistry_answer_3 = PushButton(chemistry_button_3,
                                        align="left",
                                        width=100,
                                        height=70)
        chemistry_answer_3.bg = "#DB4692"
        chemistry_answer_3.font = "sans-serif"
        chemistry_answer_4 = PushButton(chemistry_button_4,
                                        align="right",
                                        width=100,
                                        height=70)
        chemistry_answer_4.bg = "#FFFA13"
        chemistry_answer_4.font = "sans-serif"