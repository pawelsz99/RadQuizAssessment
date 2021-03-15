# -------------------------------------------------------------------------------
# Name:        english.py
# Purpose:     responsible for english quiz
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------

from guizero import App, Text, PushButton, Box, Window


class English:
    def __init__(self, app):
        app = app

        #-----------------------------English Window--------------------------------#

        english_window = Window(app, width=700, height=700, bg="#FFED7C")

        # Quiz contantainers from top to bottom; english_container_1 = Image container, english_container_2 = Question container, english_container_3 = filler container, english_container_4 = upper answer button container, english_container_5 = filler container, english_container_6 = lower answer button container, english_container_7 = bottom container with score and question
        english_container_1 = Box(
            english_window, width=700, height=250, border=2)
        english_container_2 = Box(
            english_window, width=700, height=100, border=2)
        english_container_3 = Box(
            english_window, width=700, height=25, border=2)
        english_container_4 = Box(
            english_window, width=700, height=100, border=2)
        english_container_5 = Box(
            english_window, width=700, height=25, border=2)
        english_container_6 = Box(
            english_window, width=700, height=100, border=2)
        english_container_7 = Box(
            english_window, width=700, height=100, border=2)

        # containers where the upper buttons are positioned
        english_filler_box_1 = Box(english_container_4,
                                   align="left",
                                   width=150,
                                   height=100)
        english_filler_box_2 = Box(english_container_4,
                                   align="right",
                                   width=150,
                                   height=100)
        english_button_1 = Box(english_container_4,
                               align="left", width=180, height=80)
        english_button_2 = Box(english_container_4,
                               align="right",
                               width=180,
                               height=80)

        # containers where the lower buttons are positioned
        english_filler_box_3 = Box(english_container_6,
                                   align="left",
                                   width=150,
                                   height=100)
        english_filler_box_4 = Box(english_container_6,
                                   align="right",
                                   width=150,
                                   height=100)
        english_button_3 = Box(english_container_6,
                               align="left", width=180, height=80)
        english_button_4 = Box(english_container_6,
                               align="right",
                               width=180,
                               height=80)

        # bottom section with score and questions
        english_bottom = Box(english_container_7,
                             align="bottom", width=700, height=50)
        english_bottom_question = Box(english_bottom,
                                      align="right",
                                      width=200,
                                      height=25)
        english_bottom_score = Box(
            english_bottom, align="left", width=100, height=25)

        #-----------------------------English Widgets--------------------------------#

        # Question Text
        english_question = Text(english_container_2,
                                text="Question",
                                width=100,
                                height=100)
        english_question.bg = "#FF8108"

        # Score & Question Num
        english_question_number = Text(english_bottom_question,
                                       text="Question Num: 1/10")
        english_question_score = Text(english_bottom_score, text="Score: 0")

        # Answer Buttons
        english_answer_1 = PushButton(english_button_1,
                                      align="left",
                                      width=100,
                                      height=70)
        english_answer_1.bg = "#54C03D"
        english_answer_1.font = "sans-serif"
        english_answer_2 = PushButton(english_button_2,
                                      align="right",
                                      width=100,
                                      height=70)
        english_answer_2.bg = "#2D73A9"
        english_answer_2.font = "sans-serif"
        english_answer_3 = PushButton(english_button_3,
                                      align="left",
                                      width=100,
                                      height=70)
        english_answer_3.bg = "#DB4692"
        english_answer_3.font = "sans-serif"
        english_answer_4 = PushButton(english_button_4,
                                      align="right",
                                      width=100,
                                      height=70)
        english_answer_4.bg = "#FFFA13"
        english_answer_4.font = "sans-serif"
