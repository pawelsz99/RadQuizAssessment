# -------------------------------------------------------------------------------
# Name:        chemistry.py
# Purpose:     responsible for chemistry quiz
#
# Author:      OnlyChads
#
# Created:     15/03/2021
# Copyright:   (c) OnlyChads 2020
# -------------------------------------------------------------------------------

from guizero import App, Text, PushButton, Box, Window

from question import Question

list_questions = {
    1: Question("Text Q1", "Text q1a1", "Text q1a2", "Text q1a3", "Text q1a4"),
    2: Question("Text Q2", "Text q2a1", "Text q2a2", "Text q2a3", "Text q2a4"),
    3: Question("Text Q3", "Text q3a1", "Text q3a2", "Text q3a3", "Text q3a4"),
    4: Question("Text Q4", "Text q4a1", "Text q4a2", "Text q4a3", "Text q4a4"),
    5: Question("Text Q5", "Text q5a1", "Text q5a2", "Text q5a3", "Text q5a4"),
    6: Question("Text Q6", "Text q6a1", "Text q6a2", "Text q6a3", "Text q6a4"),
    7: Question("Text Q7", "Text q7a1", "Text q7a2", "Text q7a3", "Text q7a4"),
    8: Question("Text Q8", "Text q8a1", "Text q8a2", "Text q8a3", "Text q8a4"),
    9: Question("Text Q9", "Text q9a1", "Text q9a2", "Text q9a3", "Text q9a4"),
    10: Question("Text Q10", "Text q10a1", "Text q10a2", "Text q10a3", "Text q10a4")
}

questions_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
# this will be used in randomizing questions order


class Chemistry:
    def __init__(self, app):
        self.app = app

        #-----------------------------Chemistry Window--------------------------------#

        chemistry_window = Window(
            self.app, width=700, height=700, bg="#FFED7C")

        # once chemistry button is clicked, shows a new window of a quiz

        def show_chemistry():
            chemistry_window.show()

        # Quiz contantainers from top to bottom; chemistry_container_1 = Image container, chemistry_container_2 = Question container, chemistry_container_3 = filler container, chemistry_container_4 = upper answer button container, chemistry_container_5 = filler container, chemistry_container_6 = lower answer button container, chemistry_container_7 = bottom container with score and question
        chemistry_container_1 = Box(
            chemistry_window, width=700, height=250, border=2)
        chemistry_container_2 = Box(
            chemistry_window, width=700, height=100, border=2)
        chemistry_container_3 = Box(
            chemistry_window, width=700, height=25, border=2)
        chemistry_container_4 = Box(
            chemistry_window, width=700, height=100, border=2)
        chemistry_container_5 = Box(
            chemistry_window, width=700, height=25, border=2)
        chemistry_container_6 = Box(
            chemistry_window, width=700, height=100, border=2)
        chemistry_container_7 = Box(
            chemistry_window, width=700, height=100, border=2)

        # containers where the upper buttons are positioned
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

        # containers where the lower buttons are positioned
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

        # bottom section with score and questions
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

        # Question Text
        self.chemistry_question = Text(chemistry_container_2,
                                       text="Question",
                                       width=100,
                                       height=100)
        self.chemistry_question.bg = "#FF8108"

        # Score & Question Num
        self.chemistry_question_number = Text(chemistry_bottom_question,
                                              text="Question Num: 1/10")
        self.chemistry_question_score = Text(
            chemistry_bottom_score, text="Score: 0")

        # Answer Buttons
        self.chemistry_answer_1 = PushButton(chemistry_button_1,
                                             align="left",
                                             width=100,
                                             height=70,
                                             command=self.next_question)
        self.chemistry_answer_1.bg = "#54C03D"
        self.chemistry_answer_1.font = "sans-serif"
        self.chemistry_answer_2 = PushButton(chemistry_button_2,
                                             align="right",
                                             width=100,
                                             height=70,
                                             command=self.next_question)
        self.chemistry_answer_2.bg = "#2D73A9"
        self.chemistry_answer_2.font = "sans-serif"
        self.chemistry_answer_3 = PushButton(chemistry_button_3,
                                             align="left",
                                             width=100,
                                             height=70,
                                             command=self.next_question)
        self.chemistry_answer_3.bg = "#DB4692"
        self.chemistry_answer_3.font = "sans-serif"
        self.chemistry_answer_4 = PushButton(chemistry_button_4,
                                             align="right",
                                             width=100,
                                             height=70,
                                             command=self.next_question)
        self.chemistry_answer_4.bg = "#FFFA13"
        self.chemistry_answer_4.font = "sans-serif"

        self.next_question()

    def next_question(self):
        global counter
        q = list_questions[questions_order[counter]].get_q_text()
        a1 = list_questions[questions_order[counter]].get_a1_text()
        a2 = list_questions[questions_order[counter]].get_a2_text()
        a3 = list_questions[questions_order[counter]].get_a3_text()
        a4 = list_questions[questions_order[counter]].get_a4_text()

        self.chemistry_question.value = q

        self.chemistry_answer_1.text = a1
        self.chemistry_answer_2.text = a2
        self.chemistry_answer_3.text = a3
        self.chemistry_answer_4.text = a4

        counter += 1
