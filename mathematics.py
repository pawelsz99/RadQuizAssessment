# -------------------------------------------------------------------------------
# Name:        mathematics.py
# Purpose:     responsible for maths quiz
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------

from guizero import App, Text, PushButton, Box, Window


class Mathematics:
    def __init__(self, app):
        app = app
        #------------------------------Mathematics Window-----------------------------------#

        math_window = Window(app, width=700, height=700, bg="#FFED7C")

        # Quiz contantainers from top to bottom; mathematics_container_1 = Image container, mathematics_container_2 = Question container, mathematics_container_3 = filler container, mathematics_container_4 = upper answer button container, mathematics_container_5 = filler container, mathematics_container_6 = lower answer button container, mathematics_container_7 = bottom container with score and question
        mathematics_container_1 = Box(
            math_window, width=700, height=250, border=2)
        mathematics_container_2 = Box(
            math_window, width=700, height=100, border=2)
        mathematics_container_3 = Box(
            math_window, width=700, height=25, border=2)
        mathematics_container_4 = Box(
            math_window, width=700, height=100, border=2)
        mathematics_container_5 = Box(
            math_window, width=700, height=25, border=2)
        mathematics_container_6 = Box(
            math_window, width=700, height=100, border=2)
        mathematics_container_7 = Box(
            math_window, width=700, height=100, border=2)

        # containers where the upper buttons are positioned
        math_filler_box_1 = Box(mathematics_container_4,
                                align="left",
                                width=150,
                                height=100)
        math_filler_box_2 = Box(mathematics_container_4,
                                align="right",
                                width=150,
                                height=100)
        mathematics_button_1 = Box(mathematics_container_4,
                                   align="left",
                                   width=180,
                                   height=80)
        mathematics_button_2 = Box(mathematics_container_4,
                                   align="right",
                                   width=180,
                                   height=80)

        # containers where the lower buttons are positioned
        math_filler_box_3 = Box(mathematics_container_6,
                                align="left",
                                width=150,
                                height=100)
        math_filler_box_4 = Box(mathematics_container_6,
                                align="right",
                                width=150,
                                height=100)
        mathematics_button_3 = Box(mathematics_container_6,
                                   align="left",
                                   width=180,
                                   height=80)
        mathematics_button_4 = Box(mathematics_container_6,
                                   align="right",
                                   width=180,
                                   height=80)

        # bottom section with score and questions
        mathematics_bottom = Box(mathematics_container_7,
                                 align="bottom",
                                 width=700,
                                 height=50)
        mathematics_bottom_question = Box(mathematics_bottom,
                                          align="right",
                                          width=200,
                                          height=25)
        mathematics_bottom_score = Box(mathematics_bottom,
                                       align="left",
                                       width=100,
                                       height=25)

        #-----------------------------Mathematics Widgets------------------------------#

        # Question Text
        math_question = Text(mathematics_container_2,
                             text="Question",
                             width=100,
                             height=100)
        math_question.bg = "#FF8108"

        # Score & Question Num
        math_question_number = Text(mathematics_bottom_question,
                                    text="Question Num: 1/10")
        math_question_score = Text(mathematics_bottom_score, text="Score: 0")

        # Answer Buttons
        math_answer_1 = PushButton(mathematics_button_1,
                                   align="left",
                                   width=100,
                                   height=70)
        math_answer_1.bg = "#54C03D"
        math_answer_1.font = "sans-serif"
        math_answer_2 = PushButton(mathematics_button_2,
                                   align="right",
                                   width=100,
                                   height=70)
        math_answer_2.bg = "#2D73A9"
        math_answer_2.font = "sans-serif"
        math_answer_3 = PushButton(mathematics_button_3,
                                   align="left",
                                   width=100,
                                   height=70)
        math_answer_3.bg = "#DB4692"
        math_answer_3.font = "sans-serif"
        math_answer_4 = PushButton(mathematics_button_4,
                                   align="right",
                                   width=100,
                                   height=70)
        math_answer_4.bg = "#FFFA13"
        math_answer_4.font = "sans-serif"
