# -------------------------------------------------------------------------------
# Name:        geography.py
# Purpose:     responsible for geography quiz
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------

from guizero import App, Text, PushButton, Box, Window


class Geography:
    def __init__(self, app):
        app = app
        #-----------------------------Geography Window--------------------------------#

        geography_window = Window(app, width=700, height=700, bg="#FFED7C")

        # Quiz contantainers from top to bottom; geography_container_1 = Image container, geography_container_2 = Question container, geography_container_3 = filler container, geography_container_4 = upper answer button container, geography_container_5 = filler container, geography_container_6 = lower answer button container, geography_container_7 = bottom container with score and question
        geography_container_1 = Box(
            geography_window, width=700, height=250, border=2)
        geography_container_2 = Box(
            geography_window, width=700, height=100, border=2)
        geography_container_3 = Box(
            geography_window, width=700, height=25, border=2)
        geography_container_4 = Box(
            geography_window, width=700, height=100, border=2)
        geography_container_5 = Box(
            geography_window, width=700, height=25, border=2)
        geography_container_6 = Box(
            geography_window, width=700, height=100, border=2)
        geography_container_7 = Box(
            geography_window, width=700, height=100, border=2)

        # containers where the upper buttons are positioned
        geography_filler_box_1 = Box(geography_container_4,
                                     align="left",
                                     width=150,
                                     height=100)
        geography_filler_box_2 = Box(geography_container_4,
                                     align="right",
                                     width=150,
                                     height=100)
        geography_button_1 = Box(geography_container_4,
                                 align="left",
                                 width=180,
                                 height=80)
        geography_button_2 = Box(geography_container_4,
                                 align="right",
                                 width=180,
                                 height=80)

        # containers where the lower buttons are positioned
        geography_filler_box_3 = Box(geography_container_6,
                                     align="left",
                                     width=150,
                                     height=100)
        geography_filler_box_4 = Box(geography_container_6,
                                     align="right",
                                     width=150,
                                     height=100)
        geography_button_3 = Box(geography_container_6,
                                 align="left",
                                 width=180,
                                 height=80)
        geography_button_4 = Box(geography_container_6,
                                 align="right",
                                 width=180,
                                 height=80)

        # bottom section with score and questions
        geography_bottom = Box(geography_container_7,
                               align="bottom",
                               width=700,
                               height=50)
        geography_bottom_question = Box(geography_bottom,
                                        align="right",
                                        width=200,
                                        height=25)
        geography_bottom_score = Box(geography_bottom,
                                     align="left",
                                     width=100,
                                     height=25)

        #-----------------------------Geography Widgets--------------------------------#

        # Question Text
        geography_question = Text(geography_container_2,
                                  text="Question",
                                  width=100,
                                  height=100)
        geography_question.bg = "#FF8108"

        # Score & Question Num
        geography_question_number = Text(geography_bottom_question,
                                         text="Question Num: 1/10")
        geography_question_score = Text(
            geography_bottom_score, text="Score: 0")

        # Answer Buttons
        geography_answer_1 = PushButton(geography_button_1,
                                        align="left",
                                        width=100,
                                        height=70)
        geography_answer_1.bg = "#54C03D"
        geography_answer_1.font = "sans-serif"
        geography_answer_2 = PushButton(geography_button_2,
                                        align="right",
                                        width=100,
                                        height=70)
        geography_answer_2.bg = "#2D73A9"
        geography_answer_2.font = "sans-serif"
        geography_answer_3 = PushButton(geography_button_3,
                                        align="left",
                                        width=100,
                                        height=70)
        geography_answer_3.bg = "#DB4692"
        geography_answer_3.font = "sans-serif"
        geography_answer_4 = PushButton(geography_button_4,
                                        align="right",
                                        width=100,
                                        height=70)
        geography_answer_4.bg = "#FFFA13"
        geography_answer_4.font = "sans-serif"
