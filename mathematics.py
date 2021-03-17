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
from question import Question

list_questions = {
    1: Question("An empty container weighs 120g. When 50 lollipops were put in it the weight was 870g. What is the weight of one lollipop?", "15 Grams", "Text q1a2", "Text q1a3", "Text q1a4"),
    2: Question("Anne is going to Malta. How many euros will she get for £150 when the exchange rate is 1.18 euros to a pound?", "177 euros ", "Text q2a2", "Text q2a3", "Text q2a4"),
    3: Question("A car travels at a constant speed of 63 mph for 20 minutes. How far does the car travel in this time? (pic)", "21 miles ", "Text q3a2", "Text q3a3", "Text q3a4"),
    4: Question("A liquid is warmed from –3C to +5C. By how many degrees has its temperature risen?", "By 8 ", "Text q4a2", "Text q4a3", "Text q4a4"),
    5: Question("Some water has been added to this measuring jar. How much more water is needed to fill the jar to 1.5 litres? (pic)", "0.6 litres", "Text q5a2", "Text q5a3", "Text q5a4"),
    6: Question("The number of pupils in each year group in a secondary school was recorded and this pie chart drawn. There are 1200 pupils in the school. How many pupils were there in S5/6? (pic)", "200 pupils", "Text q6a2", "Text q6a3", "Text q6a4"),
    7: Question("The number of people using a gym each day was recorded for a week and this compound bar chart was drawn. Who has used the gym the most? Male of Female? (pic)", "Female ", "Text q7a2", "Text q7a3", "Text q7a4"),
    8: Question("Sally scored the following marks in three of her tests. Maths: 25 out of 40 English: 32 out of 50 Science: 38 out of 60 In which subject did she do best in?", "English ", "Text q8a2", "Text q8a3", "Text q8a4"),
    9: Question("Calculate the perimeter of the shape. (pic)", "52 cm", "Text q9a2", "Text q9a3", "Text q9a4"),
    10: Question("Increase £80 by 60%", "128£", "Text q10a2", "Text q10a3", "Text q10a4")
}

questions_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
order_counter = 0
# this will be used in randomizing questions order


class Mathematics:
    def __init__(self, app):
        app = app
        global order_counter
        order_counter = 0
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
        self.math_question = Text(mathematics_container_2,
                                  text="Question",
                                  width=100,
                                  height=100)
        self.math_question.bg = "#FF8108"

        # Score & Question Num
        self.math_question_number = Text(mathematics_bottom_question,
                                         text="Question Num: 1/10")
        self.math_question_score = Text(
            mathematics_bottom_score, text="Score: 0")

        # Answer Buttons
        self.math_answer_1 = PushButton(mathematics_button_1,
                                        align="left",
                                        width=100,
                                        height=70,
                                        command=self.next_question)
        self.math_answer_1.bg = "#54C03D"
        self.math_answer_1.font = "sans-serif"
        self.math_answer_2 = PushButton(mathematics_button_2,
                                        align="right",
                                        width=100,
                                        height=70,
                                        command=self.next_question)
        self.math_answer_2.bg = "#2D73A9"
        self.math_answer_2.font = "sans-serif"
        self.math_answer_3 = PushButton(mathematics_button_3,
                                        align="left",
                                        width=100,
                                        height=70,
                                        command=self.next_question)
        self.math_answer_3.bg = "#DB4692"
        self.math_answer_3.font = "sans-serif"
        self.math_answer_4 = PushButton(mathematics_button_4,
                                        align="right",
                                        width=100,
                                        height=70,
                                        command=self.next_question)
        self.math_answer_4.bg = "#FFFA13"
        self.math_answer_4.font = "sans-serif"

        self.next_question()

    def next_question(self):
        global order_counter
        q = list_questions[questions_order[order_counter]].get_q_text()
        a1 = list_questions[questions_order[order_counter]].get_a1_text()
        a2 = list_questions[questions_order[order_counter]].get_a2_text()
        a3 = list_questions[questions_order[order_counter]].get_a3_text()
        a4 = list_questions[questions_order[order_counter]].get_a4_text()

        self.math_question.value = q

        self.math_answer_1.text = a1
        self.math_answer_2.text = a2
        self.math_answer_3.text = a3
        self.math_answer_4.text = a4

        order_counter += 1
