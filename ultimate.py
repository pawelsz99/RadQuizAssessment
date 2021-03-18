# -------------------------------------------------------------------------------
# Name:        ultimate.py
# Purpose:     responsible for ultimate quiz (all question combined)
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------


from guizero import App, Text, PushButton, Box, Window


class Ultimate:
    def __init__(self, app):
        app = app

        #-----------------------------Ultimate Window--------------------------------#

        ultimate_window = Window(app, width=700, height=700, bg="#FFED7C")

        # Quiz contantainers from top to bottom; ultimate_container_1 = Image container, ultimate_container_2 = Question container, ultimate_container_3 = filler container, ultimate_container_4 = upper answer button container, ultimate_container_5 = filler container, ultimate_container_6 = lower answer button container, ultimate_container_7 = bottom container with score and question
        ultimate_container_1 = Box(
            ultimate_window, width=700, height=250, border=2)
        ultimate_container_2 = Box(
            ultimate_window, width=700, height=100, border=2)
        ultimate_container_3 = Box(
            ultimate_window, width=700, height=25, border=2)
        ultimate_container_4 = Box(
            ultimate_window, width=700, height=100, border=2)
        ultimate_container_5 = Box(
            ultimate_window, width=700, height=25, border=2)
        ultimate_container_6 = Box(
            ultimate_window, width=700, height=100, border=2)
        ultimate_container_7 = Box(
            ultimate_window, width=700, height=100, border=2)

        # containers where the upper buttons are positioned
        ultimate_filler_box_1 = Box(ultimate_container_4,
                                    align="left",
                                    width=150,
                                    height=100)
        ultimate_filler_box_2 = Box(ultimate_container_4,
                                    align="right",
                                    width=150,
                                    height=100)
        ultimate_button_1 = Box(ultimate_container_4,
                                align="left",
                                width=180,
                                height=80)
        ultimate_button_2 = Box(ultimate_container_4,
                                align="right",
                                width=180,
                                height=80)

        # containers where the lower buttons are positioned
        ultimate_filler_box_3 = Box(ultimate_container_6,
                                    align="left",
                                    width=150,
                                    height=100)
        ultimate_filler_box_4 = Box(ultimate_container_6,
                                    align="right",
                                    width=150,
                                    height=100)
        ultimate_button_3 = Box(ultimate_container_6,
                                align="left",
                                width=180,
                                height=80)
        ultimate_button_4 = Box(ultimate_container_6,
                                align="right",
                                width=180,
                                height=80)

        # bottom section with score and questions
        ultimate_bottom = Box(ultimate_container_7,
                              align="bottom",
                              width=700,
                              height=50)
        ultimate_bottom_question = Box(ultimate_bottom,
                                       align="right",
                                       width=200,
                                       height=25)
        ultimate_bottom_score = Box(ultimate_bottom,
                                    align="left",
                                    width=100,
                                    height=25)

        #-----------------------------Ultimate Widgets--------------------------------#

        # Question Text
        ultimate_question = Text(ultimate_container_2,
                                 text="Question",
                                 width=100,
                                 height=100)
        ultimate_question.bg = "#FF8108"

        # Score & Question Num
        ultimate_question_number = Text(ultimate_bottom_question,
                                        text="Question Num: 1/10")
        ultimate_question_score = Text(ultimate_bottom_score, text="Score: 0")

        # Answer Buttons
        ultimate_answer_1 = PushButton(ultimate_button_1,
                                       align="left",
                                       width=100,
                                       height=70)
        ultimate_answer_1.bg = "#54C03D"
        ultimate_answer_1.font = "sans-serif"
        ultimate_answer_2 = PushButton(ultimate_button_2,
                                       align="right",
                                       width=100,
                                       height=70)
        ultimate_answer_2.bg = "#2D73A9"
        ultimate_answer_2.font = "sans-serif"
        ultimate_answer_3 = PushButton(ultimate_button_3,
                                       align="left",
                                       width=100,
                                       height=70)
        ultimate_answer_3.bg = "#DB4692"
        ultimate_answer_3.font = "sans-serif"
        ultimate_answer_4 = PushButton(ultimate_button_4,
                                       align="right",
                                       width=100,
                                       height=70)
        ultimate_answer_4.bg = "#FFFA13"
        ultimate_answer_4.font = "sans-serif"
